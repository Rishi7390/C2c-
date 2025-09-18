import ipaddress
import geocoder

def check_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        if ip_obj.is_private:
            print(f"{ip} is a private IP. Location cannot be determined.")
        else:
            g = geocoder.ip(ip)
            print(f"{ip} location info:")
            print("Country:", g.country)
            print("City:", g.city)
            print("Latitude:", g.latlng[0] if g.latlng else None)
            print("Longitude:", g.latlng[1] if g.latlng else None)
    except ValueError:
        print("Invalid IP address")

# Example usage
ip_input = input("Enter an IP address: ")
check_ip(ip_input)
