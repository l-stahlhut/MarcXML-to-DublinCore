from pymarc import parse_xml_to_array
from lxml import etree as ET

# input file (marc-xml)
filename = 'data/Tay-Bridge-Enquiry/Tay-Bridge-Enquiry-dataset-MARC.xml'

# parse marc-xml, filter out info needed for dc xml
records = parse_xml_to_array(filename)

# extract relevant information for the dublin core xml-file
dc_records = []
for record in records:
    d = {}
    # Identifier: An unambiguous reference to the resource within a given context.
    d['identifier'] = [record['001'].data]  # control number, Electronic Location and Access (R)
    d['identifier'].append(record['856']['u'])
    # Title: A name given to the resource.
    d['title'] = record.title
    # Creator: An entity primarily responsible for making the resource.
    for field in record.get_fields('700'):
        if field['e'] == 'Author.':
            d['creator'] = [(field['a'])]  # author
        elif field['e'] == 'Patron.':
            d['creator'].append(field['a'])  # patron
    # Format: The file format, physical medium, or dimensions of the resource.
    d['format'] = [record['336']['a'], record['347']['b']]  # content type term (e.g. still image), encoding format (e.g. JPEG)
    # Extent: The size or duration of the resource.
    d['extent'] = record['300']['a']
    # Publisher: An entity responsible for making the resource available.
    d['publisher'] = record['264']['b']
    # Date: A point or period of time associated with an event in the lifecycle of the resource.
    d['date'] = record['264']['c']
    # Description: An account of the resource.
    d['description'] = [record['500']['a'].rstrip(), record['518']['a'].rstrip(), record['520']['a'].rstrip()]
    # Is version of
    d['isVersionOf'] = record['534']['p'] + ' ' + record['534']['t'] + ' ' + record['534']['e']
    # Subject: The topic of the resource.
    d['subject'] = [field['a'] for field in record.get_fields('650')]  # Topical term
    d['subject'].append(record['651']['a'].rstrip())  # Geographic name
    # Rights: Information about rights held in and over the resource.
    d['rights'] = record['540']['a']

    dc_records.append(d)

# Create the root element with the namespace declaration for 'dc'
rdf = ET.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF", xmlns_dc="http://purl.org/dc/elements/1.1/")

# Iterate through your list of dictionaries
for data in dc_records:
    description = ET.Element("Description")

    # Add elements for each key-value pair in the dictionary
    for key, value in data.items():
        if isinstance(value, list):
            for item in value:
                sub_element = ET.SubElement(description, key)
                sub_element.text = item
        else:
            sub_element = ET.SubElement(description, key)
            sub_element.text = value

    # Append the description element to the root
    rdf.append(description)

# Create an ElementTree object, write the XML data to a file
tree = ET.ElementTree(rdf)
tree.write("result_DC.xml", encoding="UTF-8", xml_declaration=True)


