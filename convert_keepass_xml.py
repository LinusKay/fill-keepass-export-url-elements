# KeePassToLastPassURLConvert
#
# Insert placeholder URL value into empty URL elements in KeePass exported XML
# Prevents LastPass from importing passwords as plaintext "note" items
#
# Accepts KeePass exported XML file as input (including extension)
# Eg: TestKeePassXML.xml
# 
# By Linus Kay

import xml.etree.ElementTree as ET
fileInput = input('KeePass XML file: ')
fileName = fileInput.replace('.xml', '')
outputName = fileName + '_updated.xml'
placeholderURL = 'www.no-url.com.au'

tree = ET.parse(fileInput)
root = tree.getroot()
for stringElement in root.iter('String'):
    keyElement = stringElement.find('Key')
    if keyElement.text == 'URL':
        valueElement = stringElement.find('Value')
        if valueElement.text == None:
            valueElement.text = placeholderURL
tree.write(outputName)
print(f"Exported to '{outputName}'")