from langchain.docstore.document import Document
from langchain_community.document_loaders import PyPDFLoader
import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.cache import cache
import datetime
from .wrapper_evolutionapi import SendMessage
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from datetime import datetime, timedelta


def html_para_texto_rag(html_str: str) -> str:
    soup = BeautifulSoup(html_str, "html.parser")
    texto_final = []

    for tag in soup.find_all(["h1", "h2", "h3", "p", "li",]):
        texto = tag.get_text(strip=True)

        if not texto:
            continue

        if tag.name in ["h1", "h2", "h3"]:
            texto_formatado = f"\n\n### {texto.upper()}"
        elif tag.name == "li":
            texto_formatado = f" - {texto}"
        else:
            texto_formatado = texto

        texto_final.append(texto_formatado)
        
    return "\n".join(texto_final).strip()


def gerar_documentos(instance):
    documentos = []
    if instance.documento:
        extensao = instance.documento.name.split('.')[-1].lower()
        if extensao == 'pdf':
            loader = PyPDFLoader(instance.documento.path)
            pdf_doc = loader.load()
            for doc in pdf_doc:
                doc.metadata['url'] = instance.documento.url
            documentos += pdf_doc
    if instance.conteudo:
        document = Document(page_content=instance.conteudo)
        documentos.append(document)

    if instance.site:
        site_url = instance.site if instance.site.startswith('https://') else f'https://{instance.site}'
        content = requests.get(site_url, timeout=10).text
        content = html_para_texto_rag(content)
        documentos.append(Document(page_content=content))   

    return documentos
