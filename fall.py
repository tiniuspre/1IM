import numpy as np

f = open("info.txt", "r")
xy = (f.readline())

def les():
    f = open("info.txt", "r")
    xy = int(f.readline())

def fart():
    var0 = int(input("Start Fart (m/s): "))
    var1 = int(input("Fall tid (sek): "))
    arr = np.array([(var0), (var1), float(xy)])  # ( [0] = Start Vo ) ( [1] = Fall tid ) ( [2] Tyngdekraft )
    svar = ((arr[0]) + (arr[1]) * (arr[2]))
    print(svar)
    print("m/s")


def hoyde():
    var0 = float(input("Høyde (meter): "))
    arr = np.array([(var0), float(xy)])   # ( [0] = høyde i meter ) ( [1] = gravitasjon )
    svar = ((arr[0]) / (arr[1]) / 2)
    print(svar)
    print("sekunder")


def fil(varia):
    grav = np.array([1.62, 9.80665])  # [0] = Månen [1] = Jorda [2] =
    f = open("info.txt", "w")
    f.write(str(grav[int(varia)]))
    f.close()


def settings():
    sett = input("Endre gravitasjon (flere valg) 1\n: ")
    if sett == "1":
        a = input("Sett tyngdekraft til: \n Månen (1)\nJorda (2)\n: ")
        if a == "1":
            fil(0)
        elif a == "2":
            fil(1)
        else:
            print("ERROR")
    else:
        print("Restart")


x = input("Høyde (1) \nFart (2) \nOppset (3)\ntest (4)\n : ")
if x == "1":
    hoyde()
elif x == "2":
    fart()
elif x == "3":
    settings()
elif x == "4":
    les()
else:
    print("ERROR")