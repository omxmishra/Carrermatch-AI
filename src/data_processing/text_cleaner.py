import re


def clean_text(text):

    # convert to string
    text = str(text)

    # lowercase
    text = text.lower()

    # replace contractions/apostrophes
    text = text.replace("’", "'")

    # remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # remove HTML tags
    text = re.sub(r'<.*?>', '', text)

    # replace punctuation with spaces
    text = re.sub(r'[^\w\s]', ' ', text)

    # remove numbers
    text = re.sub(r'\d+', '', text)

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text