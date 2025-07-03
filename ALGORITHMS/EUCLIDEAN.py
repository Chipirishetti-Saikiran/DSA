#GCD of Two Numbers - Euclidean Algo

# This algorithm is a metod for efficiently calculating the gcd of two integers.

#a=15 => 1,3,5,15 
#b=50 => 1,2,5,10,25,50

def gcd(a,b):
    if b==0:
        return a 
    return gcd(b,a%b)
print(gcd(15,50))


def lcm(a,b):
    return (a*b)//gcd(a,b)

print(lcm(15,50))

#LCM(a,b)==(a*b)/GCD(a,b)

    #a*b== lcm(a,b)*gcd(a,b)