import asyncio
import os
from dotenv import load_dotenv, find_dotenv

# 1. Önce .env dosyasını ZORLA yükle (Override=True ile eskisini ez)
env_path = find_dotenv()
print(f"📂 .env Dosyası Yolu: {env_path}")
load_dotenv(env_path, override=True)

# 2. Anahtarı al
my_api_key = os.getenv("GOOGLE_API_KEY")

print(f"🔑 Okunan Anahtar (İlk 5): {my_api_key[:5]}...")
print(f"🔑 Okunan Anahtar (Son 5): ...{my_api_key[-5:]}")

# Agent'ı import et (Burası settings'i yükler ama biz anahtarı elle vereceğiz)
from src.core.agent import GeminiAgent

async def main():
    print("\n🤖 Agent, MANUEL anahtar ile başlatılıyor...")
    
    # KRİTİK NOKTA: Anahtarı settings'den değil, doğrudan buradan veriyoruz
    agent = GeminiAgent(api_key=my_api_key)
    
    try:
        print("📡 Google'a istek gönderiliyor...")
        cevap = await agent.generate_with_retry("Merhaba, sistem çalışıyor mu?")
        print(f"\n✅ BAŞARILI! Cevap: {cevap}")
    except Exception as e:
        print(f"\n❌ HATA DEVAM EDİYOR: {e}")

if __name__ == "__main__":
    asyncio.run(main())