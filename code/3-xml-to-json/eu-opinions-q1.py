import xml.etree.ElementTree as ET
import pprint
pp = pprint.PrettyPrinter(indent=2)

fp = open("eurobarometer_merge.xml","r")
element = ET.parse(fp)
c = element.findall('Mashup/Country')
respondents09 = element.findall('Mashup/Country/Dataset[@name = "Eurobarometer 2009"]/Record/Respondents')
respondents13 = element.findall('Mashup/Country/Dataset[@name = "Eurobarometer 2013"]/Record/Respondents')
respondents19 = element.findall('Mashup/Country/Dataset[@name = "Eurobarometer 2019"]/Record/Respondents')

l = []
l2 = []
for i in respondents09:
    l.append(i.text)
for x in l:
    if x == 'None':
        l2.append('null')
    else:
        l2.append(int(x))
print(l2)

l3 = []
l4 = []
for i in respondents13:
    l3.append(i.text)
for x in l3:
    if x == 'None':
        l4.append('null')
    else:
        l4.append(int(x))
print(l4)

l5 = []
l6 = []
for i in respondents19:
    l5.append(i.text)
for x in l5:
    if x == 'None':
        l6.append('null')
    else:
        l6.append(int(x))
print(l6)








