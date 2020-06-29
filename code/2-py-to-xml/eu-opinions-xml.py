from base_file import *
from countries import *
import xml.etree.ElementTree as ET

from climate_change_project.countries import countries_dict

root = ET.Element('MashupDataset')
metadata = ET.SubElement(root, 'Metadata')
title = ET.SubElement(metadata, 'Title')
title.text = 'CCODe - European opinions on climate change'
author = ET.SubElement(metadata, 'Authors')
author.text = 'Rebecca Del Bene, Leticia S. Hamvegam M., Arianna Pizzicori'
description = ET.SubElement(metadata, 'Description')
description.text = 'This dataset contains data from the european commission related to the opinions of european citizens on climate change issues, collected in 2009, 2013 and 2019. It was created for the "Open Access and Digital Ethics" end of course project at the University of Bologna, during the a.y. 2019/2020.'
license = ET.SubElement(metadata, 'License')
license.text = 'CC-BY-SA 4.0'
version = ET.SubElement(metadata, 'Version')
version.text = 'v1.0'
mash_up = ET.SubElement(root, 'Mashup')

eu_dataset = ['Eurobarometer 2009', 'Eurobarometer 2013', 'Eurobarometer 2019']

for k, v in countries_dict.items(): 
    country = ET.SubElement(mash_up, 'Country')
    country.attrib['name'] = k
    for d in eu_dataset:
        dataset = ET.SubElement(country, 'Dataset')
        dataset.attrib['name'] = d

        if d == 'Eurobarometer 2009':
            eu2009 = eurobarometer_2009('eurobarometer_2009.xlsm')
            for c in v:
                eu2009_k = eu2009.get(c)
                if eu2009_k != None:
                    for question, answer in eu2009_k.items():
                        record = ET.SubElement(dataset, 'Record')
                        if isinstance(answer, str):
                            q = ET.SubElement(record, 'Question')
                            q.text = question
                            a = ET.SubElement(record, 'Respondents')
                            a.attrib['type'] = 'percentage'
                            a.text = answer
                        elif answer == None:
                            q = ET.SubElement(record, 'Question')
                            q.text = question
                            a = ET.SubElement(record, 'Respondents')
                            a.text = 'None'
                        else:
                            quest = ET.SubElement(record, 'Question')
                            quest.text = question
                            answ = ET.SubElement(record, 'OptionList')
                            for chiave, valore in answer.items():
                                options = ET.SubElement(answ, 'Option')
                                domanda = ET.SubElement(options, 'OptionStatement')
                                domanda.text = chiave
                                risposta = ET.SubElement(options, 'OptionRespondents')
                                risposta.attrib['type'] = 'percentage'
                                risposta.text = valore
            if len(dataset) == 0:
                country.remove(dataset)

        if d == 'Eurobarometer 2013':
            eu2013 = eurobarometer_2013('eurobarometer_2013.xls')
            for c in v:
                eu2013_k = eu2013.get(c)
                if eu2013_k != None:
                    for question1, answer1 in eu2013_k.items():
                        record = ET.SubElement(dataset, 'Record')
                        if isinstance(answer1, str):
                            q1 = ET.SubElement(record, 'Question')
                            q1.text = question1
                            a1 = ET.SubElement(record, 'Respondents')
                            a1.attrib['type'] = 'percentage'
                            a1.text = answer1
                        else:
                            quest1 = ET.SubElement(record, 'Question')
                            quest1.text = question1
                            answ1 = ET.SubElement(record, 'OptionList')
                            for k1, v1 in answer1.items():
                                options1 = ET.SubElement(answ1, 'Option')
                                domanda1 = ET.SubElement(options1, 'OptionStatement')
                                domanda1.text = k1
                                risposta1 = ET.SubElement(options1, 'OptionRespondents')
                                risposta1.attrib['type'] = 'percentage'
                                risposta1.text = v1

            if len(dataset) == 0:
                country.remove(dataset)

        if d == 'Eurobarometer 2019':
            eu2019 = eurobarometer_2019('eurobarometer_2019.xls')
            for c in v:
                eu2019_k = eu2019.get(c)
                if eu2019_k != None:
                    for question2, answer2 in eu2019_k.items():
                        record = ET.SubElement(dataset, 'Record')
                        if isinstance(answer2, str):
                            q2 = ET.SubElement(record, 'Question')
                            q2.text = question2
                            a2 = ET.SubElement(record, 'Respondents')
                            a2.attrib['type'] = 'percentage'
                            a2.text = answer2
                        else:
                            quest2 = ET.SubElement(record, 'Question')
                            quest2.text = question2
                            answ2 = ET.SubElement(record, 'OptionList')
                            for k2, v2 in answer2.items():
                                options2 = ET.SubElement(answ2, 'Option')
                                domanda2 = ET.SubElement(options2, 'OptionStatement')
                                domanda2.text = k2
                                risposta2 = ET.SubElement(options2, 'OptionRespondents')
                                risposta2.attrib['type'] = 'percentage'
                                risposta2.text = v2

            if len(dataset) == 0:
                country.remove(dataset)
    if len(country) == 0:
        mash_up.remove(country)

tree = ET.ElementTree(root)
tree.write('eu_opinions.xml')

