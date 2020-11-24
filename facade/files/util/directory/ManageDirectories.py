import os
import shutil


def delete(path):
    shutil.rmtree(path)


def create(path, description_feature):
    os.makedirs(path)

    if description_feature:
        print(f'Directory created:\n\t{path}')


def validate_existence(path):
    return os.path.exists(path)


def execute(path, description_feature):
    if not validate_existence(path):
        create(path, description_feature)
