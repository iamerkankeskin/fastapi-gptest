from dotenv import load_dotenv
import os

load_dotenv()  # .env dosyasını manuel olarak yükle

# .env'den DATABASE_URL'yi doğru şekilde alıp almadığını kontrol et
print("DATABASE_URL from env:", os.getenv("DATABASE_URL"))