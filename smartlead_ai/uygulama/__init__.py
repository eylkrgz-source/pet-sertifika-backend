from flask import Flask
from flask_cors import CORS
from ayarlar import ayar_secici
from uygulama.database import veritabani_baslat

def uygulama_olustur(ayar_adi=None):
    uygulama = Flask(__name__, template_folder='sablonlar')
    
    secilen_ayar = ayar_secici.get(ayar_adi, ayar_secici['uretim'])
    uygulama.config.from_object(secilen_ayar)
    
    CORS(
        uygulama,
        origins=uygulama.config.get('CORS_ALLOWED_ORIGINS', '*'),
        methods=['GET', 'POST', 'OPTIONS']
    )
    
    with uygulama.app_context():
        veritabani_baslat(uygulama)
        
    from uygulama.rotalar import api_arayuzu
    uygulama.register_blueprint(api_arayuzu, url_prefix='/api')
    
    return uygulama