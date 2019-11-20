#2
"""
print("podaj najpierw dzielnik"" ", "d")
d = float(input())
n = float(input())

if d==0:
    print(False)
elif   n>d and n%d==0:
    print(True)
else:
    print(False)

"""

#4
"""
n=int(input())
w=0
while n>0:
    w=w+(n%10)
    n=n//10
    
print(w)
"""
#5######################
"""
n=int(input())
s = 1
for i in range(1,n):   
    if i<=n:
         s =s*(i+1)
    if i>=n:
         s=s
print(s)
"""
#5 reku nwm czemu nie działa
"""
#s == s*(i+1)
n=int(input())
s = 1
def rek2(y):
 for i in range(1,n):
    while i<=n:
        s = 1*(i+1)
     
print(s)
"""
#6
"""    
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
x = int(input())
print (fib(x))
"""



#8
"""
n = int(input())
x = int(input())
def reku (y):
    if n==0:
        return n == 0
    if x==0:
        return x == 1
    if n!=0 and x!=0:
        return n,x

print(n**x)

"""
#10
"""
n = int(input())
s = 0
if n%2==0:
    s = 1
else:
    s = 2
if s==1:
    print(n*3)
if s==2:
    print(n*0.4)
"""        
#10.2
"""
n = int(input())
s = 0
def f(y):
    if n%2==0:
        return globals(s=n)
    if s==n:
        return print(n*3)
    if s!=n:
        return print(n*0.4)
""" 

# funkcja global,globals() sluży do zadania globalnej wartosci argumentowi
# w obrębie calego kodu. 


