import os

from utils import get_page_content, extract_text, URL, CSS_SELECTOR, CHANGE_MESSAGE, NO_ELEMENT_MESSAGE


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
                    return CHANGE_MESSAGE + ' ' + current_state
                else:
                    return f"El texto sigue siendo el mismo: {current_state}"
            else:
                raise Exception(NO_ELEMENT_MESSAGE)
        else:
            raise Exception("Error al obtener el contenido de la página web.")
    except Exception as e:
        return f"Se produjo un error: {str(e)}"

    # Ejemplo de uso


result = check_version()
print(result)
