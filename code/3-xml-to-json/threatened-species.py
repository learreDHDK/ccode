from base_file import *
from countries import *
from xml.dom import minidom
import pprint
pp = pprint.PrettyPrinter(indent=2)

xmldoc = minidom.parse('natural_events.xml')
countries = xmldoc.getElementsByTagName('Country')

excludedCountries = ["Azores Islands", "Czechoslovakia", "Tibet", "Tasmania", "Kosovo", "Somaliland", "Guinea-Bissau"]
threatDict = {}

for country in countries:
    countryName = country.attributes['name'].value
    if countryName in excludedCountries:
        continue
    threatDict[countryName] = {}

    datasets = country.getElementsByTagName("Dataset")
    for dataset in datasets:
        datasetName = dataset.attributes['name'].value
        if datasetName == "Threatened Species":
            records = dataset.getElementsByTagName("Record")
            for record in records:
                entries = dataset.getElementsByTagName("Entry")
                for entry in entries:
                    if entry.attributes['value'].value == "totalKnown":
                        totK = entry.firstChild.nodeValue
                    if entry.attributes['value'].value == "threatened":
                        threat = entry.firstChild.nodeValue
                    if entry.attributes['value'].value == "percentThreatened":
                        percThreat = entry.firstChild.nodeValue
                        roundPerc = int(round(float(percThreat), 0))

                threatDict[countryName]["Total known"] = int(totK)
                threatDict[countryName]["Threatened"] = int(threat)
                threatDict[countryName]["Percentage threatened"] = roundPerc

    if threatDict[countryName] == {}:
        del threatDict[countryName]

print(threatDict)