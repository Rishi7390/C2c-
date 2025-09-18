import phonenumbers
from phonenumbers import geocoder
phone_number1= phonenumbers.parse("+919350523682")
print("\n Phone number location \n")
print(geocoder.description_for_number(phone_number1,"en"))