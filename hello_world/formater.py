import xml.etree.ElementTree as xmlTree

PLAIN = "plain"
PLAIN_UP = "plain_uppercase"
PLAIN_LO = "plain_lowercase"
JSON = "json"
XML = "xml"
SUPPORTED = [PLAIN, PLAIN_UP, PLAIN_LO, JSON]


def get_formatted(msg, imie, style):
    result = ""
    if style == PLAIN:
        result = plain_text(msg, imie)
    elif style == PLAIN_UP:
        result = plain_text_upper_case(msg, imie)
    elif style == PLAIN_LO:
        result = plain_text_lower_case(msg, imie)
    elif style == JSON:
        result = format_to_json(msg, imie)
    elif style == XML:
        result = format_to_xml(msg, imie)
    return result


def format_to_json(msg, imie):
    return ('{ "imie":"' + imie + '", "msg":' +
            msg + '"}')


def format_to_xml(msg, imie):
    root = xmlTree.Element("greetings")
    n = xmlTree.Element("name")
    root.append(n)
    n.text = imie
    m = xmlTree.Element("msg")
    root.append(m)
    m.text = msg
    return xmlTree.tostring(root, "unicode", 'xml')


def plain_text(msg, imie):
    return imie + ' ' + msg


def plain_text_upper_case(msg, imie):
    return plain_text(msg.upper(), imie.upper())


def plain_text_lower_case(msg, imie):
    return plain_text(msg.lower(), imie.lower())
