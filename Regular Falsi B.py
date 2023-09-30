import math
a = 0
b = math.pi/2
sai_so = 0.0001
i = 0
x = 100
xtemp = 0.0
while abs(xtemp - x) > sai_so:
    fa = a - 0.8 - 0.2*math.sin(a);
    fb = b - 0.8 -0.2*math.sin(b);
    xtemp = x;
    x = b - ((fb*(b-a))/(fb-fa))
    fx = x- 0.8 - 0.2*math.sin(x)
    if fa*fx > 0:
        a = x
    else:
        b = x
        i += 1
    i+=1
    print("Vong lap {}: x = {}, f(x) = {}".format(i, x, fx))
print("Vi", xtemp, "-", x, "=", xtemp - x, "<", sai_so, ",nen nghiem cua PT la", x)