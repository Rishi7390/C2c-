import os
import sqlite3
import win32crypt

def get_chrome_passwords():
    # Path to Chrome 'Login Data' database
    chrome_db = os.path.expanduser(
        r"~\AppData\Local\Google\Chrome\User Data\Default\Login Data"
    )

    # Make a copy because Chrome may be using it
    import shutil
    temp_db = "ChromeTemp.db"
    shutil.copy2(chrome_db, temp_db)

    # Connect to the database
    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()
    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")

    print("Saved Chrome passwords:\n")
    for row in cursor.fetchall():
        url = row[0]
        username = row[1]
        encrypted_password = row[2]

        try:
            # Decrypt the password
            decrypted_password = win32crypt.CryptUnprotectData(
                encrypted_password, None, None, None, 0
            )[1]
            print(f"URL: {url}\nUsername: {username}\nPassword: {decrypted_password.decode()}\n")
        except:
            print(f"Could not decrypt password for {url}\n")

    conn.close()
    os.remove(temp_db)

if __name__ == "__main__":
    get_chrome_passwords()
