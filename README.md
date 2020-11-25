# Mentex

Mentex is a local directory generator based on the BibTex citations from Mendeley groups, a feature not offered by Mendeley.

This idea arose from the problem of obtaining the directory where a research document was stored in Mendeley groups. They provide the ability to generate a copy of the files stored, but not name of the directories used. Mentex generates a copy of the directories and the files stored. Thus, we can have the actual directories created in Mendeley in a local copy. 

<img width="1000" height="1000" alt="local-copies-options" src="https://drive.google.com/thumbnail?id=1wFcncfdRm4w14D2kecWFHuqx1J2oRfSd" />
<p align="center">
  <img alt="copy" src="https://drive.google.com/thumbnail?id=11HZN2YfgJTX7QPpWdHCwNb9hKJ8lInfe" />
  <img alt="bibtex" src="https://drive.google.com/thumbnail?id=16fMoknqILR91614YIwsmFr6zh3CV_L5n" />
</p>

## Dependencies

* python 3.8.2 or older

* pybtex 0.23.0 or older

```
pip install pybtex
```

## Usage

Mentex looks at the BibTex citations copied from Mendeley, once placed in the citations.bib located in the resource’s directory. Mentex looks for 3 specific fields from these citations:
1.	file
2.	mendeley-groups
3.	title
Example:

resources/config.js
```
{
    "configs":{
        "output_path":"/Users/foo/Drive_backup/Research",
        "mendeley_path": "/"
    },
    "other":{
        "description":false,
        "validate_configs":true,
        "delete_entire_output_directory":true
    }
}
```

resources/citations.bib
```
@article{ABC,
file = {:Users/user/ Mendeley/2008/2008{\_}ABC_ok.pdf:pdf}, 
mendeley-groups = {Mendeley_directory_name},
title = {{ABC ok}},
}
```


## How It Works

With this data, Mentex can know where the document is stored in the Mendeley group directory and a location from where to copy the documents. Finally, for each citation entered in the document, Mentex will copy the documents to its corresponding directory. Thus, creating an exact copy of the directories and the documents in a specified local directory.

These can be utilized with a cloud storage service, like Google Drive, to automatically stored the files in the cloud with the same directory created in Mendeley. All you have to do is select the output path to be a directory synchronized with any of these services.

## Credits

This project was able to be created with the utilization of Pybtex, "A BibTeX-compatible bibliography processor in Python" according to the documentation.

(https://pypi.org/project/pybtex/ | https://pybtex.org)

## Config

There are some configurations that can be tweaked. All of them are located in the config.js file in the resource’s directory. 
* Output path of the generated directories and documents.
* Mendeley path: any additional data Mentex needs to find the files. For example: \ (for macOs) or C:\\user... (for Windows)
* Description: present details of the actions completed during the process.
[**true** or **false**]
* Validation: validate the configurations. For example: review the path. Make sure it was generated correctly before using.
[**true** or **false**]
* Delete entire output path: Mentex does not look for new or older documents. It just copies the current documents and directories. To make sure the copy is as accurate as possible, it's recommended to delete the directory and generate it from 0 every time.
[**true** or **false**]
