import pandas as pd

import matplotlib.pyplot as plt   # toca hacer pip install matplotlib

archivo = "PANDAS\Ccumulacion.xlsx" 
          
hoja = "Hoja1"

documento = pd.read_excel(archivo, sheet_name= hoja)
#titulos = documento.head(0)
#propiedades = documento.info()

tabla = pd.read_excel(archivo, sheet_name= hoja, index_col=0, parse_dates=True)
info_graf = tabla["Jack 2 Mean"].plot() #con esto se grafica


plt.show()





