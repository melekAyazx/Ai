import os
from dotenv import load_dotenv, find_dotenv

print("--- API ANAHTARI KONTROLÜ ---")

# 1. .env dosyasını bulmaya çalış
env_path = find_dotenv()
if env_path:
    print(f"✅ .env dosyası bulundu: {env_path}")
else:
    print("❌ .env dosyası BULUNAMADI!")

# 2. Dosyayı zorla yeniden yükle (override=True önemli)
load_dotenv(env_path, override=True)

# 3. Anahtarı oku
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ GOOGLE_API_KEY değişkeni boş veya okunamadı.")
else:
    print(f"✅ Anahtar okundu. Uzunluk: {len(api_key)} karakter.")
    print(f"👀 Anahtarın Başlangıcı: {api_key[:4]}****") # Güvenlik için sadece başını gösteriyoruz
    print(f"👀 Anahtarın Bitişi: ****{api_key[-4:]}")
    
    # 4. Gizli boşluk kontrolü (En sık yapılan hata)
    if " " in api_key:
        print("⚠️ UYARI: Anahtar içinde BOŞLUK karakteri var! Lütfen silin.")
    else:
        print("✅ Anahtar içinde boşluk yok.")

print("-------------------------------")