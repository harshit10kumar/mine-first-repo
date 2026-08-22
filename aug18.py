'''
print('hi')
value = 10
value = 'raj'
value=12.89
print(value)
print(type(value))'''

'''a=b=c=10
print(a,b,c)'''

'''a=10
print('first assignment',a)
a=40
print('second assignment',a)
print(type(a))'''

'''a=10
print('first assignment',a)
a='raj'
print('second assignment',a)
print(type(a))'''

'''empid=101
empname='harshit'
salary=10000.00
print(' my empid is:',empid)
print(' my empname is:',empname)
print(' my salary is:',salary)
print('empid type is:',type(empid))
print('empname type is:',type(empname))
print('salary type is:',type(salary))'''
'''
a=2e2
b=2E2
c=2e3
print(a)
print(b)
print(c)
print(type(a))'''
'''
a=2+5j
b=3+6j
c=4-7j
print(a)
print(b)
print(c)
print(a+b)
print(a-b)
print(b-c)
print(c+a)
print(type(a))
'''

'''a=True
b=False
print(a)
print(b)
print(a+a)
print(a+b)'''

'''a=None
print(a)
print(type(a))'''

'''
name="hello"
s2='hi'
s3="""hi,
this is harshit
from gla"""
s4="""hi,
this is harshit"""
print(name)
print(s2)
print(s3)
print(s4)
'''

'''x=[10,20,30,40,50]
y=bytes(x)
print(y[0])
print(y[1])
print(y[2])
print(y[3])'''

'''x=[10,20,300,40,50]
y=bytes(x)
print(y[0])
print(y[1])
print(y[2])
print(y[3])'''

'''x=[10,20,30,40,50]
y=bytes(x)
y[3]=30'''

'''a=range(10)
print(a)
for i in a:
    print(i)'''

'''l1=range(5)
l2=range(2,7)
l3=range(2,10,2)
print(l1)
print(l2)
print(l3)
print(type(l1))
for harsh in l1:
    print(harsh)'''

'''a=10
b=float(a)
print(b)
print(type(b))
a=5.9
b=int(a)
print(b)
print(type(b))
a=4
b=str(a)
print(b)
print(type(b))'''

'''a=True
b=int(a)
print(b)
print(type(b))
a="100"
b=int(a)
print(b)
print(type(b))'''
'''a='harshit'
b=int(a)
print(b)'''

'''print('hello world')
a=""
a=bool(a)
print(a)
print(type(a))'''
a=None
print(a)
print(type(a))

'''s1='hello'
s2='hi'
s3="""hi,
this is harshit
from gla"""
print(s1,s2,s3)
print(s1,s3)'''
x= [10,20,30,40,50]
y=bytes(x)
print(type(y))
'''x=[10,20,30,40,50]
y=bytes(x)
print(y[0])
print(y[1])
print(y[2])
print(y[3])'''
'''x=[10,20,30,40,50]
y=bytes(x)
for i in y:
    print(i)

x=[10,20,30,40,50]
y=bytes(x)
y[0]=30'''
a=range(5)
a=''
print(bool(a)+3)
print(5+int('123'))
print('2'+str(344))
a=10
b=20   
c=(a if a<b else b)+20
print(c)
if a<b:
    if b>c:
        print ('b is greater')
    else:
        print('c is greater')
        print ('a is the smallest')
else:
    if a>c:
        print('a is greater')
    else:
        print('c is greater')    
        print('b is the smallest')        
d=a+b
print(d)
d=a-b
print(d)
d=a*b
print(d)
d=a/b
print(d)
d=a//b
print(d)
d=a%b
print(d)
d=a**b                
print(d)