import xml.etree.ElementTree as ET

# tree = ET.parse('./mrt.xml')
# root = tree.getroot()
#
# print(root)
#
# ODFare = root.findall('ODFare')
#
#
# for item in ODFare:
#     OriginStationID = item.find('OriginStationID')
#     print(OriginStationID.text)

tree = ET.parse('restaurant_C_f.xml')
root = tree.getroot()

# print(root.findall('Info'))
# print(root.find('Infos'))
# infos = root.find('Infos')
# print(infos.findall('Info'))

# for item in root.findall('Info'):
#     print(item.find('Name').text)
#     print(item.find('Add').text)
#     print('-----------------------------')

# print(root.findall('Info'))
# print(root.iter('Name'))

for item in root.iter('Info'):
    print(item.find('Name').text)

# for item in root.iter('Name'):
#     print(item.text)
