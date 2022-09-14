def func1(n):
    print(f'language {n}')
func1('python')

a=10
def func2(n):
    #a = 20
    global a #changing global variable inside function
    a= a+40
    print(a)
    print(f'this is number {n}')
func2('30')
print(a)