import os

from utils import get_page_content, extract_text, URL, CSS_SELECTOR, CHANGE_MESSAGE

print("dadvvvvvvvvvvvvv         " + os.environ['PREVIOUS_STATUS'])


def comparison():
    if extract_text(get_page_content(URL), CSS_SELECTOR) != os.environ['PREVIOUS_STATUS']:
        return CHANGE_MESSAGE
    else:
        return ""


if __name__ == "__main__":
    print(comparison())
