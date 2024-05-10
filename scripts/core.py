import os

from utils import get_page_content, extract_text, URL, CSS_SELECTOR,CHANGE_MESSAGE, NO_ELEMENT_MESSAGE


def check_version():
    try:
        # Obtener el contenido de la página web
        html_content = get_page_content(URL)

        if html_content:
            # Extraer el texto del elemento
            current_state = extract_text(html_content, CSS_SELECTOR)
            previous_state = os.environ['PREVIOUS_STATUS']

            if previous_state and current_state:
                if current_state != previous_state:
                    return CHANGE_MESSAGE, current_state
                else:
                    return "El texto sigue siendo el mismo.", current_state
            else:
                raise Exception(NO_ELEMENT_MESSAGE)
        else:
            raise Exception("Error al obtener el contenido de la página web.")
    except Exception as e:
        return "Se produjo un error: " + str(e), None


# Ejemplo de uso
mensaje, estado_actual = check_version()
print(mensaje)  # Imprime el mensaje correspondiente
if estado_actual:
    print("Estado actual:", estado_actual)
