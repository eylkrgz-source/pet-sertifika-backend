import os
from dotenv import load_dotenv

load_dotenv()

class Ayarlar:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'varsayilan-gizli-anahtar')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'akilli_satis.db')
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')
    AI_PROVIDER = os.environ.get('AI_PROVIDER', 'groq')
    BUSINESS_CONTEXT = os.environ.get(
        'BUSINESS_CONTEXT',
        'Sen evcil hayvan sertifika ve analiz danışmanısın. Müşterilere kibar, profesyonel bilgi ver ve onları form doldurmaya yönlendir.'
    )
    CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', '*')
    DEBUG = False

class GelistirmeAyarlari(Ayarlar):
    DEBUG = True

class UretimAyarlari(Ayarlar):
    DEBUG = False

ayar_secici = {
    'gelistirme': GelistirmeAyarlari,
    'uretim': UretimAyarlari
}