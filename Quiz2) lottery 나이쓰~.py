c = int(input("학생수를 입력해주세요.: "))
a = range(1,c+1)
stulist = list(a)

import random

chick = random.choice(stulist)

stulist.remove(chick)


time = 0
coflist = []
while time < 3:
    cof =random.choice(stulist)
    coflist.append(cof)
    time = time + 1
    stulist.remove(cof)

print("=== Winner Announcement===")
print("chicken winner :",chick)
print("coffee winner :",coflist[0],coflist[1],coflist[2])
print("===Congratulation==\n\n")

print("{0:=^30}".format("winner announcement"))
print("{0:=^30}".format("chicken winner :{}".format(chick)))
print("{0:=^30}".format("coffee winner :{}".format(coflist)))
print("{0:=^30}".format("Congratulation !!"))
