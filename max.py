number = []
max=0
try:
    for i in number:
        if max < i:
            max=i
    print("Le max est:",max)
except:
    print("liste vide")