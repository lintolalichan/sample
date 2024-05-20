a=int(input('enter first num:'))
b=int(input('enter the second num:'))
print('1:addition')
print('2:multiplication')
print('3:substraction')
print('4:division')

choice=int(input('enter your choice'))

def add():
 print(a+b)

def mul():
 print(a*b)

def sub():
 print(a-b)

def divi():
 print(a/b)

while choice!=0:
 if choice==1:
    add()
 elif choice==2:
    mul()
 elif choice==3:
    sub()
 elif choice==4:
    divi()
 break
