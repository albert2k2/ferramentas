"""
Spyder Editor
adaptado de https://www.codesansar.com/numerical-methods/secant-method-python-program.htm

"""

import math
import numpy as np

# aqui vamos definir a  função alvo
def f(x1):
    
    
    fx=np.exp(9.24-(712)/(x1))*0.8+np.exp(8.99-(809)/(x1))*0.2-1
    
    return fx

    #x1 é T em Kelvin (K)

def secante(x0,x1,tol,IT):
    # definindo x0 = chute o / x1 = chute 1 
    # f(x) é a função de interesse designada anteriormente
    # tol como a tolerância experada
    
    n=1 
    condição= True
    while condição:
        if f(x0) == f(x1):
            print("divisão por zero, indefinição")
            break
        
        x2 = x1 - (x1-x0)*f(x1)/(f(x1)-f(x0))
        
        print("iteração-%d, x2= %0.6f e f(x2))= %0.6f" % (n, x2, f(x2)))
        
        x0=x1
        x1=x2
        n+=1
        
        if n >IT:
            print ("não converge")
            break
        
        condição = abs(f(x2)) > tol
    
    print ("\n A raiz é : %0.8f" %x2)

    

# entrada de valores e chutes iniciais
x0=100
x1=60
tol=0.0001
IT=10     # número inteirio pfr

#chamando a função 

secante(x0, x1, tol, IT)
