import phonenumbers
from phonenumbers import geocoder, carrier

print("\nPhone Numbers Location\n")

# Your main number (Amritsar area)
phone_number1 = phonenumbers.parse("+917889121072")

# Other examples from your code
phone_number2 = phonenumbers.parse("+918878586271")
phone_number3 = phonenumbers.parse("+12136574429")
phone_number4 = phonenumbers.parse("+201234567890")

numbers = [
    (phone_number1, "Your Number (+917889121072 - Expected: Punjab/Amritsar area)"),
    (phone_number2, "Number 2 (+918878586271)"),
    (phone_number3, "Number 3 (+12136574429 - US)"),
    (phone_number4, "Number 4 (+201234567890 - Egypt)")
]

for num, label in numbers:
    try:
        if phonenumbers.is_valid_number(num):
            location = geocoder.description_for_number(num, "en")
            operator = carrier.name_for_number(num, "en")
            print(f"{label}")
            print(f"   State/Circle: {location or 'India (no specific state data)'}")
            print(f"   Operator: {operator or 'Unknown'}")
            print(f"   Valid: Yes")
        else:
            print(f"{label}: Invalid number")
    except Exception as e:
        print(f"{label}: Error - {e}")
    print("---")

print("\n# LET'S CHECK PHONE NUMBER REGIONS (Approximate only!)")
print("Note: This shows the original allocated state, not exact current address.")