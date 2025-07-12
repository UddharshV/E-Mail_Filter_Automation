import re
import string

def clean_text(text):
    text = text.lower()
    text = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
    text = re.sub(r'\d+', '', text)      # Remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.strip()