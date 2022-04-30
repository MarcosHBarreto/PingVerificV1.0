import os
import time

print('Bem-vindo(a) ao PingStatus.')
time.sleep(5)
print()

print('Inicializando...')
time.sleep(5)
print()

ip_host = input('Insira o IP ou Host: ')

os.system(f'Ping -n 5 {ip_host}')