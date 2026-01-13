from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree, parse as ElementTreeParse
from src.config.Constant import *
from src.io.File import path_exists, del_file


def create_xml_file(xml, p):
    ElementTree(xml).write(p, xml_declaration=True, encoding='utf-8')


def generate_ve_manifest_xml(attrs):
    top = Element(XML_VEM_ROOT_NAME)
    top.set(XML_VEM_ROOT_ATTRIBUTE_NS, XML_VEM_ROOT_ATTRIBUTE_NS_VALUE)

    comment = Comment('Generated for Windows start menu tiles')
    top.append(comment)

    child = SubElement(top, XML_VEM_ELEMENT_VE)
    child.set(XML_VEM_ELEMENT_VE_ATTRIBUTE_I, attrs.get('display_name'))
    child.set(XML_VEM_ELEMENT_VE_ATTRIBUTE_II, attrs.get('logo_150'))
    child.set(XML_VEM_ELEMENT_VE_ATTRIBUTE_III, attrs.get('logo_70'))
    child.set(XML_VEM_ELEMENT_VE_ATTRIBUTE_IV, attrs.get('foreground_text'))
    child.set(XML_VEM_ELEMENT_VE_ATTRIBUTE_V, attrs.get('background_color'))

    return top


def generate_metadata_xml(attrs):
    top = Element(XML_MD_ROOT_NAME)
    top.set(XML_MD_ROOT_ATTRIBUTE_NS_XSD, XML_MD_ROOT_ATTRIBUTE_NS_XSD_VALUE)
    top.set(XML_MD_ROOT_ATTRIBUTE_NS_XSI, XML_MD_ROOT_ATTRIBUTE_NS_XSI_VALUE)

    child_ob = SubElement(top, XML_MD_ELEMENT_OB)
    child_ob.text = attrs.get('ob')

    child_op = SubElement(top, XML_MD_ELEMENT_OP)
    child_op.text = attrs.get('op')

    child_h = SubElement(top, XML_MD_ELEMENT_H)
    child_h.text = attrs.get('h')

    child_w = SubElement(top, XML_MD_ELEMENT_W)
    child_w.text = attrs.get('w')

    child_x = SubElement(top, XML_MD_ELEMENT_X)
    child_x.text = attrs.get('x')

    child_y = SubElement(top, XML_MD_ELEMENT_Y)
    child_y.text = attrs.get('y')

    return top


def read_ve_manifest_xml(xml_file_path):
    xml_file = ElementTreeParse(xml_file_path)
    root = xml_file.getroot()

    attrs = dict()
    for elem in root:
        attrs['display_name'] = elem.get(XML_VEM_ELEMENT_VE_ATTRIBUTE_I)
        attrs['logo_150'] = elem.get(XML_VEM_ELEMENT_VE_ATTRIBUTE_II)
        attrs['logo_70'] = elem.get(XML_VEM_ELEMENT_VE_ATTRIBUTE_III)
        attrs['foreground_text'] = elem.get(XML_VEM_ELEMENT_VE_ATTRIBUTE_IV)
        attrs['background_color'] = elem.get(XML_VEM_ELEMENT_VE_ATTRIBUTE_V)

    return attrs


def read_metadata_xml(xml_file_path):
    xml_file = ElementTreeParse(xml_file_path)
    root = xml_file.getroot()

    attrs = dict()

    for elem in root:
        if elem.tag == XML_MD_ELEMENT_OB:
            attrs['ob'] = elem.text
            continue
        if elem.tag == XML_MD_ELEMENT_OP:
            attrs['op'] = elem.text
            continue
        if elem.tag == XML_MD_ELEMENT_H:
            attrs['h'] = elem.text
            continue
        if elem.tag == XML_MD_ELEMENT_W:
            attrs['w'] = elem.text
            continue
        if elem.tag == XML_MD_ELEMENT_X:
            attrs['x'] = elem.text
            continue
        if elem.tag == XML_MD_ELEMENT_Y:
            attrs['y'] = elem.text
            continue

    return attrs


def run_ve_manifest(xml_file_path, attrs: dict):
    if path_exists(xml_file_path):
        old_attrs = read_ve_manifest_xml(xml_file_path)
        old_attrs.update(attrs)
        attrs = old_attrs.copy()

        del_file(xml_file_path)

    xml_file_data = generate_ve_manifest_xml(attrs)
    create_xml_file(xml_file_data, xml_file_path)


def run_metadata(xml_file_path, attrs: dict):
    if path_exists(xml_file_path):
        old_attrs = read_metadata_xml(xml_file_path)
        old_attrs.update(attrs)
        attrs = old_attrs.copy()

        del_file(xml_file_path)

    xml_file_data = generate_metadata_xml(attrs)
    create_xml_file(xml_file_data, xml_file_path)
