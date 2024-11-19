#Napište program, do kterého zadáte datum vašeho narození. Program se podívá na dnešní datum pomocí knihovny datetime a vypíše, kolik zbývá dnu do vašich narozenin. 
# Pokud máte narozeniny dnes, tak vám navíc ještě pogratuluje. 
from datetime import datetime, date

# Step 1: Input your birthdate
birthdate_str = input("Zadejte datum narození (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()  # Convert to date object

# Step 2: Get today's date
today = date.today()

# Step 3: Check if today is the birthday
if today.month == birthdate.month and today.day == birthdate.day:
    print("Šťastné a veselé narozeniny!")
else:
    # Step 4: Calculate the next birthday
    # If the birthday has already passed this year, use the next year
    if today > birthdate.replace(year=today.year):
        next_birthday = birthdate.replace(year=today.year + 1)
    else:
        next_birthday = birthdate.replace(year=today.year)

    # Step 5: Calculate the difference in days
    days_left = (next_birthday - today).days
    print(f"Zbývá {days_left} dnů do vašich narozenin.")

