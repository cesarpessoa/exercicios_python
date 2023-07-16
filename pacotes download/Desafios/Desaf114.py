import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
    #site = urllib.request.urlopen("https://www.agencialiderdigital.com br")
except urllib.error.URLError:
    print(f'1\033[31mO Site pudim não está acessível no momento.\033[m')
else:
    print(f'\033[34mConsegui acessar o Site Pudim com sucesso!\033[m')
    #print(site.read())