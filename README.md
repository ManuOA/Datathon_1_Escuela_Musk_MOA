# Objetivos personales

Participar en el 1er datathon de la escuela Musk como aprendizaje. Esto implica:

- No se prioriza el concursar, sino aprender y que se valoren los procedimientos y razonamientos usados.
- El objetivo prioritario personal es aprender. Esto implica intentar desarrollar paradigmas de programación
  ya estudiados y desenvolverse en la red o interactuar correctamente con ChatGPT para usar recursos no 
  aprendidos pero necesarios para realizar la consecución del proyecto.

# Objetivos del proyecto

El objetivo final es intentar analizar el impacto socioeconómico producido por la transformación en el sector del 
transporte por carretera en España con la transición impuesta para emisiones cero por la CEE.  
El esquema de pasos básicos a seguir será:

- Proyección de la evolución de la población residente en España como base para la proyección del parque
  de vehículos.
    
- Proyección de la evolución del mercado de vehículos, relacionando la curva de población con el histórico del mercado 
  de vehículos previo a 2023 en España. Nos marcaremos unos hitos básicos impuestos por la CEE.

    + 2035: Solo se podrán vender vehículos nuevos de emisión CO₂ totalmente cero.
    + 2050: Solo podrán circular vehículos de emisión CO₂ totalmente cero.

- Por facilidad inicial, vamos a tratar una evolución total hacia el mercado del vehículo eléctrico, aun sabiendo que 
  no es realista, ya que el mercado se compartirá con otros vehículos de emisión cero.  
  En todo caso, se analizará la huella económica de los vehículos de hidrógeno y e-Fuel como alternativas de cero emisiones y su rentabilidad.
    
- Proyectar las necesidades de producción eléctrica por el cambio radical de la combustión fósil a la movilidad 
  eléctrica (en principio total, aunque sea irreal), comparándolas con series históricas.

# Preguntas a resolver

Intentaremos sacar algunas respuestas a preguntas del tipo:

- ¿Cómo puede afectar a la economía familiar y de empresas la movilidad eléctrica?

    + Eficiencia y costes de las diferentes tecnologías.
    + ¿Cómo afectan los impuestos?
    
- ¿Cómo se puede producir la reforma del parque de vehículos bajo un concepto de mínimos para cumplir con los plazos de la CEE?

    + Proceso de transición energética
    + Impacto macroeconómico y cómo le afectan los impuestos.
    + Impacto en las empresas petroleras.

- Impacto en la demanda final de energía del país:

    + Incremento en la demanda final.
    
- Conclusiones
    
- Dudas en el aire y desafíos:

    + ¿Dónde y cómo se aplicarán los impuestos que no son progresivos de manera que afecten lo menos posible a las clases bajas?
    + Desafío de la automoción por hidrógeno para ser competitiva (símil diésel vs. gasolina).
    + ¿Dónde quedaría el futuro del hidrógeno (noche, falta de viento y sol, transporte aéreo o marítimo)?
    + ¿Hay futuro para el e-fuel?
    + ¿Hacen falta más presas? Reto hidráulico.

# Fuentes de datos

- INE - https://www.ine.es/dyngs/INEbase/es/categoria.htm?c=Estadistica_P&cid=1254734710984
- DGT - https://www.dgt.es/menusecundario/dgt-en-cifras/
- OTLE - https://otle.transportes.gob.es/movilidad
- BDOTLE - https://apps.fomento.gob.es/BDOTLE/visorBDpop.aspx?i=314
- Red Eléctrica Española - https://www.ree.es/es
- ChatGPT

# Categorías para la agrupación de los datos

Vamos a iniciar con cuatro categorías, aunque no se descarta la necesidad de tener que incluir alguna más.  
Las categorías nos sirven para renombrar los archivos en origen, acortando su nombre para evitar problemas y
una identificación rápida en su uso.

- **Cgt A**: Relacionadas con la población.
- **Cgt B**: Relacionadas con el número de vehículos terrestres y kilometraje promedio.
- **Cgt C**: Relacionadas con el consumo de energía del sector transporte y de vehículos.
- **Cgt D**: Relacionadas con producción, consumo y costes de energía eléctrica de España.

# Estructura del notebook

- Titulos principales # y **negrita**
- Titulos de comentarios #### y **negrita**
- Comentarios con sangria (dos espacios) y - o +
- Secciones con dataframes o graficas # y **negrita**
- titulos de dataframes o grafica en primera linea de codigo # @title 'Denominacion'

# **Informacion de interes de los apartados del notebook** (indicaciones, dependencias, resultados, fuentes, nomenclaturas)

## **Informacion** (ejecucion del entorno de trabajo)

- Especificar el entorno de trabajo cuando se pregunte
- Se monta el entorno de trabajo correspondiente
- Se cargan modulos externos
- Las importaciones necesarias para la ejecucion del notebook se cargan
- Se pregunta si se desea ejecutar el programa de limpieza

### Dependencias:
- Modulos externos:
  - DtSht_Clean.py
  - Display_df.py

## **Informacion** (evolucion de la poblacion residente en España)

### Dependencias:
- Excels preprocesados:
  - Ctg-A01.xlsx (historico)
  - Ctg-A02.xlsx (proyeccion)
- Fuente: https://www.ine.es/dyngs/INEbase/es/categoria.htm?c=Estadistica_P&cid=1254734710984
- Dataframes:
  - df_poblacion2 (temporal)

### Resultados:
- Dataframes:
  - df_poblacion
  - df_poblacion_copy

## **Informacion** (Evolucion del parque de vehiculos en funcion de la poblacion)

### Dependencias:
  - Excels preprocesados:
    - Ctg-B01.xlsx (historico parque)
      - Hoja - parque_tipos
      - Hoja - parque_camiones
      - Hoja - parque_furgonetas
    - Fuente: https://www.dgt.es/menusecundario/dgt-en-cifras/
  - Dataframes:
    - df_poblacion
    - df2 (temporal)
    - df3 (temporal)

### Resultados:
  - Dataframes:
    - df
    - df_copy

## **Informacion** (proyeccion del consumo de energia en funcion del parque de Veh convencional)

### Dependencias:
  - Excels preprocesados:
    - Ctg-C01.xlsx (Consumo de energia en el sector transporte)
  - Fuente: https://apps.fomento.gob.es/BDOTLE/visorBDpop.aspx?i=314
  - Dataframes:
    - df4 (temporal)

### Resultados:
  - Dataframes:
    - df7
    - df7_copy

## **Informacion** (matriculaciones y bajas - verificacion de errores)

### Dependencias:
  - Excels preprocesados:
    - Ctg-B02.xlsx (matriculaciones)
      - Hoja - Matr_tipo_veh
      - Hoja - Matr_ciclomotores
      - Hoja - Matr_camio_men_3500_furg_car
      - Hoja - Matr_todos_cam_furg_carga
    - Ctg-B03.xlsx (bajas)  
    - Fuente: https://www.dgt.es/menusecundario/dgt-en-cifras/
  - Dataframes:
    - df7
    - df7_copy
    - df10 (temporal)
    - df11 (temporal)
    - df12 (temporal)
    - df13 (temporal)
    - df14 (temporal)
    - df15 (temporal)

### Resultados:
  - Dataframes:
    - df16 (matriculaciones)
    - df16_copy
    - df17 (bajas)
    - df17_copy
    - df20 (error)
    - df20_copy
    - df21 (correcion del error - tabla completa)
    - df21_copy

## **Informacion** (impacto de la movilidad de cero emisiones)

### Dependencias:
  - Excels preprocesados:
    - Ctg-D06.xlsx (Eficicias de tipos de vehiculo por tipo de combustible)  
    - Fuente: tabla creada con la ayuda de chat GPT
    - Ctg-D0.xlsx (Tablas de precios)
    - Fuente: chat GPT

### Resultados:
  - Dataframes:
    - df30 (eficiencia y costes de tipos de vehiculos a los 100Km)
    - df33 (precios)
    - df30_copy

## **Informacion** (transicion completa del parque de Veh a EV para el 2050)

### Dependencias:
  - Dataframes:
   - df
   - df21

### Resultados:
  - Dataframes:
    - df40 (transicion Veh - EV)
    - df40_copy

## **Informacion** (Transicion energetica en el secto transp. vial)

### Dependencias:
  - Excels preprocesados:
    - Ctg-B05.xlsx (kilometraje anual por tipo de vehiculo)  
    - Fuente: https://www.dgt.es/menusecundario/dgt-en-cifras/
  - Dataframes:
    - df7

### Resultados:
  - Dataframes:
    - df51 (media km/año por tipo de vehiculo 2014 -2023)
    - df51_copy
    - df50 
    - df50_copy

