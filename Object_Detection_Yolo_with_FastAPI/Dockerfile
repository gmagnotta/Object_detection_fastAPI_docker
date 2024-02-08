# Python imajını kullanın
FROM python:3.10

# Gerekli paketleri yükleyin
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    libgl1

# Uygulama dosyalarını Docker imajına kopyala
COPY . /app

# Uygulamanın çalıştırılacağı dizini belirtin
WORKDIR /app

# Gerekli Python paketlerini yükleyin
RUN pip install -r requirements.txt

# Uygulamayı çalıştırın
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
