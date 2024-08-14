# syntax=docker/dockerfile:1 #definicao de sintax

#imagens que eu estou utilizando em python
FROM python:3.8-slim-buster

#pasta criada dentro do conteiner docker 
WORKDIR /app 
ENV FLASK_APP run.py

#pedindo para o docker copiar e instalar dentro do container 
COPY requirements.txt requirements.txt
RUN pip install -r requiriments.txt

COPY . .

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]

