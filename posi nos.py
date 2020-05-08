x = int(input("Enter the num: "))
y = int(input("Enter the num: "))
z = int(input("Enter the num: "))
i = int(input("Enter the num: "))
k = int(input("Enter the num: "))
  

list1=[x,y,z,i,k]
list_1= list(filter(lambda l : l>=0, list1))
print(list_1)
