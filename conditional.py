'''#if
print('enter a number')
a = int(input())

print('marks is')
if a<40:
    print('fail')
elif a>=40 and a<70:
    print('average')
else:
    print('good')
print('thank you')

if a<40:
    x ='fail'
elif a>40 and a<70:
    x ='average'
else:
    x = 'good'
print('marks is ',a,x)


if a<40:
    x ='fail'
elif a>=40 and a<70:
    if a==40:
       x='just pass'
    if a >40:
        x ='average'
else:
    x = 'good'
print('marks is ',a,x)


print('enter first number: ')
m = input()
print('enter second number: ')
n = input()
print('enter third number: ')
o = input()

if m>n and n>o:
    print('m is greater. The value is:',m)
elif n>m and n>o:
    print('n is greater. The value is:',n)
elif o>n and n>m:
    print('o is greater. The value is:',o)
else:
    print('all are equal. the value is',m)


totalclass=200
print('enter number of classes attended:')
a = int(input())
p = (a*100)/totalclass
print(p)
if p<40:
    print('not allowed to write exam')
else:
    print('eligible to write exam')
'''

print('enter salary')
salary = int(input())
print('enter number of years working in company')
years=int(input())
if years>=10:
    bonus = (15*salary)/100
    final = salary+ bonus
    print(final)
elif years>=5 and years<10:
    bonus = (10*salary)/100
    final = salary+ bonus
    print(final)
elif years>=3 and years<5:
    bonus = (5*salary)/100
    final = salary+ bonus
    print(final)
else:
    print('not eligible')
