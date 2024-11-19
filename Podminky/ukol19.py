#Armstrongovo číslo (nebo také narcistické číslo) je číslo, které je rovno součtu svých vlastních číslic umocněných na počet číslic v tomto čísle. Například 153 je Armstrongovo číslo, protože:

#153 = 1^3 + 5^3 + 3^3

#Napište program, který zjistí, zda je dané číslo Armstrongovo číslo.


vstup = int(input("Zadejte číslo: "))

# Extract digits
a = vstup // 100  # First digit (hundreds)
b = (vstup // 10) % 10  # Second digit (tens)
c = vstup % 10  # Third digit (ones)

# Check if it's an Armstrong number (sum of cubes of digits)
if (a**3 + b**3 + c**3) == vstup:
    print(f"{vstup} je Armstrongovo číslo.")
elif (a**3 + b**3 + c**3) != vstup:
    print(f"{vstup} není Armstrongovo číslo.")
