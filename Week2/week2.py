print("Hello, World")
print(2 ** 88)
print((1+2j)*(3*4j))
#Single line comments begin with a hash symbol
"""
Multi line commments are like this
"""
x=[1,
   2,
    4,
     5]
print(x)

def main():
    print(sum1ton(100))

def sum1ton(n):
    sum=0
    i=0
    while i<=n:
        sum=sum+i
        i=i+1
    return sum

main()
# we can use del x to delete the variabe x
"""
Python provides many built-in functions for numbers, including: 
 Mathematical functions: round(), pow(), abs(). 
 Type conversion functions: int(), float(), str(), bool(); and type() to get the type. 
 Base radix conversion functions: hex(), bin(), oct(). 
"""
