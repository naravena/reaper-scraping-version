import re

from utils import get_page_content, extract_text, URL, CSS_SELECTOR

if __name__ == "__main__":
    def current_state():
        try:
            aux = extract_text(get_page_content(URL), CSS_SELECTOR)
            return re.sub(r'[^\w\s.-]', '', aux)
        except Exception as e:
            raise f"Se produjo un error: {str(e)}"


    print(current_state())
