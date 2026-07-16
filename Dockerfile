# Imagem base oficial do Python
FROM python:3.12-slim

# Evita geração de arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Permite logs imediatos no terminal
ENV PYTHONUNBUFFERED=1

# Diretório interno da aplicação
WORKDIR /app

# Copia dependências primeiro para aproveitar cache do Docker
COPY requirements.txt .

# Atualiza pip e instala dependências
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copia todo o projeto
COPY . .

# Comando padrão da aplicação
CMD ["python", "main.py"]