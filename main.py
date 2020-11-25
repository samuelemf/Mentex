from facade.OrganizerSystem import Organizer
from util.Presentation import *

"""
    Mentex is local a directory generator based on the BibTex citations generated from
    Mendeley groups, a feature not offered by Mendeley.
    
Author:
    Samuel E. Matos Flores
    https://github.com/samuelemf
    
Contribution:
    This project was able to be created with the utilization of Pybtex, 
    "A BibTeX-compatible bibliography processor in Python" according to the documentation.
    (https://pypi.org/project/pybtex/ | https://pybtex.org)
     
Args:
    resources/config.json
    resources/citations.bib

Catch:
    KeyError: If bibtex citation has missing mendeley-groups field.
    FileNotFoundError: If file to copy is not found.
"""


def main():
    welcome()
    Organizer().process()
    goodbye()


if __name__ == '__main__':
    main()
