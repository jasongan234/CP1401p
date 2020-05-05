"""https://github.com/jasongan234/CP1401p/blob/master/prac06/languages.py"""
from prac06.programmng_languages import ProgrammingLanguage


def main():

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    list_of_languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in list_of_languages:
        if language.is_dynamic():
            print(language.name)

main()