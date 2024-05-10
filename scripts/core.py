import os
import re

from utils import get_page_content, extract_text, URL, CSS_SELECTOR


def comparison():
    if extract_text(get_page_content(URL), CSS_SELECTOR) != os.environ['PREVIOUS_STATUS']:
        return True
    else:
        return False


if __name__ == "__main__":
    comparison()
