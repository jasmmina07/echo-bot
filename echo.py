import requests
from pprint import pprint
TOKEN="5959656588:AAFRUBI1vozVI4ScI9HCVu3YRk2qd_6PjxQ"

from time import sleep

base_url = f"https://api.telegram.org/bot{TOKEN}"

def get_updates():
    update = requests.get(f"{base_url}/getUpdates")
    data = update.json()
    return data['result']

def send_message(chat_id, text):
    parameters = {
        "chat_id": chat_id,
        "text": text
    }

    r = requests.get(f"{base_url}/sendMessage", params=parameters)
    return r.json()


last_message_id = -1

while True:
    msgs = get_updates()
    last_msg = msgs[-1]
    
    message_id = last_msg['message']['message_id']

    chat_id = last_msg['message']['chat']['id']
    text = last_msg['message']['text']

    print(last_message_id, message_id)
    if last_message_id != message_id:
        
        send_message(chat_id, text)

        last_message_id = message_id
    
    sleep(2)