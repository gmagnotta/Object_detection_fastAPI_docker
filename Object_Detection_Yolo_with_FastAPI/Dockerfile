# Python taban imajını kullan
FROM python:3.9-slim

# Uygulamanın çalıştırılacağı dizini belirt
WORKDIR /app

# Gerekli dosyaları kopyala
COPY requirements.txt .

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y libgl1

# Uygulama kodunu kopyala
COPY . .

# Uygulamayı çalıştır
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
