import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

#estou usando np.array apenas para poder tratar as listas posteriormente
P =np.array([19.953 , 39.223 , 42.984 , 48.852 , 52.652 ,56.62, 60.614 , 
    63.998 , 67.924, 70.229 , 72.832 , 84.652])

x1=np.array([0, 0.1686, 0.2167, 0.3039, 0.3681, 0.4461, 0.5282,
    0.6044, 0.6804, 0.7255, 0.7776,1])



#como linearizar 

plt.plot(x1,P,".",label="P x X")
plt.title("P x X")
plt.xlabel("X")
plt.ylabel("Pressão")

reg = np.polyfit(x1,P,deg=1)

print("a=",reg[0],"b=",reg[1])
#ax + b = y

linear_reg= np.polyval(reg,x1)
plt.plot(x1,linear_reg)
