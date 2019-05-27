import numpy as np
import matplotlib.pyplot as plt

x, y = np.loadtxt('t_busqueda_ale', unpack=True)

plt.plot(x,y, 'ro-', label="t=f(n)")
plt.legend()
plt.title("tamaño conjunto v/s buscar 10 elem. aleatorios")
plt.ylabel("tiempo (s)")
plt.xlabel("n")
plt.grid()
plt.savefig("n_10rdsearch.png")
plt.show()
