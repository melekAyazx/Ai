# 🧮 Calculator Agent - AI Builder Challenge Hackathon

## 📋 Hackathon Hakkında

Bu proje, **AI Builder Challenge 2-Day Hackathon** için hazırlanmış bir "Broken Calculator Agent" challenge'ıdır. Projede **12 kritik hata** ve **100+ derleme hatası** gizlidir. Katılımcıların görevi bu hataları tespit edip düzeltmek ve projeye **yeni bir modül** eklemektir.

### 🎯 Hackathon Hedefleri

- **Gün 1**: Syntax ve runtime hatalarını bulup düzeltmek
- **Gün 2**: Silent failures'ı tespit etmek ve yeni modül eklemek
- **Bonus**: CI/CD pipeline kurmak ve dokümantasyon tamamlamak

### 📊 Puanlama Sistemi

- **Level 1 Hatalar (Syntax)**: 10 puan/hata (Toplam 40 puan)
- **Level 2 Hatalar (Runtime)**: 20 puan/hata (Toplam 60 puan)
- **Level 3 Hatalar (Silent Failures)**: 30 puan/hata (Toplam 60 puan)
- **Bonus Modül**: 40 puan
- **CI/CD**: 20 puan
- **Dokümantasyon**: 10 puan
- **Toplam**: 230 puan

---

## 🚀 Proje Hakkında

Google Gemini Gen AI SDK kullanılarak geliştirilmiş modüler, genişletilebilir bir hesaplama agent'ı. Proje şu anda **çalışmayan durumda** ve hackathon katılımcıları tarafından düzeltilmesi gerekiyor.

### ✨ Mevcut Özellikler

- **Modüler Yapı**: Her hesaplama türü bağımsız modüller halinde
- **Gemini AI Entegrasyonu**: Google Gemini ile akıllı hesaplama
- **Çoklu Domain Desteği**:
  - Temel Matematik (+, -, \*, /, sqrt, log, trigonometri)
  - Kalkülüs (limit, türev, integral, seri)
  - Lineer Cebir (matris, vektör, determinant)
  - Finansal Hesaplamalar (NPV, IRR, faiz, kredi)
  - Denklem Çözücü (doğrusal, polinom, diferansiyel)
  - Grafik Çizim (2D/3D plotlar)

---

## 🔧 Kurulum

### Gereksinimler

- Python 3.11+
- Google Gemini API Key
- Git

### Adımlar

1. **Repository'yi klonlayın:**

```bash
git clone <repository-url>
cd CalculatorAgent
```

2. **Sanal ortam oluşturun:**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Bağımlılıkları yükleyin:**

```bash
pip install -r requirements.txt
```

4. **Environment değişkenlerini ayarlayın:**

```bash
cp .env.example .env
# .env dosyasını düzenleyip GEMINI_API_KEY'inizi ekleyin
```

---

## 🐛 Hata Kategorileri

### Level 1: Syntax Hataları (10 puan/hata)

Bu hatalar derleme anında tespit edilir ve projenin çalışmasını engeller.

**Örnek Hata Tipleri:**

- Circular import hataları
- Eksik parantezler
- Yanlış indentasyon
- Tanımlanmamış değişkenler

**Çözüm Şablonu:**

```python
# HATA: [Hata açıklaması]
# Dosya: [dosya_yolu]
# Satır: [satır_numarası]

# MEVCUT KOD (HATALI):
[hatalı_kod_buraya]

# ÇÖZÜM:
[çözüm_kodunuz_buraya]

# AÇIKLAMA:
[çözümünüzü_neden_bu_şekilde_yaptığınızı_açıklayın]
```

**Alternatif Çözümler:**

- [Alternatif çözüm 1 açıklaması]
- [Alternatif çözüm 2 açıklaması]

---

### Level 2: Runtime Hataları (20 puan/hata)

Bu hatalar çalışma zamanında ortaya çıkar ve uygulamanın crash etmesine neden olur.

**Örnek Hata Tipleri:**

- API key güvenlik zaafiyetleri
- Sıfıra bölme hataları
- Yanlış metod çağrıları
- Dictionary key hataları

**Çözüm Şablonu:**

```python
# HATA: [Hata açıklaması]
# Dosya: [dosya_yolu]
# Satır: [satır_numarası]
# Hata Tipi: Runtime Error / KeyError / ValueError

# MEVCUT KOD (HATALI):
[hatalı_kod_buraya]

# ÇÖZÜM:
[çözüm_kodunuz_buraya]

# TEST:
[çözümünüzü_nasıl_test_ettiğiniz]

# AÇIKLAMA:
[çözümünüzü_neden_bu_şekilde_yaptığınızı_açıklayın]
```

**Alternatif Çözümler:**

- [Alternatif çözüm 1 açıklaması]
- [Alternatif çözüm 2 açıklaması]

---

### Level 3: Silent Failures (30 puan/hata)

Bu hatalar en zor tespit edilenlerdir. Uygulama çalışır gibi görünür ama yanlış sonuçlar üretir.

**Örnek Hata Tipleri:**

- Rate limit bypass
- Logging yapılandırma hataları
- Tip dönüşüm hataları
- Async blocking sorunları

**Çözüm Şablonu:**

```python
# HATA: [Hata açıklaması]
# Dosya: [dosya_yolu]
# Satır: [satır_numarası]
# Hata Tipi: Silent Failure / Logic Error

# MEVCUT KOD (HATALI):
[hatalı_kod_buraya]

# PROBLEM ANALİZİ:
[hatayı_nasıl_tespit_ettiğiniz]

# ÇÖZÜM:
[çözüm_kodunuz_buraya]

# TEST:
[çözümünüzü_nasıl_test_ettiğiniz]

# AÇIKLAMA:
[çözümünüzü_neden_bu_şekilde_yaptığınızı_açıklayın]
```

**Alternatif Çözümler:**

- [Alternatif çözüm 1 açıklaması]
- [Alternatif çözüm 2 açıklaması]

---

## 🎯 Hata Çözüm Rehberi

### 1. Hata Tespit Stratejisi

**Adım 1: Derleme Hatalarını Bulun**

```bash
# Python syntax kontrolü
python -m py_compile src/**/*.py

# Linter kullanımı
pylint src/
flake8 src/
```

**Adım 2: Runtime Hatalarını Test Edin**

```bash
# Basit test çalıştırma
python -m src.main "2 + 2"

# Test suite çalıştırma
pytest tests/
```

**Adım 3: Silent Failures İçin Debug**

```bash
# Logging seviyesini artırın
export LOG_LEVEL=DEBUG
python -m src.main

# Profiling ile performans analizi
python -m cProfile -o profile.stats src/main.py
```

### 2. Hata Çözüm Yaklaşımları

**Yaklaşım 1: Minimal Değişiklik**

- Sadece hatayı düzeltin
- Minimum kod değişikliği
- Hızlı çözüm

**Yaklaşım 2: Refactoring**

- Kodu yeniden yapılandırın
- Daha iyi mimari
- Uzun vadeli çözüm

**Yaklaşım 3: Defensive Programming**

- Ekstra kontroller ekleyin
- Hata yakalama mekanizmaları
- Güvenli çözüm

### 3. Test Stratejisi

Her hatayı düzelttikten sonra:

```python
# Unit Test Örneği
def test_fixed_error():
    """Düzeltilen hatanın testi"""
    # Arrange
    [test_verileri]

    # Act
    [test_aksiyonu]

    # Assert
    [beklenen_sonuç]
```

---

## 🆕 Eklenen Özellikler

Hackathon sırasında projeye eklediğiniz yeni özellikleri buraya dokümante edin.

### Yeni Modül: [Modül Adı]

**Açıklama:**
[Yeni modülünüzün ne yaptığını açıklayın]

**Kullanım:**

```python
# Kullanım örneği
[örnek_kod]
```

**Özellikler:**

- [Özellik 1]
- [Özellik 2]
- [Özellik 3]

**Test Coverage:**

```bash
pytest tests/modules/test_[modül_adı].py --cov
```

**Dosya Yapısı:**

```
src/modules/
├── [modül_adı].py
└── ...

tests/modules/
├── test_[modül_adı].py
└── ...
```

---

### Diğer Eklenen Özellikler

#### 1. [Özellik Adı]

**Açıklama:**
[Özelliğin açıklaması]

**Kullanım:**

```python
[örnek_kod]
```

**Faydalar:**

- [Fayda 1]
- [Fayda 2]

---

#### 2. [Özellik Adı]

**Açıklama:**
[Özelliğin açıklaması]

**Kullanım:**

```python
[örnek_kod]
```

**Faydalar:**

- [Fayda 1]
- [Fayda 2]

---

## 🧪 Test Sonuçları

### Test Coverage

```bash
# Coverage raporu
pytest --cov=src --cov-report=html
```

**Coverage Sonuçları:**

- **Toplam Coverage**: [%XX]
- **Modüller**: [%XX]
- **Core**: [%XX]
- **Utils**: [%XX]

### Test Sonuçları

```bash
# Test çalıştırma
pytest -v
```

**Sonuçlar:**

- ✅ Başarılı Testler: [sayı]
- ❌ Başarısız Testler: [sayı]
- ⏭️ Atlanan Testler: [sayı]

---

## 📊 Hata Çözüm Özeti

### Çözülen Hatalar

| Hata No | Kategori | Dosya   | Satır   | Durum | Puan |
| ------- | -------- | ------- | ------- | ----- | ---- |
| 1       | Level 1  | [dosya] | [satır] | ✅    | 10   |
| 2       | Level 1  | [dosya] | [satır] | ✅    | 10   |
| 3       | Level 2  | [dosya] | [satır] | ✅    | 20   |
| ...     | ...      | ...     | ...     | ...   | ...  |

### Toplam Puan

- **Level 1 Hatalar**: [X] / 40 puan
- **Level 2 Hatalar**: [X] / 60 puan
- **Level 3 Hatalar**: [X] / 60 puan
- **Bonus Modül**: [X] / 40 puan
- **CI/CD**: [X] / 20 puan
- **Dokümantasyon**: [X] / 10 puan
- **TOPLAM**: [X] / 230 puan

---

## 🚀 CI/CD Pipeline

### GitHub Actions / GitLab CI

**Pipeline Yapılandırması:**

```yaml
# .github/workflows/ci.yml veya .gitlab-ci.yml
[pipeline_yapılandırmanız]
```

**Pipeline Adımları:**

1. [Adım 1]
2. [Adım 2]
3. [Adım 3]

**Pipeline Durumu:**

- ✅ Build: [durum]
- ✅ Test: [durum]
- ✅ Lint: [durum]
- ✅ Deploy: [durum]

---

## 📝 Kodlama Standartları

Projede uyulması gereken standartlar:

- **Async/Await**: Tüm Gemini API çağrılarında async pattern
- **Type Hints**: Tüm fonksiyonlarda zorunlu tip belirtilmesi
- **Google Docstring**: Dokümantasyon formatı
- **Pydantic Models**: Input/output validasyonu
- **Test Coverage**: Minimum %90 unit test coverage

---

## 🔒 Güvenlik İyileştirmeleri

Hackathon sırasında yaptığınız güvenlik iyileştirmeleri:

### 1. [Güvenlik İyileştirmesi]

**Problem:**
[Güvenlik sorunu]

**Çözüm:**
[Çözüm açıklaması]

**Kod:**

```python
[çözüm_kodu]
```

---

## 🏗️ Proje Yapısı

```
calculator-agent/
├── src/
│   ├── main.py                 # Agent orchestrator ve UI entry point
│   ├── config/
│   │   ├── settings.py         # API keys, modeller, rate limiting
│   │   └── prompts.py          # Gemini prompt templates
│   ├── core/
│   │   ├── agent.py            # Gemini ile iletişim layer'ı
│   │   ├── parser.py           # Doğal dil → semantik komut
│   │   └── validator.py        # Giriş doğrulama ve güvenlik
│   ├── modules/
│   │   ├── base_module.py      # Abstract base class
│   │   ├── calculus.py         # Kalkülüs modülü
│   │   ├── linear_algebra.py   # Lineer cebir modülü
│   │   ├── basic_math.py       # Temel matematik
│   │   ├── financial.py        # Finansal modül
│   │   ├── equation_solver.py  # Denklem çözücü
│   │   ├── graph_plotter.py    # Grafik çizim modülü
│   │   └── [yeni_modül].py     # Eklediğiniz yeni modül
│   ├── utils/
│   │   ├── logger.py           # Yapılandırılmış logging
│   │   ├── exceptions.py       # Custom exception'lar
│   │   └── helpers.py          # Ortak yardımcı fonksiyonlar
│   └── schemas/
│       └── models.py           # Pydantic modelleri
├── tests/
│   ├── conftest.py
│   ├── test_integration.py
│   └── modules/
│       ├── test_calculus.py
│       ├── test_linear_algebra.py
│       └── test_[yeni_modül].py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 🎓 Öğrenilen Dersler

Hackathon sırasında öğrendiğiniz önemli dersler:

1. **[Ders 1]**

   - [Açıklama]

2. **[Ders 2]**

   - [Açıklama]

3. **[Ders 3]**
   - [Açıklama]

---


## 📄 Lisans

Bu proje AI Builder Challenge hackathon'u için geliştirilmiştir.



**İyi hackathonlar! 🚀**
