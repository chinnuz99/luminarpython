#define function to integrate
def f(x):
    return 1/(1+x**2)
def simpson13(x0,xn,n):
    h=(xn-x0)/n
    integration=f(x0)+f(xn)
    for i in range(1,n):
        k=x0+i*h
        if(i%2==0):
            integation=integration+2*f(k)
        else:
            integration=integration+4*f(k)
            integration=integration*h/3
            return integration
        lower_limit=float(input("enter the lower limit of integration:"))
        upper_limit=float(input("enter the upper limit of intgratioin:"))
        sub_interval=int(input("enter number of sun intervals"))
        result=simpson13(lower_limit,upper_limit,sub_interval)
        print("integration result by simpson's 1/3 method is:%0.6f"%(result))






