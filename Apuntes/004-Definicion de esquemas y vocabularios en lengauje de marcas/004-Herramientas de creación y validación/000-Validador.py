from lxml import etree

xml_doc = etree.parse("002-Curriculum.xml")
xsd_doc = etree.parse("003-Curriculum.xsd")

schema = etree.XMLSchema(xsd_doc)

print(schema.validate(xml_doc))
