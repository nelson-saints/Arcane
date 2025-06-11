
# Projeto de WEB + IA

O projto se trata de um Oráculo: uma aplicação web integrada a um agente de IA, desenvolvida para auxiliar equipes comerciais na consulta de informações sobre a empresa.

O projeto consta com upload de arquivos e treinamentos de IA e Chat em tempo real.
## Siga os passos para rodar o projeto.


Crie seu ambiente virtual:
```bash
  python -m venv venv
```

Ative seu ambiente virual.

instale o Django:
```bash
  pip install django
```

Defina sua chave OPENAI,
crie um arquivo 
```bash
   .env
``` 
dentro deste arquivo defina sua chave da seguinte forma: 
```bash
  OPENAI_API_KEY= valor da chave
```
Ative o cluster para alimentar a IA. 
```bash
  python manage.py qcluster
```
Inicie o servidor django e utilize a aplicação.