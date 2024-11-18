#Task: Ask the user for hours and minutes. Convert and print the total time in minutes.

hodnota1 = int(input("zadejte hodiny"))
hodnota2 = int(input("zadejte minuty"))

hodiny = hodnota1
minuty = hodnota2

minuty_kvypoctu = 60
prevod = hodiny*minuty_kvypoctu+minuty

print(f"soucet {hodiny} hodin a {minuty} minut je {prevod} minut")
