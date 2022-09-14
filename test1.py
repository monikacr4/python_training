a = input('enter name: ')
#print(len(a))
for names in {a}:
    if len(names)<1:
        print('enter name')
    if names.isalpha()== False:
        print(f'its compulsory to enter name with alphabets only {names} is invalid')
        name = input('enter name: ')
        
phone=input("Enter phone Number : ")
while len(phone)!=10 or phone.isnumeric()==False:
    phone=input("Enter Valid Telephone Number : ")

c = input('age: ')
while c.isnumeric()==False or int(c)<20 :
    c=(input('enter age: '))   

d = input('email: ')
if len(d)<=5:
    print('invalid')
    input('enter a email: ')

e = input('address: ')

s = input('salary: ')
while(len(s)==0 or s.isnumeric() == False or int(s)<0):
     input('enter salary:')

dept=input("Enter Your Department: ")
while len(dept)==0 or dept.isalpha()==False:
    input('enter department:')

print('details you entered')
print('name: ',name)
print(f'phone: {phone}')
print('age: ',c)
print('email: ',d)
print('address: ',e)
print('salary: ',s)
print('department: ',dept)
