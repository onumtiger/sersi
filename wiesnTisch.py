from env import *
import urllib3
http = urllib3.PoolManager()

# requests urls
paulaner_wiesntisch_url = 'https://paulanerfestzelt.de/reservierung/muenchner-tische/'
gruppenchat_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={group_id}&text="
einzelchat_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text="

# strings
wartemeldung = "Termin wird noch bekannt gegeben"
einkaufsnachricht = f"WIESNTISCH BESTELLEN SOFORT UNTER: {paulaner_wiesntisch_url}"
wartenachricht = "Es wurde noch kein Datum bekannt gegeben..."

# website überprüfen
paulaner_website_response = http.request('GET', paulaner_wiesntisch_url)
paulaner_website_inhalt = paulaner_website_response.data.decode("utf-8")

if wartemeldung not in paulaner_website_inhalt:
    http.request('GET', einzelchat_url+einkaufsnachricht)
    http.request('GET', gruppenchat_url+einkaufsnachricht)
