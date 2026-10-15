import urllib.request

try:
    # Tenta abrir o site do pudim
    site = urllib.request.urlopen('https://www.youtube.com')
except urllib.error.URLError:
    print('WEBSITE NOT FOUND!999')
else:
    print('Website acessado com sucesso.\n')
    # .decode('utf-8') transforma os bytes em texto limpo
    print(site.read().decode('utf-8'))