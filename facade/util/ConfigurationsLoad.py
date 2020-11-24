import json


class Configurations:
    def __init__(self):
        with open("./resources/config.json") as json_data_file:
            data = json.load(json_data_file)
            self.__output_path = data['configs']['output_path']
            self.__necessary_data_for_path = data['configs']['mendeley_path']
            self.__description = data['other']['description']
            self.__validate_configs = data['other']['validate_configs']
            self.__delete_entire_output_directory = data['other']['delete_entire_output_directory']

    def get_output_path(self):
        return self.__output_path

    def get_description(self):
        return self.__description

    def get_validate_configs(self):
        return self.__validate_configs

    def get_necessary_data_for_path(self):
        return self.__necessary_data_for_path

    def get_delete_entire_output_directory(self):
        return self.__delete_entire_output_directory
