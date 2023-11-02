import pandas as pd

excel_file = "PANDAS\GDB_FAUNA.xlsx"  # La direccion debe incluir la carpeta aunque este en la misma del .py
nombre_hoja = "Registros"

documento = pd.read_excel(excel_file, sheet_name= nombre_hoja) #crea un dataframe , lee el doc

# ***     A todo el data frame

# solo muestra los emcabezados de las series (columnas), si se coloca cero
documento_encabezados = documento.head(0) 
'''
hace un resumen con tipo de datos del dataframe y obj nulos de cada serie
devuelve: la cantidad de entradas = fila de datos
columnas: cantidad de columnas
'''
'''documento_info = documento.info()''' # toco comentar, se imprime solo

# ***     A una serie o columna

abundancia = documento["ABUND_ABS"] #se puede escoger una serie (columna)
abundacia_esp = documento[["ESPECIE", "ABUND_ABS"]] # o varias series, las llaves internas indican lista

# este metodo <describe()> hace resumen de lo principal , en round() pq da muchos decimales
abundancia_aspectos = round(abundancia.describe(), 2) 

# ***     filtrar de un dataframe

abundantes = documento ["ABUND_ABS"] > 10 # retorna lista con booleans

abundantes_2 = documento[documento["ABUND_ABS"] > 10] # retorna unicamente lista que cumple con la condicion

xx = abundantes.shape

f_Tyrannidae = documento[documento["FAMILIA"].isin(["Tyrannidae"])] #retorna unicamente los miembros de la familia solicitada

f_TyrannYFalcon = documento[documento["FAMILIA"].isin(["Tyrannidae", "Falconidae"])]

f_TyrannYFalcon = documento[documento["FAMILIA"].isin(["Tyrannidae"]) | documento["FAMILIA"].isin(["Falconidae"])] #lo mismo de arriba "o"

familyabund = documento[documento["FAMILIA"].isin(["Tyrannidae"]) & documento["ABUND_ABS"].isin([2, 3])] #tiranides con 2 y 3

#devuelve las especies que cumplen la condicione de abundancia
avesAbundantes = documento.loc[documento["ABUND_ABS"] >= 10, "ESPECIE"]

selec_column = documento.iloc[0:5, 0:5] #devuelve filas y columnas por numero


print(selec_column)



