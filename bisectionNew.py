import math


a = 1 # a and b is the estiamted bounds between pi
b = 4

m = (math.sin(a) + math.sin(b))  / 2     #inital bisection
tol = (math.pi - math.sin(m) )/ math.pi  #pi - estimated / pi ... to iniate the loop
digit = 0.000000000000001                #number of digits for precision

while abs(tol) > digit:                 #loop through until our estimated digits are less than our desired
    m = (math.sin(a) + math.sin(b)) / 2  #bisection
    if math.sin(a) * math.sin(m) < 0 :   #picks which side the root lies on
        b = m
    else:
        a = m
    pi_test = math.pi - math.sin(m)     # pi - estimated
    print("sin(m)", math.sin(m))
    tol = (math.pi - pi_test) / 2
    #print("A = ", a)
    #print("B = ", b)
    print("estimated value: ",pi_test)
    #print("tolerance: ", tol)

print("true pi: ",math.pi)
print("Pi to 15 digits: ", pi_test )
