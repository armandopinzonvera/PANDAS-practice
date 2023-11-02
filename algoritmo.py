
#0. Instalacion de software propio
'''
- instalar past y Stimate

'''
#1. Recibir el archivo de excel - formato .xlsx

'''
   (VENTANA DE INICIO)
   a- Recibir archivo mediante carga o arrastre y suelte
   b- verficar formato
      verificar que estan las worksheets requeridas con sus nombres segun estandar
      (condicional) True > Mensaje: "archivo adecuado"
                            Animacion: "icono de progreso"
                            >> (VENTANA DE MENU) >> (PASO 2)    
                    False> Mensaje: "archivo rechazado"
                           Mensaje: "razones rechazo e indicaciones para arreglo"
'''

#2. Definir tipo de procesamiento

'''
   (VENTANA DE MENU) - CHECK LIST
   a- botones: 
        - todo 
            (condicional) True > selecciona todo las otras opciones
        - Muestreo 
            (condicional) True > Animacion: "icono de progreso"
                                 {<Proceso>} crea tabla : listado de puntos [tipo (punto - transecto), ID, Cobertura, fecha, coordenadas, longitud(trans)]
                                 (VENTANA DE RESULTADO) >> (PASO 3) 
                                 
        - Suficiencia muestreo
            (condicional) True > Animacion: "icono de progreso"
                                 {<Proceso>} crea tabla : listado de puntos
            
        - Registro 
            (condicional) True > Animacion: "icono de progreso"
                                 {<Proceso>} crea 1 worksheets por cada clase con ecologia: 
                                   tabla columnas [Orden, Familia, genero, spc, n_c, coberturas registro, densidad, gremio trof. distri alt, migracion, endemismo, uso ]
                                   grafico - torta: riqueza de ordenes
                                                    riqueza de familias
                                            
                                 {<Proceso>} crea 1 worksheets por cada clase con importancia:   
                                   columnas [Orden, Familia, genero, spc, n_c, cat. amenaz, ]
                                 (VENTANA DE RESULTADO) >> (PASO 3)
                                    
        - Aspectos ecologicos
            (condicional) True > Animacion: "icono de progreso"
                                 {<Proceso>} crea 1 worksheets por cada clase con Grem. trof: 
                                   tabla columnas [Orden, Familia, genero, spc, n_c, gremio trof. ]
                                   grafico - torta: riqueza por gremio trof.
                                   
                                 {<Proceso>} crea 1 worksheets por cada clase con migracion: 
                                   tabla columnas [Orden, Familia, genero, spc, n_c,  migracion. ]
                                   grafico - torta: riqueza por clase migratorio.      
                                   
                                 {<Proceso>} crea 1 worksheets por cada clase con endemismo: 
                                   tabla columnas [Orden, Familia, genero, spc, n_c, endemismo. ]
                                   grafico - torta: riqueza por clase endemismo.   
                                   
                                {<Proceso>} crea 1 worksheets por cada clase con uso: 
                                   tabla columnas [Orden, Familia, genero, spc, n_c, uso. ]
                                   grafico - torta: riqueza por clase endemismo.   
                                   
        - Distribucion en coberturas
            (condicional) True > Animacion: "icono de progreso"                           
                                <Proceso>} crea 1 worksheets por cada clase con Grem. trof: 
                                   tabla de indices ecologicos en unidades de cobertura
                                   grafico - cladograma indice de jacard                     
'''                              
                                                                                                                             
#3. Retornar un nuevo documento con tablas y graficos                                   
                                   
'''
(VENTANA DE DESCARGAR) - opcion correo - descarga en equipo
    a- 

'''                                                                         
    







