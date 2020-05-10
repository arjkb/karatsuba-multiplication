from termcolor import colored

def recursiveMultiply(x, y):
    print("recursiveMultiply({}, {})".format(x, y))
    # pad = len(str(x)) - len(str(y))
    xs, ys = str(x), str(y)

    # padding... because this whole thing works iff length of both numbers are the same
    # So, if we store the length as max of the available two lengths,
    # then further down the line when we split the numbers
    # the math automatically works out
    nx = max(len(xs), len(ys))
    ny = max(len(xs), len(ys))
    # print("(nx, ny) = ({}, {})".format(nx, ny))

    # base case (digits length is 1)
    if nx == 1 or ny == 1:
        print("Base case product:", int(x) * int(y))
        return int(x) * int(y)

    # recursive case:
    xh, xg = int((nx//2)), int(nx - (nx//2)) # the power of 10 to which the digit-group must be separated by
    yh, yg = int(ny//2), int(ny - (ny//2)) # (same as above)

    # compute A, B, C, D
    a = x//(10**xh)
    b = x % (10**xh)
    c = y//(10**yh)
    d = y % (10**yh)

    ac = recursiveMultiply(a, c)
    bd = recursiveMultiply(b, d)
    a_b__c_d = recursiveMultiply(a + b, c + d)
    ad_plus_bc = a_b__c_d - ac - bd     # Gauss' Trick

    print("a={}, b={}, c={}, d={}".format(a, b, c, d))
    print("ac\t\t= {}\nbd\t\t= {}\n(a+b)*(c+d)\t= {}\n(ad+bc)\t\t= {}".format(ac, bd, a_b__c_d, ad_plus_bc))
    print("nx={}, xh={}".format(nx, xh))
    # product = (10**nx)*ac + (10**xh)*(ad_plus_bc) + bd
    product = (10**(xh+yh))*ac + (10**xh)*(ad_plus_bc) + bd
    attrs = [] if ((product - (x*y)) != 0) else []
    color = 'red' if ((product - (x*y)) != 0) else 'green'
    # print((product - (x*y)), attrs)
    print(colored("Product of {} * {} = {}; Act={}, Error={}".format(x, y, product, x * y, product - (x*y)), color, attrs=attrs))
    return product

def main():
    num1 = input().strip()
    num2 = input().strip()
    print("{} {}".format(num1, num2))

    print("Product:", recursiveMultiply(int(num1), int(num2)))

if __name__ == "__main__":
    main()