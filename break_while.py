import random

h1=40
h2=50
h3=60

while h1 > 0:
    dmg = random.randrange(h2, h3)
    h1= dmg-h1
    print(dmg , "new h1", h1)

    if h1 < 10:
        pass

        print("low value")
        break

    if h1<=0:
        h1=0

    if h1==0:
        print("h1 is zero")

