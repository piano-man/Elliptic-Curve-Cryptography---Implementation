from collections import namedtuple
import matplotlib.pyplot as plt
from sympy.ntheory import sqrt_mod

Point = namedtuple("Point", "x y")

O = 'Origin'

a = 2
b = 2

def valid(P):
    # print((P.y**2)%p)
    # print((P.x**3 + a*P.x + b) % p)                  
    if P == O:
        return True
    else:
        return (
            (P.y**2 - (P.x**3 + a*P.x + b)) % p == 0 and
            0 <= P.x < p and 0 <= P.y < p)

def inv_mod_p(x):
    if x % p == 0:
        raise ZeroDivisionError("Impossible inverse")
    return pow(x, p-2, p)

def ec_inv(P):
    if P == O:
        return P
    return Point(P.x, (-P.y)%p)

def ec_add(P, Q):
    if not (valid(P) and valid(Q)):
        raise ValueError("Invalid inputs")
    if P == O:
        result = Q
    elif Q == O:
        result = P
    elif Q == ec_inv(P):
        result = O
    else:
        if P == Q:
            dydx = ((3 * P.x**2 + a) * inv_mod_p(2 * P.y)) % p
        else:
            dydx = ((Q.y - P.y) * inv_mod_p(Q.x - P.x)) % p
        x = (dydx**2 - P.x - Q.x) % p
        y = (dydx * (P.x - x) - P.y) % p
        result = Point(x, y)
    assert valid(result)
    return result

def test_singularity():
    if 4*a**3+27*b**2!=0:
        print("the curve is non-singulat")
    else:
        print("the curve is singular and should not be used")

def plot_curve(p,a,b):
    x= []
    y = []
    y_neg = []
    for i in range(-1000,1000):
        j = i**3 + a*i + b
        x.append(i)
        y.append(j)
        y_neg.append(-1*j)
    plt.plot(x,y)
    plt.plot(x,y_neg)
    plt.show()

def curve_under_field(p,a,b):
    for i in range(1000):
        if i in range(0,p):
            j = i**3 + a*i + b
            j_final = sqrt_mod(j,p,True)
            # print(j_final)
            if j_final==None:
                continue
            else:
                if type(j_final)==list and len(j_final) > 1:
                    # print(j_final[0])
                    # print(j_final[1])
                    x_field.append(i)
                    x_field.append(i)
                    # print("Modulus :-",j%p,(j_final[0]**2)%p,(j_final[1]**2)%p)
                    y_field.append(j_final[0])
                    y_field.append(j_final[1])
            # plt.scatter(i,j)
    # plt.show()

def find_order(P):
    order = 0
    P_inv = ec_inv(P)
    # print(P)
    # print(P_inv)
    temp = P
    while (temp.x!=P_inv.x) or (temp.y!=P_inv.y):
        order = order+1
        temp = ec_add(temp , P)
        print(temp)
    return order+2

p = 17
plot_curve(p,a,b)
x_field = []
y_field = []
curve_under_field(p,a,b)

# P = Point(x_field[2],y_field[2])
P = Point(x=5,y=1)
print(P)
print(valid(P))
print(find_order(P))
# print(ec_inv(P))
