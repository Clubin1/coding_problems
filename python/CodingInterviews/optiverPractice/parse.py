import xml.etree.ElementTree as ET 

xml_tree = ET.parse("sample.xml")
xml_root = xml_tree.getroot()

def print_all_items():
    for x in xml_root.findall("food"):
        item = x.find("item").text
        price = x.find("price").text
        desc = x.find("description").text
        cal = x.find("calories").text
        print(item, price, desc, cal)


def update_tag():
    # update each item desc tag
    for i in xml_root.iter("description"):
        a = str(i.text) + " New Description"
        i.text  = str(a)
        i.set('updated', 'yes')
        xml_tree.write("new.xml")

def add_tag():
    # add tag in root
    ET.SubElement(xml_root[0], 'specialty')
    for i in xml_root.iter('specialty'):
        title = "South Indian Special"
        i.text = str(title)
    xml_tree.write("add.xml")
    print("New xml has been created")


print_all_items()
add_tag()