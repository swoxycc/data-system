import requests
from itertools import cycle
from colorama import Fore, Style, init


init(autoreset=True)

print(Fore.GREEN + "----------------------------------------------------------------" + Style.RESET_ALL)
print("")
print(Fore.GREEN + " ╔═╗╦ ╦╔═╗═╗ ╦╦ ╦  ╦  ╔═╗╔═╗  ╔═╗╦ ╦╔═╗╔╦╗╔═╗╔╦╗" + Style.RESET_ALL)
print(Fore.GREEN + " ╚═╗║║║║ ║╔╩╦╝╚╦╝  ║  ║ ║║ ╦  ╚═╗╚╦╝╚═╗ ║ ║╣ ║║║" + Style.RESET_ALL)
print(Fore.GREEN + " ╚═╝╚╩╝╚═╝╩ ╚═ ╩   ╩═╝╚═╝╚═╝  ╚═╝ ╩ ╚═╝ ╩ ╚═╝╩ ╩" + Style.RESET_ALL)
print("")
print("")

print(Fore.GREEN + "API : V9 / V10"+ Style.RESET_ALL)

print(Fore.GREEN + "----------------------------------------------------------------" + Style.RESET_ALL)

source_channel_id = int(input("[+] Verilerin Çekilecegi Kanal İD : "))  
dest_channel_id = int(input("[+] Verilerin Aktarılacağı Kanal İD : "))  
print(" ")

base_url = 'https://discord.com/api/v9'
print("Veriler Başarıyla Çekiliyor...")

with open('tokens.txt') as f:
    tokens = f.read().splitlines()

token_cycle = cycle(tokens)

while True:
    token = next(token_cycle)
  
    headers = {
        'Authorization': f'{token}'
    }

    response = requests.get(f'{base_url}/channels/{source_channel_id}/messages', headers=headers)
  
    for message in response.json():
        requests.post(f'{base_url}/channels/{dest_channel_id}/messages', json=message, headers=headers)
