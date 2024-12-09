
# Documentación del Script
La funcionalidad es una limpieza general de multiples tablas del tipo xlsx para iniciar su tratamiento en un notebook
- Filas y columnas vacias
- Titulos individuales que falsean cabeceras
- Comentarios

## 1. Bibliotecas necesarias
Para instalar las bibliotecas necesarias, ejecute los siguientes comandos:
```bash
pip install pandas
pip install openpyxl
pip install ipython
```

## 2. Clases, funciones, y parámetros

### Clase `Utilidades`
- **Función `limpiar_consola()`**: Limpia la consola en función del sistema operativo.
- **Función `cuenta_regresiva()`**: Realiza una cuenta regresiva antes de salir, con opción de limpiar la pantalla en Jupyter.
  - **Retorno**: Sin valor de retorno (modifica la consola directamente).

### Clase `UtilidadesArchivos`
- **Función `listar_archivos_xlsx(directorio, gestor_directorios=None)`**: Lista archivos .xlsx en el directorio especificado.
  - **Parámetros**:
    - `directorio`: Ruta del directorio donde buscar archivos .xlsx.
    - `gestor_directorios` (opcional): Instancia de un gestor de directorios para cambiar de directorio si no se encuentran archivos.
  - **Retorno**: Diccionario con los archivos listados `{indice: nombre_archivo}`.
- **Función `seleccionar_archivos(archivos_dict)`**: Permite al usuario seleccionar archivos de una lista.
  - **Parámetros**:
    - `archivos_dict`: Diccionario de archivos listados con índices.
  - **Retorno**: Lista de archivos seleccionados por el usuario.

### Clase `GestorDirectorios`
- **Función `formatear_ruta(ruta, contexto='')`**: Formatea la ruta según el sistema operativo.
  - **Parámetros**:
    - `ruta`: Ruta que se desea formatear.
    - `contexto` (opcional): Contexto para diferenciar salida o ruta interna.
  - **Retorno**: Cadena con la ruta formateada.
- **Función `obtener_directorio_trabajo()`**: Solicita y establece el directorio de trabajo actual.
  - **Retorno**: Ruta del directorio de trabajo actual.

### Clase `VisualizadorDataframes`
- **Función `ajustar_ancho_pantalla(df)`**: Ajusta el ancho de pantalla para mostrar el DataFrame.
  - **Parámetros**:
    - `df`: DataFrame a visualizar con ajuste de ancho.
  - **Retorno**: Sin retorno directo (modifica la configuración de pantalla).
- **Función `resetear_ancho_pantalla()`**: Restablece el ancho de pantalla a valores predeterminados.
- **Función `visualizar_dataframes(directorio, archivos)`**: Carga y visualiza hojas de archivos Excel seleccionados.
  - **Parámetros**:
    - `directorio`: Ruta del directorio de trabajo.
    - `archivos`: Lista de archivos a visualizar.

### Clase `ProcesadorArchivosExcel`
- **Función `es_archivo_excel_valido(ruta_archivo)`**: Verifica la validez del archivo Excel.
  - **Parámetros**:
    - `ruta_archivo`: Ruta del archivo que se desea verificar.
  - **Retorno**: `True` si es válido; `False` en caso contrario.
- **Función `limpiar_hoja_actualizada(df)`**: Elimina filas y columnas vacías en un DataFrame.
  - **Parámetros**:
    - `df`: DataFrame a limpiar.
  - **Retorno**: DataFrame limpio sin filas o columnas vacías.
- **Función `procesar_archivos(archivos, directorio)`**: Limpia y guarda archivos Excel en el directorio especificado.
  - **Parámetros**:
    - `archivos`: Lista de archivos a procesar.
    - `directorio`: Ruta del directorio donde se encuentran los archivos.

### Clase `AplicacionConsola`
- **Parámetro de inicialización**: `in_colab` (booleano que indica si el entorno es Google Colab).
- **Función `aviso_seguridad()`**: Muestra un aviso de seguridad para trabajar con archivos respaldados.
- **Función `menu_principal()`**: Muestra el menú principal de la aplicación y permite seleccionar opciones.

## 3. Variables

- **IN_COLAB**: Variable que indica si el entorno es Google Colab.
- **archivos_dict**: Diccionario con los archivos .xlsx listados en el directorio.
- **archivos_seleccionados**: Lista de archivos seleccionados por el usuario.
- **directorio**: Directorio de trabajo actual.

## 4. Relaciones y dependencias

- La clase `AplicacionConsola` depende de `GestorDirectorios`, `VisualizadorDataframes`, y `ProcesadorArchivosExcel`.
- `IN_COLAB` determina el entorno y afecta a `AplicacionConsola` para la selección de rutas y el montaje de Google Drive.
- `archivos_dict` y `archivos_seleccionados` son generados y utilizados en `UtilidadesArchivos` para gestionar archivos .xlsx.
- `directorio` es gestionado por `GestorDirectorios` y afecta las operaciones de `AplicacionConsola`.

Este archivo proporciona una referencia estructurada del script, útil para entender su funcionamiento y dependencias.
