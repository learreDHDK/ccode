from xml.dom import minidom
from operator import itemgetter
from collections import Counter
import pprint
pp = pprint.PrettyPrinter(indent=2)

def getKey(item):
    return item[0]

xmldoc = minidom.parse('natural_events_merge.xml')
countries = xmldoc.getElementsByTagName('Country')

stats = ["Droughts", "Floods", "Wildfires", "Hurricanes"]
nat_events = {}

for country in countries:
    countryName = country.attributes['name'].value
    nat_events[countryName] = {}
    nat_events[countryName]["xData"]= [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    nat_events[countryName]["datasets"] = []
    datasets = country.getElementsByTagName("Dataset")
    for dataset in datasets:
        datasetName = dataset.attributes['name'].value
        if datasetName not in stats:
            continue
        dataset_dict = {}
        dataset_dict["name"] = datasetName

        records = dataset.getElementsByTagName("Record")
        record_list = []
        for record in records:
            couple_list = [int(record.getElementsByTagName("Date")[0].firstChild.nodeValue.strip()[:4]), int(record.getElementsByTagName("Entry")[0].firstChild.nodeValue)]
            record_list.append(couple_list)
        final_record_list = sorted(record_list, key=itemgetter(0))

        if datasetName == "Floods":
            tot_list = []
            last_list = []
            for couple in final_record_list:
                tot_list.append(couple[0])
            conto = dict(Counter(tot_list))
            for k, v in conto.items():
                last_list.append([k, v])
            final_record_list = sorted(last_list, key=itemgetter(0))

        idx = 0
        len_idx = len(final_record_list)
        null_list = []
        while len_idx != 1:
            difference = final_record_list[idx+1][0] - final_record_list[idx][0]
            while difference != 1:
                null_list.append([final_record_list[idx][0] + difference - 1, 'null'])
                difference -= 1
            idx += 1
            len_idx -= 1

        diff_min = final_record_list[0][0] - 1980
        while diff_min != 0:
            null_list.append([1980 + diff_min - 1, 'null'])
            diff_min -= 1

        diff_max = 2019 - final_record_list[len(final_record_list) - 1][0]
        while diff_max != 0:
            null_list.append([2019 - diff_max + 1, 'null'])
            diff_max -= 1

        for list in null_list:
            final_record_list.append(list)
        super_record_list = sorted(final_record_list, key=itemgetter(0))

        dataset_dict["data"] = []
        for lista in super_record_list:
            dataset_dict["data"].append(lista[1])
        dataset_dict["unit"] = "tot"
        dataset_dict["type"] = "line"
        dataset_dict["valueDecimals"] = 0

        nat_events[countryName]["datasets"].append(dataset_dict)

print(nat_events)
