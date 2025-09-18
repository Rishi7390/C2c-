import requests

try:
    # Use a free and reliable public API to get the IP
    response = requests.get('https://api.ipify.org')
    public_ip = response.text
    print(f"My public IP address is: {public_ip}")
except requests.RequestException as e:
    print(f"Error: Could not retrieve public IP address. {e}")