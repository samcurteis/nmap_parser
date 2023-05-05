import xml.etree.ElementTree as ET
root = ET.parse('results.xml').getroot()

def parse_file():
    final_res = {}
    for child in root:
        if child.tag == 'host':
            ports = child.find('ports')
            for child in ports:
                firstTag = child[0].tag
                if firstTag == 'state':
                    if child[0].attrib['state'] == 'open':
                        print(child.attrib['portid'], child.attrib['protocol'], child[1].attrib['name'], child[0].attrib['state'])

parse_file()
