import pandas as pd

import matplotlib.pyplot as plt   # toca hacer pip install matplotlib

archivo = "PANDAS\jcumulacion.xlsx" 
excel_file = "PANDAS\GDB_FAUNA.xlsx"
          
hoja = "Hoja1"

documento = pd.read_excel(archivo, sheet_name= hoja)
#titulos = documento.head(0)
#propiedades = documento.info()

tabla = pd.read_excel(archivo, sheet_name= hoja, index_col=0, parse_dates=True)
'''
tabla.plot() # Grafica todos los valores numericos de la tabla
info_graf = tabla["Jack 2 Mean"].plot() #con esto se grafica solo esa serie
'''


#https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html

#compara dos series
tabla.plot.scatter(x="Doubletons Mean", y="Uniques Mean", alpha = 0.5)

plt.show()





