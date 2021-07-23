import random

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
fhand = open('20210722.txt')
for i in fhand:
    i = i.strip()
    a = 0
    while a < len(i):
        b = alphabet[random.randint(0,25)]
        print(f'{i[a:a+1]}{b}',end='')
        a += 1
        if a == len(i)-1:
            print(f'{i[a:a+1]}')
            break
    

