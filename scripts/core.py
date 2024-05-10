import os
from utils import get_page_content, extract_text, URL, CSS_SELECTOR

if __name__ == "__main__":
    def check_status():
        try:
            current_state = extract_text(get_page_content(URL), CSS_SELECTOR)
            previous_state = os.environ['PREVIOUS_STATUS']
            if current_state != previous_state:
                return True
            else:
                return False
        except Exception as e:
            raise f"Se produjo un error: {str(e)}"


    print(check_status())
