import os

from utils import get_page_content, extract_text, CSS_SELECTOR, URL, CHANGE_MESSAGE, NO_STATE_MESSAGE, \
    NO_ELEMENT_MESSAGE


def check_version():
    try:
        # Obtener el contenido de la página web
        html_content = get_page_content(URL)

        if html_content:
            # Extraer el texto del elemento
            current_state = extract_text(html_content, CSS_SELECTOR)
            if current_state:
                # Obtener el estado anterior de la variable de entorno
                previous_state = os.environ['PREVIOUS_STATUS']
            else:
                raise Exception(NO_ELEMENT_MESSAGE)
                # Comparar el estado actual con el estado anterior

            if current_state != previous_state:
                return CHANGE_MESSAGE, current_state
            else:
                return "El texto sigue siendo el mismo.", current_state
        else:
            raise Exception("Error al obtener el contenido de la página web.")
    except Exception as e:
        return "Se produjo un error: " + str(e), None
