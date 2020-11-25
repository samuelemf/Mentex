def space_separator():
    return '-'*75


def welcome():
    print('Welcome to Mentex!\n\n\tThanks for using this application.')
    print('\tBe sure to suggest any fixes or new features.')
    print(space_separator())


def goodbye():
    print(space_separator())
    print('Review the results of the organizer.')
    print('Thank you for using this applications to generate a local copy of your research documents.')


def configuration_test_details(directory, file, output):
    print(f'\nDirectory example:\n\t{directory}')
    print('\n' + space_separator())
    print(f'\nFile to move:\n\t{file}\n')
    print("Test if you can find this file successfully with the parameters. "
          "If not, change it's until its correct.")
    print('\n' + space_separator())
    print(f'\nOutput directory:\n\t{output}')
    print('\n' + space_separator())
    print('If the test output look correct, please change the validate_configs to false to start the process.')
