#Napište program, který „otočí“ seznam doprava o n pozic. Například, pokud n = 2, poslední 2 prvky by měly být přesunuty na začátek.



seznam = [1, 2, 3, 4, 5, 6, 7]

n = 3

n = n % len(seznam)
seznam = seznam[-n:] + seznam[:-n]

print(seznam)
