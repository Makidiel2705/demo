a = -3.0
b = -2.0
sai_so = 0.0001
i = 0
x = 100
xtemp = 0.0
while abs(xtemp - x) > sai_so:
    fa = a**3 + 3*a**2 - 1
    fb = b**3 + 3*b**2 - 1
    xtemp = x;
    x = b - ((fb*(b-a))/(fb-fa))
    fx = x**3 + 3*x**2 - 1
    if fa*fx > 0:
        a = x
    else:
        b = x
        i += 1
    print("Vong lap {}: x = {}, f(x) = {}".format(i, x, fx))
print("Vi", xtemp, "-", x, "=", xtemp - x, "<", sai_so, ",nen nghiem cua PT la", x)
