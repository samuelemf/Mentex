import shutil


def copy(output_path, file_path, description_feature):
    try:
        shutil.copy(file_path, output_path)
        if description_feature:
            print(f'File copied:\n\t{file_path}')
            print(f'File copied to:\n\t{output_path}')
    except FileNotFoundError:
        print(f"File: {file_path} was not found.\nTherefore, it was not copied.\nUsually it's a special character.")


def execute(output_path, file_path, description_feature):
    copy(output_path, file_path, description_feature)
