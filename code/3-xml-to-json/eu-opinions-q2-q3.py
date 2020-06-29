import xml.etree.ElementTree as ET
import pprint
pp = pprint.PrettyPrinter(indent=2)

fp = open("eurobarometer_merge.xml","r")
element = ET.parse(fp)

eu_pie_dict = {}
for country in element.find('Mashup'):
    for k, v in country.items():
        eu_pie_dict[v] = {}

    list09 = []
    dataset = country.findall('Dataset[@name = "Eurobarometer 2009"]')
    if v == "Belgium":
        list09 = ['null', 'null', 'null', 'null']
        third_q = dataset[0][2]
        d_k = third_q[1][0][1].text
        agree = third_q[1][1][1].text
        disagree = third_q[1][2][1].text
        list09.append(d_k)
        list09.append(agree)
        list09.append(disagree)
    elif v == "Croatia":
        list09 = ['null', 'null', 'null', 'null', 'null', 'null', 'null']
    else:
        second_q = dataset[0][1]
        not_serious = second_q[1][0][1].text
        fairly_serious = second_q[1][1][1].text
        very_serious = second_q[1][2][1].text
        dk = second_q[1][3][1].text
        if dk == '-':
            dk = 'null'
        else:
            dk = int(dk)
        third_q = dataset[0][2]
        d_k = third_q[1][0][1].text
        agree = third_q[1][1][1].text
        disagree = third_q[1][2][1].text
        list09 = [int(not_serious), int(fairly_serious), int(very_serious), dk, int(d_k), int(agree), int(disagree)]

##########

    list13 = []
    dataset = country.findall('Dataset[@name = "Eurobarometer 2013"]')
    second_q = dataset[0][1]
    not_serious = second_q[1][0][1].text
    fairly_serious = second_q[1][1][1].text
    very_serious = second_q[1][2][1].text
    dk = second_q[1][3][1].text
    if dk == '-':
        dk = 'null'
    else:
        dk = int(dk)

    third_q = dataset[0][2]
    d_k = third_q[1][0][1].text
    if d_k == '-':
        d_k = 'null'
    else:
        d_k = int(d_k)
    agree = third_q[1][1][1].text
    disagree = third_q[1][2][1].text

    list13 = [int(not_serious), int(fairly_serious), int(very_serious), dk, d_k, int(agree), int(disagree)]

############

    list19 = []
    dataset = country.findall('Dataset[@name = "Eurobarometer 2019"]')
    second_q = dataset[0][1]
    not_serious = second_q[1][0][1].text
    if not_serious == '-':
        not_serious = 'null'
    else:
        not_serious= int(not_serious)
    fairly_serious = second_q[1][1][1].text
    if fairly_serious == '-':
        fairly_serious = 'null'
    else:
        fairly_serious = int(fairly_serious)
    very_serious = second_q[1][2][1].text
    if very_serious == '-':
        very_serious = 'null'
    else:
        very_serious = int(very_serious)
    dk = second_q[1][3][1].text
    if dk == '-':
        dk = 'null'
    else:
        dk = int(dk)

    third_q = dataset[0][2]
    d_k = third_q[1][0][1].text
    if d_k == '-':
        d_k = 'null'
    else:
        d_k = int(d_k)
    agree = third_q[1][1][1].text
    if agree == '-':
        agree = 'null'
    else:
        agree = int(agree)
    disagree = third_q[1][2][1].text
    if disagree == '-':
        disagree = 'null'
    else:
        disagree = int(disagree)

    list19 = [not_serious, fairly_serious, very_serious, dk, d_k, agree, disagree]

    eu_pie_dict[v]['2009'] = list09
    eu_pie_dict[v]['2013'] = list13
    eu_pie_dict[v]['2019'] = list19

print(eu_pie_dict)


