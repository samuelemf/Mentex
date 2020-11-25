from facade.files.util.directory.ManageDirectories import execute as directory_execute
from facade.files.util.copy.CopyFilesToDirectories import execute as file_execute
from facade.files.util.directory.ManageDirectories import delete
from util.Presentation import *
import os


class FileSystem:

    def __init__(self, configurations):
        self.__configs = configurations

    def operation(self, mendeley_files):
        if self.__configs.get_delete_entire_output_directory():
            delete(self.__configs.get_output_path())

        for file in mendeley_files:
            for current_mendeley_path in file.get_mendeley_group_path():
                directory_execute(os.path.join(self.__configs.get_output_path(), current_mendeley_path),
                                  self.__configs.get_description())
                file_execute(os.path.join(self.__configs.get_output_path(), current_mendeley_path),
                             os.path.join(self.__configs.get_necessary_data_for_path(), file.get_path()),
                             self.__configs.get_description())

            if self.__configs.get_description():
                print(space_separator()*2)

    def test_configurations_enabled(self):
        return self.__configs.get_validate_configs()

    def test(self, mendeley_file):
        for current_mendeley_path in mendeley_file.get_mendeley_group_path():
            print(configuration_test_details(os.path.join(self.__configs.get_output_path(), current_mendeley_path),
                                             os.path.join(self.__configs.get_necessary_data_for_path(),
                                                          mendeley_file.get_path()),
                                             self.__configs.get_output_path()))
