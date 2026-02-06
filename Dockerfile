FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Instala dependências
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia código
COPY . .

# Copia entrypoint
COPY entrypoint.sh .

# Executa entrypoint no runtime
CMD ["./entrypoint.sh"]
