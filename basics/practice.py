# number = input("enter value: ")
table = {}
def tables(number):
    for i in range(1,11):
        # number = input("enter value: ")
        table[i] = int(number) * i
    for k,v in table.items():
        # return (f"{number}*{k}={v}")
        print(f"{number}*{k}={v}")

tables(5)
# for k,v in table.items():
#     print (f"{number}*{k}={v}")