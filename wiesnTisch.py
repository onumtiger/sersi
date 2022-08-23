from env import *
import json
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


#whatsapp request data
data = {"messaging_product": "whatsapp", "to": f"{phone_number}", "type": "template",
        "template": {"name": f"{template_name}", "language": {"code": "de"}}}
encoded_data = json.dumps(data).encode('utf-8')

if paulaner_website_inhalt == "":
    pass
 
elif wartemeldung not in paulaner_website_inhalt:
    http.request('GET', einzelchat_url+einkaufsnachricht)
    http.request('GET', gruppenchat_url+einkaufsnachricht)
    http.request(
        'POST',
        f'https://graph.facebook.com/v14.0/{whatsapp_id}/messages',
        body=encoded_data,
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {whatsapp_token}'
        }

    )
