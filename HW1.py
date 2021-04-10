#-----------1. ÖDEV-------------
mylist = [5, 10, 15, 20, 35, 40, 45, 50]

x = len(mylist)
print(x)

mylist2 = mylist[int(x/2):]
mylist3 = mylist[:int(x/2)]
print(mylist2 + mylist3)


#-----------2. ÖDEV-------------
n = int(input("Tek Basamaklı Bir Sayı Girin : "))
for i in range (0,n+1,2):
    print(i)