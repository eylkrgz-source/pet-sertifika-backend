from flask import Blueprint, request, jsonify
from uygulama.servisler.yapay_zeka_servisi import yapay_zeka_servisi, YapayZekaServisHatasi
from uygulama.database import talep_ekle, tum_talepleri_getir

api_arayuzu = Blueprint('api', __name__)

@api_arayuzu.route('/sohbet', methods=['POST'])
def sohbet_et():
    veri = request.json or {}
    mesaj = veri.get('mesaj')
    gecmis = veri.get('gecmis', [])
    
    if not mesaj:
        return jsonify({'basari': False, 'hata': 'Mesaj boş olamaz.'}), 400
        
    try:
        cevap = yapay_zeka_servisi.yanit_uret(mesaj, gecmis)
        return jsonify({'basari': True, 'cevap': cevap})
    except YapayZekaServisHatasi as e:
        return jsonify({'basari': False, 'hata': str(e)}), 503

@api_arayuzu.route('/talepler', methods=['POST'])
def talep_kaydet():
    veri = request.json or {}
    isim = veri.get('isim')
    telefon = veri.get('telefon')
    firma = veri.get('firma_adi', '')
    belge_detayi = veri.get('belge_detayi', '')
    
    if not isim or not telefon:
        return jsonify({'basari': False, 'hata': 'İsim ve telefon zorunludur.'}), 400
        
    talep_ekle(isim, telefon, firma, belge_detayi)
    return jsonify({'basari': True, 'mesaj': 'Talebiniz başarıyla kaydedildi.'})

@api_arayuzu.route('/talepler', methods=['GET'])
def talepleri_listele():
    talepler = tum_talepleri_getir()
    return jsonify({'basari': True, 'toplam': len(talepler), 'talepler': talepler})