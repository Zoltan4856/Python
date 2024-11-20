#Napište program, který vypíše na obrazovku Fibonacciho posloupnost od hodnoty 0 do hodnoty zadané uživatelem (generace králíků)



zadane_cislo = int(input("Zadejte číslo pro Fibonacciho posloupnost: "))

a, b = 0, 1
fib_seznam = [a]

while b <= zadane_cislo:
    fib_seznam.append(b)
    a, b = b, a + b  
    
print("Fibonacciho posloupnost až do", zadane_cislo, "je:", fib_seznam)


