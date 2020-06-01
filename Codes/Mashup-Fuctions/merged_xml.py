# MANCANTI: string droughts, delete country with no data, decidere tag

from base_file import *
from countries import *
import xml.etree.ElementTree as ET

root = ET.Element('MashupDataset')
metadata = ET.SubElement(root, 'Metadata')
mash_up = ET.SubElement(root, 'Mashup')

nature_with_country = ['Droughts', 'Floods', 'Hurricanes', 'Wildfires', 'Threatened Species']

for k, v in countries_dict.items():
    country = ET.SubElement(mash_up, 'Country')
    country.attrib['name'] = k
    for d in nature_with_country:
        dataset = ET.SubElement(country, 'Dataset')
        dataset.attrib['name'] = d

        # OK STRINGHE
        # DROUGHTS
        if d == 'Droughts':
            dr = droughts('droughts.dbf')
            for c in v:
                dr_k = dr.get(c)
                if dr_k != None:
                    for year, num in dr_k.items():
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
        # for c, y in droughts('droughts.dbf').items():


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
                                severity.attrib['type'] = 'number' # number?
                                severity.attrib['value'] = 'severity'
                                severity.text = j
            if len(dataset) == 0:
                country.remove(dataset)

        #HURRICANES
        if d == 'Hurricanes':
            hurr = hurricanes('hurricanes.csv')
            for c in v:
                hurr_k = hurr.get(c)
                if hurr_k != None:
                    for year, num in hurr_k.items():
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

        #WILDFIRES
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
            for c in v: # ogni elemento nella lista di paesi (che è il valore) del countries dict
                threat_k = threat_s.get(c) # le chiavi in threat sp che hanno un country associato in countries dict
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

    # OK STRINGHE
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

    # OK STRINGHE
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

    # OK STRINGHE
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
tree.write('natural_events_merge.xml')






