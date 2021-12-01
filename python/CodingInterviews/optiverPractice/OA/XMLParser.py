import xml.etree.ElementTree as ET

class XMLParser(object):

    """
    Verifies if there are multiple of the same element
    :param elements, exception: multiple "elements" and an "exception" of we are excluding from the check, in
    this case Symbol as it's the only element there are allowed multiple of
    :return: XMLFoundTooManyElementsError() if duplicate elements
    """
    @staticmethod
    def verify_elem_dup(elements, exception):
        element_map = []
        for element in elements.iter():
            if element.tag != exception and element.tag in element_map:
                raise XMLFoundTooManyElementsError()
            else:
                element_map.append(element.tag)
    
    """
    Verifies value of element attribute, for purpose of assessment
    specifically handles boolean, but can be changed to more data types
    :param elem_to_check, value: element of attribute we are checking and attribute value
    :return: value of attr, if not boolean return XMLBooleanParsingError() 
    """
    @staticmethod 
    def verify_elem_attr(elem_to_check, value):
        tree_value = elem_to_check.attrib[value].lower()
        if tree_value == "true":
            tree_bool = True
            return tree_bool
        elif tree_value == "false":
            tree_bool = False
            return tree_bool
        else:
            raise XMLBooleanParsingError()

    """
    Checks if elem_to_check is in parent_elem
    :param parent_elem, elem_to_check: element we are looping through and element we are checking for
    :return: boolean 
    """
    @staticmethod
    def verify_elem(parent_elem, elem_to_check):
        if parent_elem.find(elem_to_check) is not None:
            return True
        return False

    """
    Gets Multiplier text, casts as float and if it is a whole num and does not contain
    decimals, cast as int
    :param elements: Element of ElementTree
    :return: mulitplier value, raises XMLIntegerParsingError() if item is not an integer
    """
    @staticmethod
    def get_mult_val(elements):
        mult = float(elements.find("Multiplier").text)
        if mult % 1 == 0: 
            mult = int(mult)
            return mult
        else:
            raise XMLIntegerParsingError()

    """
    Loops through all symbol text and add to list, does not
    add duplicates and sorts alphabetically before returning
    :param elements: Element of ElementTree
    :return: list of all symbols in Element
    """
    @staticmethod
    def get_symbols(elements):
        symbols = []
        for symbol in elements.findall("Symbols/Symbol"):
            if symbol.text not in symbols:
                symbols.append(symbol.text)
        symbols.sort()
        return symbols

    """
    Parses xml file input, uses helper methods for abstraction
    :param cls, input_xml: class and "input_xml", xml file that holds data to be parsed
    :return: parsed xml file with result structure
    """
    @classmethod
    def get_data_from_xml(cls, input_xml):
        # Create tree from input xml 
        tree = ET.parse(input_xml)
        tree_name = tree.findall(r'Name')[0].text
        multiplier_value = 100

        # Built first part of result
        result = {
            'name': tree_name,
            'strategies': [],
        }

        # Loop through Tree and find all elements in Tree
        for element in tree.findall(r'TradingStrategies/TradingStrategy'):
            # Create booleans if Elements exist to prevent "type None" error
            verify_elem_mult = cls.verify_elem(element, 'Multiplier')
            verify_elem_sym = cls.verify_elem(element, 'Symbols/Symbol')

            # Checks if there are any duplicate Elements, returns excpetion if so, 
            # Takes Exception 'Symbol' since we are allowed dups of that
            cls.verify_elem_dup(element, 'Symbol')
            enabled_bool = cls.verify_elem_attr(element, 'enabled')

            # If Elements exist, get their values
            if verify_elem_mult:
                multiplier_value = cls.get_mult_val(element)

            if verify_elem_sym:
                symbol_list = cls.get_symbols(element)

            # Append data after every loop
            result['strategies'].append(
                {
                    'enabled': enabled_bool,
                    'symbols': symbol_list,
                    'multiplier': multiplier_value
                }
            )
        # Return final Data Structure
        return result

parse = XMLParser() 
print(parse.get_data_from_xml("input003.xml"))