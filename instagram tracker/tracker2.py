import phonenumbers
from phonenumbers import geocoder

# Example phone numbers (with international format starting with +)
phone_number1 = phonenumbers.parse("+917889121072", None)  # Your original (invalid - will show nothing)
phone_number2 = phonenumbers.parse("+918878586271", None)  # Likely the one that printed Kakinada
phone_number3 = phonenumbers.parse("+12136574429", None)   # US number
phone_number4 = phonenumbers.parse("+201234567890", None)  # Egypt number

# A valid example Indian number for demonstration
valid_indian = phonenumbers.parse("+919876543210", None)

print("\nPhone Numbers Location\n")

def print_location(number, name):
    try:
        location = geocoder.description_for_number(number, "en")
        if location:
            print(f"{name}: {location}")
        else:
            print(f"{name}: Invalid or no location data available")
    except Exception as e:
        print(f"{name}: Error - {e}")

print_location(phone_number1, "Phone Number 1 (+917889121072)")
print_location(phone_number2, "Phone Number 2 (+918878586271)")
print_location(phone_number3, "Phone Number 3 (+12136574429)")
print_location(phone_number4, "Phone Number 4 (+201234567890)")
print_location(valid_indian, "Valid Indian Example (+919876543210)")

print("\n# LET'S TRACK PHONE NUMBERS")