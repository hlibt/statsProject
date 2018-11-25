import math
import scipy
import scipy.misc

a = 20
b = 500
sum = 0
up_lim = int(T/a  +1)
T = 365 * 24
for n in range(1, up_lim):
    if (T - n * a)/(b-a) >= n:
        sum += 1
        continue
    if (T - n * a) < 0:
        break
    for k in range(math.floor((T - n * a)/(b-a))+1):
        #print(sum)
        sum = sum + (-1)**k /(scipy.special.factorial(n)) * scipy.special.comb(n,k) * ((T - n * a)/(b-a) - k)**(n)
print("Sum = %s" % sum)
