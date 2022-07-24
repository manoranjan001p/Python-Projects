a=0
b=1
for i in range(10):
    c=a+b
    a=b
    b=c
    print(c)
/////////////////////
    def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
fib(10)
/////////////////////
def Fibonacci(number):
           if(number == 0):
                      return 0
           elif(number == 1):
                      return 1
           else:
                      return (Fibonacci(number - 2)+ Fibonacci(number - 1))
number = int(input("Enter the Range Number: "))
for n in range(0, number):
           print(Fibonacci(n))
