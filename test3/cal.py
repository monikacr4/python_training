fname = input('enter first name: ')
lname = input('enter last name: ')
print("enter salary: ")
salary = int(input())
    
def basic():
    basic = 50*salary/100
    return basic

def hra():
    hra = 40*salary/100
    return hra

def compensation():
    compensation = 10*salary/100
    return compensation

