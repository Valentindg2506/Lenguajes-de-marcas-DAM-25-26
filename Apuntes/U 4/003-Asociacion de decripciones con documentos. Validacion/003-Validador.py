from lxml import etree

xml_doc = etree.parse("001-Documento de referencia.xml")
xsd_doc = etree.parse("002-Esquema.xsd")

schema = etree.XMLSchema(xsd_doc)

print(schema.validate(xml_doc))
