import requests
from flask import current_app

class YapayZekaServisHatasi(Exception):
    pass

class YapayZekaServisi:
    def yanit_uret(self, kullanici_mesaji, sohbet_gecmisi=None):
        saglayici = current_app.config.get('AI_PROVIDER', 'groq').lower()
        
        if saglayici == 'groq':
            return self._groq_cagir(kullanici_mesaji, sohbet_gecmisi)
        else:
            return self._demo_yaniti_ver(kullanici_mesaji)

    def _groq_cagir(self, mesaj, gecmis=None):
        api_key = current_app.config.get('GROQ_API_KEY')
        if not api_key:
            return self._demo_yaniti_ver(mesaj)
            
        baglam = current_app.config.get('BUSINESS_CONTEXT', '')
        mesajlar = [{"role": "system", "content": baglam}]
        
        if gecmis:
            mesajlar.extend(gecmis)
        mesajlar.append({"role": "user", "content": mesaj})
        
        try:
            cevap = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "llama-3.3-70b-versatile",
                    "messages": mesajlar,
                    "temperature": 0.7
                },
                timeout=15
            )
            veri = cevap.json()
            return veri['choices'][0]['message']['content']
        except Exception as e:
            raise YapayZekaServisHatasi(f"Yapay zeka servisi yanıt veremedi: {str(e)}")

    def _demo_yaniti_ver(self, mesaj):
        return "Sistem demo modunda çalışıyor. Lütfen GROQ API anahtarınızı kontrol edin."

yapay_zeka_servisi = YapayZekaServisi()