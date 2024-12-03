number = input("enter value: ")
table = {}
for i in range(1,11):
    # number = input("enter value: ")
    table[i] = int(number) * i
for k,v in table.items():
    print (f"{number}*{k}={v}")