import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

# estou usando np.array apenas para poder tratar as listas posteriormente
P =np.array([19.953 , 39.223 , 42.984 , 48.852 , 52.652 ,56.62, 60.614 , 
    63.998 , 67.924, 70.229 , 72.832 , 84.652])

x1=np.array([0, 0.1686, 0.2167, 0.3039, 0.3681, 0.4461, 0.5282,
    0.6044, 0.6804, 0.7255, 0.7776,1])

y1=np.array([0, 0.5714, 0.6268, 0.6943, 0.7345, 0.7742, 0.8085, 0.8383,
    0.8733, 0.8922, 0.9141,1])

# o tamanho das listas com base no P dado 
w=len(P)

#para a Pressões de saturação em 333.15K (Valores em KPa)

Psat1=84.562
Psat2=19.953
 

#plottando Pxy
plt.plot(x1,P,".",label="P-x")
# se quiser plottar com linha basta colocar marker="." NO LUGAR DE APENAS "."
plt.plot(y1,P,"x",label="P-y")
plt.xlabel("X1 & Y1")
plt.ylabel("P(KPa)")
plt.title("relação pressão x fração de metanol")
plt.legend()
