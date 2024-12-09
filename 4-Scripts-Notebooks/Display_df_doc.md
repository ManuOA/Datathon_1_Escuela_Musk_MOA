
# USO

Asegúrate cuando llames al módulo de lo siguiente:

## Celdas cabecera según entorno
Debes activar o desactivar una u otra con `#` según entorno.

### Celda 1 - ejemplo activado (Google Colab)

```python
from google.colab import drive
drive.mount('/content/drive')

import os
import sys

# Define el directorio de trabajo
directorio = '/content/drive/My Drive/resto/de/ruta'
os.chdir(directorio)  # Cambia al directorio de trabajo

# Añade la ruta del módulo externo a sys.path
ruta_modulo = r'/content/drive/My Drive/resto/de/ruta'  
sys.path.append(ruta_modulo)

# Guardar la ruta actual para restaurarla después
ruta_original = os.getcwd()

# Cambiar temporalmente a la ruta del módulo
os.chdir(ruta_modulo)

# Importar el módulo externo (solo se necesita importar una vez por sesión)
import Display_df  # Nombre del archivo del módulo sin extensión

# Restaurar la ruta original del notebook
os.chdir(ruta_original)
```

### Celda 2 - ejemplo desactivado (Entorno local)

```python
# import os
# import sys

# # Define el directorio de trabajo
# directorio = '/ruta/a/tu/directorio/de/trabajo'
# os.chdir(directorio)  # Cambia al directorio de trabajo

# # Añade la ruta del módulo externo a sys.path
# ruta_modulo = r'/ruta/a/tu/directorio/del/modulo'
# sys.path.append(ruta_modulo)

# # Guardar la ruta actual para restaurarla después
# ruta_original = os.getcwd()

# # Cambiar temporalmente a la ruta del módulo
# os.chdir(ruta_modulo)

# # Importar el módulo externo (solo se necesita importar una vez por sesión)
# import Display_df  # Nombre del archivo del módulo sin extensión

# # Restaurar la ruta original del notebook
# os.chdir(ruta_original)
```

## Llamada en celdas inferiores

```python
# Usar la función del módulo - Ejemplo
display_utilities.display_dataframe_with_scroll(df=df, title="Título tabla", separator_indices=[4,6])
```