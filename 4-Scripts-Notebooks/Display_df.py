from IPython.core.display import display, HTML

def display_dataframe_with_scroll(df, title, separator_indices):
    """
    Mostrar un DataFrame con scroll vertical y horizontal.

    Se puede añadir una línea separadora fina y blanca entre columnas específicas.
    Los índices de separación (columnas después de las cuales se añade un borde)
    se definen al crear la función mediante el parámetro separator_indices.

    Args:
        df (pd.DataFrame): El DataFrame a mostrar.
        title (str): El título que se mostrará encima de la tabla.
        separator_indices (list of int): Lista de índices de columna después de los cuales se añade un borde de separación.
    """
    # Generar estilos CSS para las líneas de separación
    separator_styles = ""
    if separator_indices:
        for index in separator_indices:
            separator_styles += f"#scrollable th:nth-child({index + 1}), #scrollable td:nth-child({index + 1}) {{ border-right: 1px solid white !important; }}\n"

    # Generar la tabla HTML y el título
    display_html = f"""
    <style>
        #scrollable {{
            display: block;
            max-height: 300px;
            overflow-y: scroll;
            overflow-x: auto;
            border: 1px solid #ddd;
            white-space: nowrap;
        }}
        #scrollable thead th {{
            position: sticky;
            top: 0;
            background-color: #333; /* Fondo gris oscuro */
            color: #fff; /* Texto blanco para contraste */
            z-index: 2; /* Asegura que se muestren encima del contenido */
            text-align: left;
            border-bottom: 2px solid #ddd;
        }}
        #scrollable tbody td {{
            border-top: 1px solid #ddd;
        }}
        {separator_styles}
    </style>
    <div>
        <h3 style="text-align: left; margin-top: 10px;">{title}</h3>
        <div id="scrollable">
            {df.to_html(index=True, escape=False, classes='table table-striped')}
        </div>
    </div>
    """
    display(HTML(display_html))
