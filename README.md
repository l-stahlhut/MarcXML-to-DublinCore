# MARC-XML to Dublin Core-XML Conversion

This script parses a MARC-XML file, extracts the relevant information for a Dublin Core-XML file, and wirtes a Dublin
Core XML-file.

## How to use the script
1. Download the MARC-XML file from the descriptive metadata for the Tay Bridge Enquiry mentioned below.
2. Install the requirements
```
$ pip install -r requirements.txt
```
3. Run the script to create a Dublin Core XML-file.
```
$ python3 parse_file.py
```

## Data
The [data](https://data.nls.uk/data/metadata-collections/tay-bridge-enquiry/) used for this project is the descriptive
metadata for the Tay Bridge Enquiry, which is publicly available on the website of the National Library of Scotland.

## Data Formats
You can get more information on the two data formats here: 
- MARC-XML tags: https://www.loc.gov/marc/bibliographic/bd6xx.html
- Dublin Core categories: https://www.dublincore.org/specifications/dublin-core/dces/
