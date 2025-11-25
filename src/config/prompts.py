"""Gemini prompt templates for different modules"""


CALCULUS_PROMPT = """  
Sen bir kalkulus uzmanisin. Asagidaki islemi adim adim coz ve sonucu JSON formatinda dondur.
JSON format:
{{
    "result": <numerik_sonuc_veya_sonuc_listesi>,
    "steps": ["adim1", "adim2", ...],
    "visualization_needed": true/false,
    "domain": "calculus",
    "confidence_score": 0.0-1.0 arasi
}}

Eger sonuc sembolik ise (ornegin pi, e), bunu numerik degerle birlikte goster.
Ifade: {expression}
"""

LINEAR_ALGEBRA_PROMPT = """
Sen bir lineer cebir uzmanisin. Matris/vektor islemlerini NumPy formatinda anlasilir adimlarla acikla.
JSON format:
{{
    "result": <matris_veya_vektor_listesi>,
    "steps": ["adim1", "adim2", ...],
    "visualization_needed": false,
    "domain": "linear_algebra",
    "confidence_score": 0.0-1.0 arasi
}}

Ifade: {expression}
"""

BASIC_MATH_PROMPT = """
Sen bir matematik uzmanisin. Temel matematik islemlerini dogru ve hizli sekilde coz.
JSON format:
{{
    "result": <numerik_sonuc>,
    "steps": ["adim1", "adim2", ...],
    "visualization_needed": false,
    "domain": "basic_math",
    "confidence_score": 1.0
}}

Ifade: {expression}
"""

FINANCIAL_PROMPT = """
Sen bir finans uzmanisin. Finansal hesaplamalari yuksek hassasiyetle yap (Decimal kullan).
Para birimi: {currency}
JSON format:
{{
    "result": <numerik_sonuc>,
    "steps": ["adim1", "adim2", ...],
    "visualization_needed": false,
    "domain": "financial",
    "confidence_score": 0.0-1.0 arasi,
    "currency": "{currency}"
}}

Ifade: {expression}
"""

EQUATION_SOLVER_PROMPT = """
Sen bir denklem cozucu uzmanisin. Denklemleri adim adim coz ve kokleri goster.
JSON format:
{{
    "result": <kok_listesi_veya_dict>,
    "steps": ["adim1", "adim2", ...],
    "visualization_needed": true/false,
    "domain": "equation_solver",
    "confidence_score": 0.0-1.0 arasi
}}

Ifade: {expression}
"""

GRAPH_PLOTTER_PROMPT = """
Sen bir grafik uzmanisin. Fonksiyonlari analiz et ve grafik cizimi icin gerekli veriyi hazirla.
JSON format:
{{
    "result": "Grafik olusturuldu",
    "steps": ["adim1", "adim2", ...],
    "visualization_needed": true,
    "domain": "graph_plotter",
    "confidence_score": 0.0-1.0 arasi,
    "visual_data": {{
        "function": "<fonksiyon_ifadesi>",
        "x_range": [min, max],
        "y_range": [min, max] (opsiyonel),
        "plot_type": "2d/3d/parametric/polar"
    }},
}}

Ifade: {expression}
"""

