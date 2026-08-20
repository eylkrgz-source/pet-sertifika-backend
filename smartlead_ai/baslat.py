from uygulama import uygulama_olustur

uygulama = uygulama_olustur()

if __name__ == '__main__':
    uygulama.run(host='0.0.0.0', port=5000, debug=True)