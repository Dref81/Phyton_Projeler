import random
yasam = 2
shot = random.randrange(1,4)
fatal_bullet = random.randrange(1,4)
print("Ateşlemek için Enter'a bas")
input()
while yasam > 0:
    if shot == fatal_bullet:
        print("Öldün")
        yasam = 0
        input()
    else:
        yasam = 1
        print("Yaşadın")
        input()