'''def print_numbers(n):
    d = {k:v}
    for i in range(n):
        for j in range(n):
            print (i,j)

print_numbers(10)'''

'''def oddeven():
    k = int(input("enter the number:  "))
    if k <= 0:
        print ("enter a valid number")
    else:
        if k%2==0:
            print (k,"is the even number")
        else:
            print (k,"is the odd number")

oddeven()'''

'''def prime_number():
    k = input("enter the number:  ")
    n = input("enter the number:  ")
    k_lst = k.split()

    for i in range(len(k_lst)):
        k_lst[i] = int(k_lst[i])
    #print (k_lst)
    #return k_lst
    for i in range(len(k_lst)):
        for j in range(i+1, len(k_lst)):
            if k_lst[i] + k_lst[j] == n:
                print (k_lst[i], k_lst[j])

prime_number()'''

'''i = 1
while i<=5:
    print(i)
    i = i+1'''
'''table = int (input("enter the table number you want: "))
for i in range(1,11):
    print (table*i)'''

'''k = (input("enter a number: "))
l = []
#print (type(k))
for i in (k):
   l.append(i)
for j in l:
    print (type(j))'''

'''a= 2
b=3
temp = a
b = a
temp = b
print (temp)'''


# word = "banana"
# letter_counts = {}

def word_count(word):
    letter_counts = {}
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts


l = word_count("hhhhhhhlllooopppp")
print(l)

# Print the dictionary
# print("Letter counts:", letter_counts)


# print ("sorry anna \n"*100)
