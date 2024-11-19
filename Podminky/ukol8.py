#Napište program, který zjistí, zda zadané heslo uživatelem je silné. 
#heslo musí mít alespoň jedno velké písmeno, jedno malé písmeno, jednu číslici, 
#jeden speciální znak a minimální délka musí být alespoň 8 znaků.

password = input("Zadejte heslo: ")

# Inicializace proměnných pro kontrolu podmínek
has_upper = False
has_lower = False
has_digit = False
has_special = False

# Smyčka pro procházení každého znaku v hesle
for char in password:
    if char.isupper():  # Velké písmeno
        has_upper = True
    elif char.islower():  # Malé písmeno
        has_lower = True
    elif char.isdigit():  # Číslice
        has_digit = True
    elif char in '@$!%*?&':  # Speciální znak
        has_special = True

# Ověření všech podmínek
if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Heslo je silné.")
else:
    print("Heslo není silné.")
