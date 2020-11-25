from facade.mendeley.MendeleySystem import MendeleySystem
from facade.files.FileSystem import FileSystem
from facade.util.ConfigurationsLoad import Configurations


class Organizer:
    def __init__(self):
        self.__subsystem_a = MendeleySystem()
        self.__subsystem_b = FileSystem(Configurations())

    def process(self):
        self.__subsystem_a.operation()
        if not self.__subsystem_b.test_configurations_enabled():
            self.__subsystem_b.operation(self.__subsystem_a.get_mendeley_list())
        else:
            self.__subsystem_b.test(self.__subsystem_a.get_mendeley_list()[0])
