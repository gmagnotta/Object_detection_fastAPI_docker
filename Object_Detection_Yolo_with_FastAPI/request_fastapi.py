import requests

# API endpoint URL
api_endpoint = "http://localhost:8000/detect/"

# Resim dosyasının adı
image_filename = "bus.jpg"

# Etiket parametresi
label = ""

# Resmi yükleme
files = {"image": open(image_filename, "rb")}

# API endpoint URL'sini ve etiket parametresini birleştirme
api_endpoint_with_label = f"{api_endpoint}?label={label}" if label else api_endpoint

# POST isteği gönderme
response = requests.post(api_endpoint_with_label, files=files)

# Yanıtı kontrol etme
if response.status_code == 200:
    # Başarılı yanıt
    result = response.json()
    print(result)
else:
    # Hata durumu
    print("API request failed:", response.text)
