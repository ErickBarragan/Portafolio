import matplotlib.pyplot as plt
import numpy as np


# Fixing random state for reproducibility
np.random.seed(19680801)


diccionariox = { '1': 10, '2': 13, '3': 20, '4': 28, '5': 15 }

values = list(diccionariox.values())
values2 = np.array(values)


names=list(diccionariox.keys())

#plt.stem( names,values, use_line_collection=True) #names are de x values and values is y values, ESTA ES LA QUE ACTUALMENTE USAMOS
plt.plot(values)

plt.show()
