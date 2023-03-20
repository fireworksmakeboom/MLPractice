# XML Stuff
import xml.etree.ElementTree as ET
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))

# Json stuff

import json
data2 = '''
{
    "name": "Chuck",
    "phone": {
        "type": "intl",
        "number": "+1 734 303 4456"
    },
    "email": {
        "hide": "yes"
    }
}'''

info = json.loads(data2)
print('Name: ', info["name"])
print('Attr: ', info["email"]["hide"])


# calling a webservice happens with urllib just like in network