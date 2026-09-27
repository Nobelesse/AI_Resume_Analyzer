import re

from modules.skill_extractor import (
    extract_skills
)


def extract_email(text):

    emails = re.findall(
        r'[\w\.-]+@[\w\.-]+',
        text
    )

    return emails[0] if emails else "Not Found"


def extract_phone(text):

    phones = re.findall(
        r'\+?\d[\d\s\-]{8,15}',
        text
    )

    return phones[0] if phones else "Not Found"


def extract_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line) > 2 and len(line) < 40:
            return line

    return "Not Found"


def parse_resume(text):

    data = {}

    data["name"] = extract_name(text)

    data["email"] = extract_email(text)

    data["phone"] = extract_phone(text)

    data["skills"] = extract_skills(text)

    return data