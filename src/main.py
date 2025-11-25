import asyncio
import sys
from pathlib import Path
from typing import Optional

# Proje root'unu Python path'ine ekle
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.core.agent import GeminiAgent
from src.core.parser import CommandParser
from src.core.validator import InputValidator
from src.config.settings import settings
from src.utils.logger import setup_logger

# Modülleri içe aktar (Henüz olmayanları yorum satırı yapabilirsiniz)
from src.modules.basic_math import BasicMathModule
# from src.modules.calculus import CalculusModule
# from src.modules.linear_algebra import LinearAlgebraModule
# from src.modules.financial import FinancialModule
# from src.modules.equation_solver import EquationSolverModule
# from src.modules.graph_plotter import GraphPlotterModule

from src.utils.exceptions import (
    CalculationError,
    InvalidInputError,
    SecurityViolationError,
    ModuleNotFoundError,
)

logger = setup_logger()
APP_NAME = "Calculator Agent"
APP_VERSION = "1.0.0"

class CalculatorAgent:
    """Ana calculator agent orchestrator"""

    def __init__(self):
        # Ayarları doğrula
        try:
            settings.validate()
        except ValueError as e:
            logger.error(f"Settings validation error: {e}")
            raise

        self.gemini_agent = GeminiAgent()
        self.parser = CommandParser()
        self.validator = InputValidator()

        # Modülleri başlat
        # NOT: Henüz oluşturmadığınız modülleri buradan geçici olarak kapattım.
        # Dosyaları oluşturdukça yorum satırlarını açabilirsiniz.
        self.modules = {
            "basic_math": BasicMathModule(self.gemini_agent),
            # "calculus": CalculusModule(self.gemini_agent),
            # "linear_algebra": LinearAlgebraModule(self.gemini_agent),
            # "financial": FinancialModule(self.gemini_agent),
            # "equation_solver": EquationSolverModule(self.gemini_agent),
            # "graph_plotter": GraphPlotterModule(self.gemini_agent),
        }

        logger.info("Calculator Agent başlatıldı")

    async def process_command(self, user_input: str) -> Optional[str]:
        """Kullanıcı komutunu işler"""
        try:
            # Komutu parse et (Hangi modül? Hangi işlem?)
            module_name, expression = self.parser.parse(user_input)
            
            # Güvenlik kontrolü
            self.validator.sanitize_expression(expression)

            # Modül var mı kontrol et
            if module_name not in self.modules:
                # Eğer parser bir modül buldu ama bizde yüklü değilse basic_math'e yönlendir (Fallback)
                if "basic_math" in self.modules:
                    module_name = "basic_math"
                else:
                    raise ModuleNotFoundError(f"Modül bulunamadı: {module_name}")

            module = self.modules[module_name]
            logger.info(f"Processing: {module_name} - {expression}")

            # Hesaplamayı yap
            result = await module.calculate(expression)
            
            # Sonucu formatla ve döndür
            return self._format_output(result)

        except SecurityViolationError as e:
            return f"❌ Güvenlik Hatası: {e}"
        except InvalidInputError as e:
            return f"⚠️ Geçersiz Giriş: {e}"
        except ModuleNotFoundError as e:
            return f"🔍 Modül Hatası: {e}"
        except CalculationError as e:
            return f"🧮 Hesaplama Hatası: {e}"
        except Exception as e:
            logger.error(f"Unexpected error: {e}", exc_info=True)
            return f"💥 Beklenmeyen Hata: {e}"

    def _format_output(self, result) -> str:
        """Sonucu kullanıcı dostu ve şık bir formatta gösterir"""
        output = []
        separator = "=" * 50
        
        output.append(separator)
        output.append(f"🤖 Modül: {result.domain.upper()}")
        output.append(separator)

        # 1. Sonuç Kısmı
        if result.result:
            # Eğer sonuç çok uzunsa veya liste ise düzgün göster
            res_str = str(result.result)
            output.append(f"🎯 Sonuç: {res_str}")
        else:
            output.append("ℹ️  Sonuç: (Bilgi/Sohbet yanıtı)")

        # 2. Adımlar Kısmı
        if result.steps:
            output.append("\n📝 Adımlar:")
            for i, step in enumerate(result.steps, start=1):
                clean_step = str(step).strip()
                output.append(f"  {i}. {clean_step}")

        # 3. Güven Skoru (Sadece düşükse göster)
        if result.confidence_score < 0.8:
            output.append(f"\n⚠️ Güven Skoru: {result.confidence_score:.2f}")

        # 4. Görsel Veri (Grafik vs.)
        if result.visual_data and "plot_paths" in result.visual_data:
            png = result.visual_data["plot_paths"].get("png")
            if png:
                output.append(f"\n📈 Grafik Oluşturuldu: {png}")

        output.append(separator)
        return "\n".join(output)

async def interactive_mode():
    """İnteraktif mod"""
    agent = CalculatorAgent()

    print("\n" + "=" * 60)
    print(f"🤖 AI AGENT BAŞLATILDI - v{APP_VERSION}")
    print("=" * 60)
    print("Çıkmak için 'q', 'quit' veya 'exit' yazabilirsiniz.\n")

    while True:
        try:
            user_input = input("\nSen > ").strip()

            if user_input.lower() in ["quit", "exit", "q"]:
                print("\n👋 Görüşmek üzere! Çıkış yapılıyor...")
                break

            if not user_input:
                continue

            # İşleniyor mesajı (isteğe bağlı, yavaş bağlantılarda iyi olur)
            print("⏳ Düşünüyor...", end="\r")
            
            result = await agent.process_command(user_input)
            
            # Satırı temizle
            print(" " * 20, end="\r")
            
            if result:
                print(result)
                
        except KeyboardInterrupt:
            print("\n\nİşlem iptal edildi.")
            break
        except Exception as e:
            print(f"\nKritik Hata: {e}")

async def single_command_mode(expression: str):
    """Tek komut modu"""
    agent = CalculatorAgent()
    result = await agent.process_command(expression)
    if result:
        print(result)

def main():
    """Ana giriş noktası"""
    if len(sys.argv) > 1:
        expression = " ".join(sys.argv[1:])
        asyncio.run(single_command_mode(expression))
    else:
        asyncio.run(interactive_mode())

if __name__ == "__main__":
    main()