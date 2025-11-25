import asyncio
from src.core.agent import GeminiAgent

async def main():
    print("🤖 Gemini Agent Test Ediliyor...")
    
    # Agent'ı başlat
    agent = GeminiAgent()
    
    # 1. Basit Metin Testi
    print("\n--- TEST 1: Basit Soru ---")
    soru = "Yazılım dünyasında 'Hello World' neden gelenektir? Kısaca anlat."
    print(f"Soru: {soru}")
    try:
        cevap = await agent.generate_with_retry(soru)
        print(f"✅ Cevap: {cevap}")
    except Exception as e:
        print(f"❌ Hata: {e}")

    # 2. JSON Testi (Native JSON Mode)
    print("\n--- TEST 2: JSON Üretimi ---")
    json_soru = "Bana Python, Java ve C++ dillerini popülerliklerine göre sırala ve JSON döndür."
    print(f"İstek: {json_soru}")
    try:
        json_cevap = await agent.generate_json_response(json_soru)
        print(f"✅ JSON Çıktısı:\n{json_cevap}")
        print(f"Veri Tipi: {type(json_cevap)}") # <class 'dict'> veya 'list' olmalı
    except Exception as e:
        print(f"❌ JSON Hata: {e}")

if __name__ == "__main__":
    asyncio.run(main())