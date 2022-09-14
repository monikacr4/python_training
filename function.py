'''def func(par1,par2)
     #body
     #return
    
def message():
    print(f'this is first function')
message()

def message(name,usn):
    print(f'name is {name} and usn is {usn}')
message('monika','1rv18ee030')

def hra(salary):
    hra = round(salary*40/100)
    #print(hra)
    return hra
s = hra(75000)
print(s) 
'''    
# if return is not declared inside function, we cant use other variable to print that answer
def number(n):
    if n%2 == 0:
        print('its even')
    else:
        print('this is odd')
number(20)

# randint: validate number randomly between 2 specific numbers
print(number.__doc__)