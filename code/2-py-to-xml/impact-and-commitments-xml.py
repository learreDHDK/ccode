from base_file import *
from countries import *
import xml.etree.ElementTree as ET

root = ET.Element('MashupDataset')
metadata = ET.SubElement(root, 'Metadata')
title = ET.SubElement(metadata, 'Title')
title.text = 'CCODe - Impact on climate change and commitments'
author = ET.SubElement(metadata, 'Authors')
author.text = 'Rebecca Del Bene, Leticia S. Hamvegam M., Arianna Pizzicori'
description = ET.SubElement(metadata, 'Description')
description.text = 'This dataset contains data from different organizations related to the impact of the countries all over the world on the environment and their actions undertaken to fight the climate change. It was created for the "Open Access and Digital Ethics" end of course project at the University of Bologna, during the a.y. 2019/2020.'
license = ET.SubElement(metadata, 'License')
license.text = 'CC-BY-SA 4.0'
version = ET.SubElement(metadata, 'Version')
version.text = 'v1.0'
mash_up = ET.SubElement(root, 'Mashup')

actions = ['GHG Emissions', 'Footprint', 'Paris Agreement', 'Global Funds']

for k, v in countries_dict.items():
    country = ET.SubElement(mash_up, 'Country')
    country.attrib['name'] = k
    for d in actions:
        dataset = ET.SubElement(country, 'Dataset')
        dataset.attrib['name'] = d

        if d == 'GHG Emissions':
            ghg = ghg_emissions('ghg-emissions.xml')
            for c in v:
                ghg_k = ghg.get(c)
                if ghg_k != None:
                    for year, emission in ghg_k.items():
                        record = ET.SubElement(dataset, 'Record')
                        date_ghg = ET.SubElement(record, 'Date')
                        date_ghg.attrib['type'] = 'year'
                        date_ghg.text = year
                        emis = ET.SubElement(record, 'Entry')
                        emis.attrib['unit'] = 'Kt of CO2'
                        emis.attrib['value'] = 'emission'
                        emis.text = emission
            if len(dataset) == 0:
                country.remove(dataset)

        if d == 'Footprint':
            footp = footprint('footprint.csv')
            for c in v:
                footp_k = footp.get(c)
                if footp_k != None:
                    for year, info in footp_k.items():
                        record = ET.SubElement(dataset, 'Record')
                        date_foot = ET.SubElement(record, 'Date')
                        date_foot.attrib['type'] = 'year'
                        date_foot.text = year
                        for i, j in info.items():
                            if i == 'AreaTotHA':
                                areatot = ET.SubElement(record, 'Entry')
                                areatot.attrib['unit'] = 'ha'
                                areatot.attrib['value'] = 'totalArea'
                                areatot.text = j
                            if i == 'BiocapTotGHA':
                                biocap = ET.SubElement(record, 'Entry')
                                biocap.attrib['unit'] = 'gha'
                                biocap.attrib['value'] = 'totalBiocapacity'
                                biocap.text = j
            if len(dataset) == 0:
                country.remove(dataset)

        if d == 'Paris Agreement':
            paris = paris_agreement('paris_agreement_clean.xlsx')
            for c in v:
                paris_k = paris.get(c)
                if paris_k != None:
                    for exact_date, summary in paris_k.items():
                        record = ET.SubElement(dataset, 'Record')
                        date_paris = ET.SubElement(record, 'Date')
                        date_paris.attrib['type'] = 'exactDate'
                        date_paris.text = exact_date
                        summ = ET.SubElement(record, 'Entry')
                        summ.attrib['value'] = 'summary'
                        summ.text = summary

            if len(dataset) == 0:
                country.remove(dataset)

        if d == 'Global Funds':
            funds = global_funds('global_funds.xlsx')
            for c in v:
                funds_k = funds.get(c)
                if funds_k != None:
                    for lista in funds_k:
                        record = ET.SubElement(dataset, 'Record')
                        income = ET.SubElement(record, 'Entry')
                        income.attrib['value'] = 'incomeSituation'
                        income.text = lista[0]
                        nazione = ET.SubElement(record, 'Entry')
                        nazione.attrib['value'] = 'country'
                        nazione.text = lista[1]
                        deposited = ET.SubElement(record, 'Entry')
                        deposited.attrib['unit'] = 'USD million'
                        deposited.attrib['value'] = 'deposited'
                        deposited.text = lista[2]
                        problem = ET.SubElement(record, 'Entry')
                        problem.attrib['value'] = 'problem'
                        problem.text = lista[3]
                        pledged = ET.SubElement(record, 'Entry')
                        pledged.attrib['unit'] = 'USD million'
                        pledged.attrib['value'] = 'pledged'
                        pledged.text = lista[4]
            if len(dataset) == 0:
                country.remove(dataset)

    if len(country) == 0:
        mash_up.remove(country)

tree = ET.ElementTree(root)
tree.write('impact_and_commitments.xml')