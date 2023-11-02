import pandas as pd

datos = pd.DataFrame(
    {
        "ID":["trebol","roble","totumo"],
        "color":["green", "blue", "red" ],
        "size":[33, 21, 17]
    }
)  
'''
'''
#print(f"Todo el dataFrame {datos} y la serie color {datos['color']}")
talla = datos["size"]

print(talla.describe())

