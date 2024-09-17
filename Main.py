import phonenumbers
from phonenumbers import timezone, geocoder, carrier

# Input the phone number
number = input("Enter your number: ")

# Parse the phone number
phone = phonenumbers.parse(number)

# Get the time zones for the number
time_zones = timezone.time_zones_for_number(phone)

# Get the carrier for the number
car = carrier.name_for_number(phone, "en")

# Get the region for the number (e.g., India)
country = geocoder.country_name_for_number(phone, "en")

# Get the location (specific region or state, e.g., Gujarat)
region = geocoder.description_for_number(phone, "en")

# Print the results
print(f"Phone number: {phone}")
print(f"Time zones: {time_zones}")
print(f"Carrier: {car}")
print(f"Country: {country}")
print(f"Region: {region}")