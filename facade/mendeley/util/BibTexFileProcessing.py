from facade.mendeley.file.File import MendeleyFile
from pybtex.database.input import bibtex


def process_bib_file():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('./resources/citations.bib')
    try:
        return [MendeleyFile(bib_data.entries[bib].fields['file'][1:-4].replace('{\_}', '_'),
                             bib_data.entries[bib].fields['mendeley-groups'],
                             bib_data.entries[bib].fields['title']) for bib in bib_data.entries.keys()]
    except KeyError:
        print('There is one or more files missing the mendeley-group field in the citations.\nReview and try again.')
