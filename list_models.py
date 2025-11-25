import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

# .env yükle
load_dotenv(find_dotenv(), override=True)
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ HATA: API Key bulunamadı!")
else:
    genai.configure(api_key=api_key)
    
    print("🔍 Hesabınız için uygun modeller listeleniyor...\n")
    try:
        found_any = False
        for m in genai.list_models():
            # Sadece metin üretebilen (generateContent) modelleri göster
            if 'generateContent' in m.supported_generation_methods:
                print(f"✅ Model Adı: {m.name}")
                found_any = True
        
        if not found_any:
            print("⚠️ Hiçbir uygun model bulunamadı. API Key yetkilerini kontrol edin.")
            
    except Exception as e:
        print(f"❌ HATA: {e}")