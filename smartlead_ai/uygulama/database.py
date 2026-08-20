import sqlite3
import os
from flask import current_app

def baglanti_al():
    db_yolu = current_app.config.get('DATABASE_URL', 'akilli_satis.db')
    baglanti = sqlite3.connect(db_yolu)
    baglanti.row_factory = sqlite3.Row
    return baglanti

def veritabani_baslat(app):
    db_yolu = app.config.get('DATABASE_URL', 'akilli_satis.db')
    baglanti = sqlite3.connect(db_yolu)
    imlec = baglanti.cursor()
    
    imlec.execute('''
        CREATE TABLE IF NOT EXISTS analiz_talepleri (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT NOT NULL,
            telefon TEXT NOT NULL,
            firma_adi TEXT,
            belge_detayi TEXT,
            olusturulma_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    baglanti.commit()
    baglanti.close()

def talep_ekle(isim, telefon, firma_adi='', belge_detayi=''):
    baglanti = baglanti_al()
    imlec = baglanti.cursor()
    imlec.execute(
        'INSERT INTO analiz_talepleri (isim, telefon, firma_adi, belge_detayi) VALUES (?, ?, ?, ?)',
        (isim, telefon, firma_adi, belge_detayi)
    )
    baglanti.commit()
    baglanti.close()

def tum_talepleri_getir():
    baglanti = baglanti_al()
    imlec = baglanti.cursor()
    imlec.execute('SELECT * FROM analiz_talepleri ORDER BY olusturulma_tarihi DESC')
    satirlar = imlec.fetchall()
    baglanti.close()
    return [dict(satir) for satir in satirlar]