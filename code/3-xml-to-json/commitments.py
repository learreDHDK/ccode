from base_file import *
from countries import *
from xml.dom import minidom
import pprint
pp = pprint.PrettyPrinter(indent=2)

xmldoc = minidom.parse('impact_and_commitments.xml')
countries = xmldoc.getElementsByTagName('Country')

excludedCountries = ["Azores Islands", "Czechoslovakia", "Tibet", "Tasmania", "Kosovo", "Somaliland", "Guinea-Bissau"]
commitDict = {}

for country in countries:
    countryName = country.attributes['name'].value
    if countryName in excludedCountries:
        continue
    commitDict[countryName] = {}

    datasets = country.getElementsByTagName("Dataset")
    for dataset in datasets:
        datasetName = dataset.attributes['name'].value
        if datasetName == "Paris Agreement":
            commitDict[countryName]['Paris Agreement'] = {}
            records = dataset.getElementsByTagName("Record")
            for record in records:
                dateParis = record.getElementsByTagName("Date")[0].firstChild.nodeValue
                summary = dataset.getElementsByTagName("Entry")[0].firstChild.nodeValue

                commitDict[countryName]['Paris Agreement']['Date'] = dateParis
                commitDict[countryName]['Paris Agreement']['Summary'] = summary

        if datasetName == "Global Funds":
            commitDict[countryName]['Global Funds'] = {}
            records = dataset.getElementsByTagName("Record")
            for record in records:
                entries = record.getElementsByTagName("Entry")
                for entry in entries:
                    if entry.attributes['value'].value == "incomeSituation":
                        income = entry.firstChild.nodeValue
                    if entry.attributes['value'].value == "problem":
                        problem = entry.firstChild.nodeValue
                    if entry.attributes['value'].value == "pledged":
                            pledged = entry.firstChild.nodeValue
                    if entry.attributes['value'].value == "deposited":
                        if entry.firstChild is not None:
                            deposited = entry.firstChild.nodeValue
                        else:
                            deposited = 0

                commitDict[countryName]['Global Funds']['Income situation'] = income
                commitDict[countryName]['Global Funds'][problem] = {}
                commitDict[countryName]['Global Funds'][problem]['Pledged'] = pledged
                commitDict[countryName]['Global Funds'][problem]['Deposited'] = deposited

    if commitDict[countryName] == {}:
        del commitDict[countryName]

print(commitDict)