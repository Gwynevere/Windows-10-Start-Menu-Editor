from src.config.Constant import *


def validate_ve_manifest(attrs):
    if (
            attrs.get(XML_VEM_ELEMENT_VE_ATTRIBUTE_I) is not None and
            attrs.get(XML_VEM_ELEMENT_VE_ATTRIBUTE_II) is not None and
            attrs.get(XML_VEM_ELEMENT_VE_ATTRIBUTE_III) is not None and
            attrs.get(XML_VEM_ELEMENT_VE_ATTRIBUTE_IV) is not None and
            attrs.get(XML_VEM_ELEMENT_VE_ATTRIBUTE_V) is not None
    ):
        return True
    return False


def validate_metadata(attrs):
    if (
            attrs.get(XML_MD_ELEMENT_OB) is not None and
            attrs.get(XML_MD_ELEMENT_OP) is not None and
            attrs.get(XML_MD_ELEMENT_H) is not None and
            attrs.get(XML_MD_ELEMENT_W) is not None and
            attrs.get(XML_MD_ELEMENT_X) is not None and
            attrs.get(XML_MD_ELEMENT_Y) is not None
    ):
        return True
    return False
