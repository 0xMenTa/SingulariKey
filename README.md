![](https://raw.githubusercontent.com/0xMenTa/SingulariKey/refs/heads/main/images/singularikey_banner.png)

🐦‍⬛​ Welcome to the Singularikey project. Coded in Python, the aim of the project is to understand how it works and to improve my level of code. For now, the code is pretty simple, with multiples functionnality.

## ✨ Features

- ⌨️ Basic keylogger functionnality : records all keys pressed by the user (I'm using keyboard module)
- 📄 More clarity in recording result : UTF-8 encoding, Special & Function key highlighted + anti-repeat function
- 📆 Timestamp for each recording session
- 📥 Buffering system
- 👃 Clipboard Sniffer : Intercepts and logs clipboard contents when Ctrl+C is detected.
- 🚀 Sends log files to a configured remote server after a cooldown period.
- 🚀 Sends a Telegram message notification with system information upon upload.
- 🧼 Overwrites log file contents with random bytes after sending to avoid recovery.
- 🪟 Optimized for Windows

## ⚙️ Configuration

You can customize the following values in the class constructor:

```
self.output_file = "result.txt"          # Output log file
self.buffer_size = 50                    # Max buffer length before writing to file
self.telegram_token = "[TOKEN]"          # Telegram bot API token
self.telegram_chatid = "[CHATID]"        # Telegram chat ID for notifications
self.srv_url = "http://localhost:5000/upload"  # Server endpoint for file uploads
self.srv_cooldown = 60000                # Time in seconds between each file upload
```

## 🔧 Requirements

- `Python 3.X`
- `keyboard` library
- `requests` library

Install dependencies :

```
pip install keyboard requests
```

## ⚠️ DISCLAIMER
This project is intended strictly for educational and ethical research purposes only. Unauthorized access or data collection without user consent is illegal and unethical. Use responsibly.

More coming soon...
