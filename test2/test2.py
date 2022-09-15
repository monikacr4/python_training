import mariadb
import sys
conn = mariadb.connect(
    user = 'root',
    password = '@Mahalakshmi1',
    host = 'localhost',
    port = 3306,
    database='test2'
    )
cur = conn.cursor()
conn.autocommit=True
try:
    cur.execute('CREATE TABLE information1(name VARCHAR(30),phone INTEGER,age INTEGER,email VARCHAR(255),address VARCHAR(255),salary INTEGER,dept VARCHAR(255))')
except Exception as y:
    print(y)
name=input("name: ")
for names in {name}:
    if len(names)<1:
        print('enter name')
    if names.isalpha()== False:
        print(f'its compulsory to enter name with alphabets only {names} is invalid')
        name = input('enter name: ')
phone = input("phone:" )
while len(phone)!=10 or phone.isnumeric()==False:
    phone=input("Enter Valid Telephone Number : ")
age =input('age: ')
while age.isnumeric()==False or int(age)<20 :
    age=(input('enter age: ')) 
email = input('email: ')
if len(email)<=5:
    print('invalid')
    input('enter a email: ')
address =input('address: ')

salary =input('salary: ')
while(len(salary)==0 or salary.isnumeric() == False or int(salary)<0):
    input('enter salary:')
dept = input('department: ')
while len(dept)==0 or dept.isalpha()==False:
    input('enter department:')

a="INSERT INTO information1(name,phone,age,email,address,salary,dept) VALUES (%s,%d,%d,%s,%s,%d,%s)"
b=(name, int(phone), int(age),email,address,int(salary),dept)
cur.execute(a,b)
cur.execute('SELECT name,phone,age,email,address,salary,dept FROM information1')

for (name,phone,age,email,address,salary,dept) in cur:
    print('Name',{name},'phone',{phone},'Age',{age},'email',{email},'address',{address},'salary',{salary},'dept',{dept})