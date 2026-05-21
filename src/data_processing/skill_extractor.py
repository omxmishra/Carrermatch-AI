import re

from src.utils.skills import skills


def extract_skills(text):

    found_skills = []

    for skill in skills:

        pattern = r'\b' + re.escape(skill) + r'\b'

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills