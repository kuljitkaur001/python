import random
import string

# Generate one random lowercase letter
lower = random.choice(string.ascii_lowercase)
print("Random lowercase letter:", lower)

# Generate one random uppercase letter
upper = random.choice(string.ascii_uppercase)
print("Random uppercase letter:", upper)

# Generate one random digit
digit = random.choice(string.digits)
print("Random digit:", digit)

# Generate one random special character
special = random.choice(string.punctuation)
print("Random special character:", special)
