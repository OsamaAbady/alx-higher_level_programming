import telegram ,time
import requests, json, os
from datetime import datetime
name = 'tassssssneem'

def gtall(name, d):
    add = lambda x, y: [f'\n\n{n+y}:\nTime: {datetime.utcfromtimestamp(post["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")}\nMessage: {post["comment"]}\nReply: {post["reply"]}' for n, post in enumerate(x)]
    dct, n, last = {}, 0, 0
    with open(f'{name}\\answers.txt','w', encoding='utf-8') as db:
        db.write(f'Answers: {d["answers"]}')
        if not d['posts']:
            db.write('\n\n[No Messages _/(0_0)\_]')
            return
        dct = json.loads(
                requests.get(
            f'https://curiouscat.me/api/v2/profile?username={name}&count=1'
                        ).content.decode()
                )
        db.write(''.join(add(dct['posts'], n + 1)))
        n += len(dct['posts'])
    
        if not dct['posts']:
            return


def cc():
    name = 'tassssssneem'
    dct = json.loads(requests.get(f'https://curiouscat.me/api/v2/profile?username={name}').content.decode())
    if 'error' in dct:
        print("\nProfile doesn't exist!")
        return
    os.makedirs(f'{name}', exist_ok=True)
    gtall(name, dct)
p = 0     
while True:
    cc()
    dct = json.loads(requests.get(f'https://curiouscat.me/api/v2/profile?username={name}').content.decode())
    if 'error' in dct:
        print("\nProfile doesn't exist!")
        break

    answers = dct['answers']
    if answers > p :
        
        
        # Replace TOKEN with your bot's token
        bot = telegram.Bot('5628245599:AAGP60JoW4LUDyr50GK3xOZJIlmyuTKyjIQ')
        # Replace CHAT_ID with the chat ID of the chat where you want to send the message
        chat_id = 406520300
        # Set the path of the text file that you want to send
        FILE_PATH = "tassssssneem\\answers.txt"
        # Read the contents of the text file
        with open(FILE_PATH, "r") as f:
            text = f.read()
            bot.send_message(chat_id=chat_id, text=text)
            p = answers
    time.sleep(5)
