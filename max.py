number = [12,24,89,33,60,14,73,99]
max=0
try:
    for i in number:
        if max < i:
            max=i

    print("Le max est:",max)
except():
    print("liste vide")
    print("hello")