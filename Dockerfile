# Use uma imagem base do Python como ponto de partida
FROM python:3.8

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo de requisitos para o contêiner
COPY requirements.txt .

# Instale as dependências usando o pip
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código-fonte da aplicação Flask para o contêiner
COPY . .

# Exponha a porta em que a aplicação Flask irá rodar (por padrão, a porta 5000)
EXPOSE 5000

# Comando para criar o banco de dados e iniciar a aplicação Flask
CMD ["bash", "-c", "python -c 'from app import db; db.create_all()'; python app.py"]
