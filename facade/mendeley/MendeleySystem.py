from facade.mendeley.util.BibTexFileProcessing import *


class MendeleySystem:
    def __init__(self):
        self.__mendeley_list = None

    def get_mendeley_list(self):
        return self.__mendeley_list.copy()

    def operation(self):
        self.__mendeley_list = process_bib_file()
