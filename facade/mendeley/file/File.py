class MendeleyFile:
    def __init__(self, absolute, mendeley, name):
        self.__absolute_path = absolute
        self.__mendeley_group = mendeley.split(',')
        self.__file_name = name

    def get_name(self):
        return self.__file_name

    def get_mendeley_group_path(self):
        return self.__mendeley_group

    def get_path(self):
        return self.__absolute_path
