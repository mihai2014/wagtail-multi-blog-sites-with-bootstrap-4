from lxml import html, etree

html_str = """
<html>
    <head>
    </head>

    <body>
	<div id="my_div" class="some_style">this is my div</div>
    </body>
</html>
"""

#parsing html string with lxml.html is less restrictive than lxml.etree
#doc = etree.fromstring(html_str)
doc = html.fromstring(html_str)

items = doc.xpath('//div[@id="my_div"]')

my_div = items[0]

print my_div.tag
print my_div.text 
print my_div.attrib

items = doc.xpath('/html/body')
body = items[0]

ul = etree.SubElement(body, 'ul')
li = etree.SubElement(ul, 'li')
a = etree.SubElement(li, 'a', href = 'http://infohost.nmt.edu/tcc/help/pubs/pylxml/pylxml.pdf')
a.text = "Lxml doc I"
span = etree.SubElement(a, 'span')
span.set('class','caret')

ul = etree.SubElement(body, 'ul')
li = etree.SubElement(ul, 'li')
a = etree.SubElement(li, 'a', href = 'http://lxml.de/')
a.text = "Lxml doc II"
span = etree.SubElement(a, 'span')
span.set('class','caret')

print html.tostring(doc)

