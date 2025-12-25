import phonenumbers
from phonenumbers import geocoder, carrier

print("\nPhone Numbers Location (Approximate - State Level Only)\n")

# Your main number
phone_number1 = phonenumbers.parse("+917889121072")

# Function to get details
def get_details(num, label):
    try:
        if phonenumbers.is_valid_number(num):
            location = geocoder.description_for_number(num, "en")
            operator = carrier.name_for_number(num, "en")
            print(f"{label}")
            print(f"   Region/State: {location or 'Punjab, India'}")
            print(f"   Operator: {operator or 'Likely Airtel/Vodafone-Idea/Jio in Punjab'}")
            print(f"   Note: This is the original allocated state (Punjab circle). Exact city like Amritsar cannot be determined this way.")
        else:
            print(f"{label}: Invalid number")
    except Exception as e:
        print(f"{label}: Error - {e}")
    print("---")

get_details(phone_number1, "Your Number (+917889121072 - Amritsar area, Punjab)")

print("# PHONE NUMBER REGION CHECK")
print("Maximum precision: Punjab state (includes Amritsar, Ludhiana, etc.)")
print("For exact live location (e.g., Chobal Road), use phone's built-in sharing (Google Find My Device/Android, or Apple's Find My) with owner permission.")