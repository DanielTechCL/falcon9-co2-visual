import matplotlib.pyplot as plt

x = ['10 km', '20 km', '30 km', '40 km', '50 km', '60 km', '70 km', '80 km', '90 km', '100 km']
y = [225.0, 225.0, 225.0, 225.0, 225.0, 225.0, 225.0, 112.3, 112.3, 112.3]

plt.plot(x, y)

plt.title('Dióxido de carbono del Falcon 9: CO2 por tramo de 10 km',
          fontsize=13)

plt.xlabel('Distancia recorrida (km)',
           fontsize=12)

plt.ylabel('CO2 generado (toneladas)',
            fontsize=12)

plt.show()