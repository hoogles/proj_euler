from scipy.optimize import fsolve

def ispyth(x,y):
    a = x[0]
    b= x[1]
    c = (a*a+b*b)**0.5
    pyth_err = abs(a*a+b*b-c*c)
    sum_err = abs(a+b+c-y)
    return [pyth_err,sum_err]
def ispyth1000(x):
    return ispyth(x,1000)
    
x0 = [3,4]
z = fsolve(ispyth1000,x0)
z.append(z[0]**2+z[1]**2)
print(z)
