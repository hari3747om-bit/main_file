Number = (input('Enter your number'))
digit = [int(d) for d in str(Number)]
dict1 = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 0: "Zero"}
for d in digit:
    print(dict1[d], end=" ")