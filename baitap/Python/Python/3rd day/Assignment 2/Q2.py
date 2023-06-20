import codecs
import xml.etree.ElementTree as ET
import json

def find_mix_max(data):
    x = list()
    y = list()
    result = dict()
    for value in data[0]['points']:
        x.append(value['x'])
    for value in data[0]['points']:
        y.append(value['y'])
    result['x_min'] = str(min(x))
    result['x_max'] = str(max(x))
    result['y_min'] = str(min(y))
    result['y_max'] = str(max(y))
    return result


tree = ET.parse('xml_in.xml')
root = tree.getroot()
data = list()
for x in root.iter('bndbox'):
    print(x.find('xmin').text)


annotations = ET.Element('annotations')
folder = ET.SubElement(annotations, 'folder')
folder.text = 'images'
filename = ET.SubElement(annotations, 'filename')
filename.text = '1_1.jpg'
folder = ET.SubElement(annotations, 'folder')
folder.text = 'VOC'
size = ET.SubElement(annotations, 'size')
width = ET.SubElement(size, 'width')
width.text = '560'
height = ET.SubElement(size, 'height')
height.text = '360'
depth = ET.SubElement(size, 'depth')
depth.text = '3'
Object = ET.SubElement(annotations, 'object')
name = ET.SubElement(Object, 'name')
name.text = "thyroid_cancer"
pose = ET.SubElement(Object, 'pose')
pose.text = "Unspecified"
truncated = ET.SubElement(Object, 'truncated')
truncated.text = "0"
difficult = ET.SubElement(Object, 'difficult')
difficult.text = "0"

for child in root.iter('mark'):
    data = json.loads(child.find('svg').text)
    # print(data)
    result = find_mix_max(data)
    bndbox = ET.SubElement(Object, 'bndbox')
    xmin = ET.SubElement(bndbox, 'xmin')
    xmin.text = result['x_min']
    xmax = ET.SubElement(bndbox, 'xmax')
    xmax.text = result['x_max']
    ymin = ET.SubElement(bndbox, 'ymin')
    ymin.text = result['y_min']
    ymax = ET.SubElement(bndbox, 'ymax')
    ymax.text = result['y_max']


tree = ET.ElementTree(annotations)

with open ('xml_out.xml', "wb") as files :
    tree.write(files)

print(ET.tostring(annotations, encoding='utf8').decode('utf8'))