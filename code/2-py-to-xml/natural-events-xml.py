from base_file import *
from countries import *
import xml.etree.ElementTree as ET

root = ET.Element('MashupDataset')
metadata = ET.SubElement(root, 'Metadata')
title = ET.SubElement(metadata, 'Title')
title.text = 'CCODe - Natural Events'
author = ET.SubElement(metadata, 'Authors')
author.text = 'Rebecca Del Bene, Leticia S. Hamvegam M., Arianna Pizzicori'
description = ET.SubElement(metadata, 'Description')
description.text = 'This dataset contains data from different organizations related to the following natural events: precipitation, temperature, sea ice, floods, droughts, wildfires and threatened species. For precipitation, temperature and sea ice the data were collected on a global scale; while for droughts, floods, wildfires and threatened species, data were collected on a country based scale. The temporal coverages of the datasets are different; the majority of them collected data from 1980 to 2019, but there are some cases that bring back to 1880 and some others that end at the beginning of the XXI century. It was created for the "Open Access and Digital Ethics" end of course project at the University of Bologna, during the a.y. 2019/2020.'
license = ET.SubElement(metadata, 'License')
license.text = 'CC-BY-SA 4.0'
version = ET.SubElement(metadata, 'Version')
version.text = 'v1.0'
mash_up = ET.SubElement(root, 'Mashup')

nature_with_country = ['Droughts', 'Floods', 'Hurricanes', 'Wildfires', 'Threatened Species']

for k, v in countries_dict.items():
    country = ET.SubElement(mash_up, 'Country')
    country.attrib['name'] = k
    for d in nature_with_country:
        dataset = ET.SubElement(country, 'Dataset')
        dataset.attrib['name'] = d

        # DROUGHTS
        if d == 'Droughts':
            dr = droughts('droughts.dbf')
            d_list = []
            d_dict = {}
            for c in v:
                dr_k = dr.get(c)
                if dr_k != None:
                    d_list.append(dr_k)
            if len(d_list) != 0:
                dizionario = d_list[0]
                for e, f in dizionario.items():
                    d_dict[e] = f
                if len(d_list) > 1:
                    idx = len(d_list) - 1
                    while idx != 0:
                        for chiave, valore in d_list[idx].items():
                            if d_dict.get(chiave) == None:
                                d_dict[chiave] = valore
                            else:
                                d_dict[chiave] += valore
                        idx -= 1

            for year, num in d_dict.items():
                record = ET.SubElement(dataset, 'Record')
                date = ET.SubElement(record, 'Date')
                date.attrib['type'] = 'year'
                date.text = year
                entry = ET.SubElement(record, 'Entry')
                entry.attrib['type'] = 'number'
                entry.attrib['value'] = 'total'
                entry.text = str(num)
            if len(dataset) == 0:
                country.remove(dataset)


        # FLOODS
        if d == 'Floods':
            flood = floods('floods.xlsx')
            for c in v:
                flood_k = flood.get(c)
                if flood_k != None:
                    for exact_date, info in flood_k.items():
                        record = ET.SubElement(dataset, 'Record')
                        date_flood = ET.SubElement(record, 'Date')
                        date_flood.attrib['type'] = 'exactDate'
                        date_flood.text = exact_date
                        for i, j in info.items():
                            if i == 'dead':
                                dead = ET.SubElement(record, 'Entry')
                                dead.attrib['type'] = 'people'
                                dead.attrib['value'] = 'deaths'
                                dead.text = j
                            if i == 'displaced':
                                displaced = ET.SubElement(record, 'Entry')
                                displaced.attrib['type'] = 'people'
                                displaced.attrib['value'] = 'displaced'
                                displaced.text = j
                            if i == 'duration':
                                duration = ET.SubElement(record, 'Entry')
                                duration.attrib['type'] = 'days'
                                duration.attrib['value'] = 'duration'
                                duration.text = j
                            if i == 'main_cause':
                                main_cause = ET.SubElement(record, 'Entry')
                                main_cause.attrib['type'] = 'string'
                                main_cause.attrib['value'] = 'mainCause'
                                main_cause.text = j
                            if i == 'severity':
                                severity = ET.SubElement(record, 'Entry')
                                severity.attrib['type'] = 'number'
                                severity.attrib['value'] = 'severity'
                                severity.text = j
            if len(dataset) == 0:
                country.remove(dataset)


        #HURRICANES
        if d == 'Hurricanes':
            hurr = hurricanes('hurricanes.csv')
            k_list = []
            k_dict = {}
            for c in v:
                hurr_k = hurr.get(c)
                if hurr_k != None:
                    k_list.append(hurr_k)
            if len(k_list) != 0:
                dizionario = k_list[0]
                for e, f in dizionario.items():
                    k_dict[e] = f
                if len(k_list) > 1:
                    idx = len(k_list) - 1
                    while idx != 0:
                        for chiave, valore in k_list[idx].items():
                            if k_dict.get(chiave) == None:
                                k_dict[chiave] = valore
                            else:
                                k_dict[chiave] += valore
                        idx -= 1

            for year, num in k_dict.items():
                record = ET.SubElement(dataset, 'Record')
                date = ET.SubElement(record, 'Date')
                date.attrib['type'] = 'year'
                date.text = year
                value = ET.SubElement(record, 'Entry')
                value.attrib['type'] = 'number'
                value.attrib['value'] = 'total'
                value.text = str(num)

            if len(dataset) == 0:
                country.remove(dataset)

        # WILDFIRES
        if d == 'Wildfires':
            fire = global_fires('global_fires.csv')
            for c in v:
                fire_k = fire.get(c)
                if fire_k != None:
                    for year, num in fire_k.items():
                        record = ET.SubElement(dataset, 'Record')
                        date = ET.SubElement(record, 'Date')
                        date.attrib['type'] = 'year'
                        date.text = year
                        value = ET.SubElement(record, 'Entry')
                        value.attrib['type'] = 'number'
                        value.attrib['value'] = 'total'
                        value.text = num
            if len(dataset) == 0:
                country.remove(dataset)

        # THREATENED SPECIES
        if d == 'Threatened Species':
            threat_s = threatened_species('threatened_species.xml')
            for c in v:
                threat_k = threat_s.get(c)
                if threat_k != None:
                    for t in threat_k:
                        record = ET.SubElement(dataset, 'Record')
                        for inf, numb in t.items():
                            if inf == 'TOT_KNOWN':
                                totk = ET.SubElement(record, 'Entry')
                                totk.attrib['type'] = 'number'
                                totk.attrib['value'] = 'totalKnown'
                                totk.text = numb
                            elif inf == 'THREATENED':
                                thr = ET.SubElement(record, 'Entry')
                                thr.attrib['type'] = 'number'
                                thr.attrib['value'] = 'threatened'
                                thr.text = numb
                            elif inf == 'PERCENT_THREATENED':
                                percthr = ET.SubElement(record, 'Entry')
                                percthr.attrib['type'] = 'percentage'
                                percthr.attrib['value'] = 'percentThreatened'
                                percthr.text = numb
                            else:
                                dataset.remove(record)
            if len(dataset) == 0:
                country.remove(dataset)


nature_no_country = ['Temperature', 'Precipitation', 'Sea Ice']
world = ET.SubElement(mash_up, 'World')
for d in nature_no_country:
    dataset = ET.SubElement(world, 'Dataset')
    dataset.attrib['name'] = d

    if d == 'Temperature':
        temp = temperature('temperature.json')
        for year, anom in temp.items():
            record = ET.SubElement(dataset, 'Record')
            date = ET.SubElement(record, 'Date')
            date.attrib['type'] = 'year'
            date.text = year
            value = ET.SubElement(record, 'Entry')
            value.attrib['type'] = 'number'
            value.attrib['value'] = 'anomaly'
            value.text = anom

    if d == 'Precipitation':
        prec = precipitation('precipitation.csv')
        for year, anom in prec.items():
            record = ET.SubElement(dataset, 'Record')
            date = ET.SubElement(record, 'Date')
            date.attrib['type'] = 'year'
            date.text = year
            value = ET.SubElement(record, 'Entry')
            value.attrib['type'] = 'number'
            value.attrib['value'] = 'anomaly'
            value.text = anom

    if d == 'Sea Ice':
        sea_ice = seaice('seaice.xml')
        for year, anom in sea_ice.items():
            record = ET.SubElement(dataset, 'Record')
            date = ET.SubElement(record, 'Date')
            date.attrib['type'] = 'year'
            date.text = year
            value = ET.SubElement(record, 'Entry')
            value.attrib['type'] = 'number'
            value.attrib['value'] = 'anomaly'
            value.text = anom

    if len(country) == 0:
        mash_up.remove(country)

tree = ET.ElementTree(root)
tree.write('natural_events.xml')








