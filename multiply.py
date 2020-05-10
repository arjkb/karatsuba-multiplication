from termcolor import colored

def recursiveMultiply(x, y):
    print("recursiveMultiply({}, {})".format(x, y))
    xs, ys = str(x), str(y)
    nx = len(xs)
    ny = len(ys)
    # print("(nx, ny) = ({}, {})".format(nx, ny))

    # for starters just deal with the situation where nx == ny, and they're both a power of 2

    # base case (digits length is 1)
    if nx == 1 or ny == 1:
        print("Base case product:", int(x) * int(y))
        return int(x) * int(y)

    # recursive case:

    # compute A, B, C, D
    xh, xg = int((nx//2)), int(nx - (nx//2)) # the power of 10 to which the digit-group must be separated by
    yh, yg = int(ny//2), int(ny - ny//2) # (same as above)
    # print("(xh, xg) = ({}, {})".format(xh, xg))
    # print("(yh, yg) = ({}, {})".format(yh, yg))
    
    # a = int(xs[:xh])
    # b = int(xs[xh:])
    # c = int(ys[:yh])
    # d = int(ys[yh:])

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

    result = recursiveMultiply(int(num1), int(num2))
    print("Product:", result)


if __name__ == "__main__":
    main()