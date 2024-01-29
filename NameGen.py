# Coded By Topher
# Use This However You Want :p
import random # This imports random to generate random shit

def generate_random_name():
    # First name = first
    first = ["Luke", "Lucas", "David", "John", "Henry", "Liam", "Noah", "Jack", "Jackson", "Elijah", "Oliver", "James", "William", "Jonathon", "Amelia", "Ava", "Lisa", "Rebecca", "Emily", "Charlotte", "Chloe", "Emma", "Evelyn", "Gemma", "Isla", "Lily", "Ella", "Mia", "Jane", "Scarlett", "Jordan"]
    last = ["Johnson", "Smith", "Jones", "Tucker", "Williams", "Davis", "Smith", "Miller", "Brown", "Anderson", "Jackson", "Garcia", "Smith", "Moore", "Robinson", "Thomas", "Taylor", "Kelly", "Rebeccas", "Luff", "Kirkby", "Jenkins"]
    
    # Shit to make it work
    name1 = random.choice(first)
    name2 = random.choice(last)
    return name1, name2

# Generate the random name
random_name1, random_name2 = generate_random_name()

# Print the result
print("Here's A Random Name:", random_name1, random_name2)
# Why do you need random names? Just find one online but ok
# We'll do coding lessons sometime idk