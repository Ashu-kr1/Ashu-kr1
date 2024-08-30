for i in range(0,10):
    print(i)
    if i==5:
        break
# |i | Condition |  O/P
# |0 |  0 == 5 -> False |  O/P = 0
# |1 |  1 ==5 -> False |  O/P = 1
# |2 |  2 ==5 -> False |  O/P = 2
# |3 |  3 ==5 -> False |  O/P = 3
# |4 |  4 ==5 -> False |  O/P = 4
# |5 |  5 ==5 -> True -> break |  O/P = 5
# Not i and exit the loop

#  Break - Based on condition , exit the loop
for i in  range(0,10,1):
    print(i)

#  Break - Based on condition , exit the loop

for i in range(0,10,2):
    print(i)
    if i==6:
        print(i)
else:
    print("no output")
print("----------------")
for i in range (0,10,1):
    if i ==6 or i ==5:
        print(i)
    else:
        pass
