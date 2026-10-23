s= []

n = int(input("Enter how many numbers in list: "))

for i in range(n):
    a = int(input("Enter number: "))
    s.append(a)

key = int(input("Enter element to search: "))

found = False

for i in range(n):
    if a[i]==key:
        found=True
        print("It is Found:",i)
        break
if found==False:
    print("It is not Found")
