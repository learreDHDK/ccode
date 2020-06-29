from xml.dom import minidom

xmldoc = minidom.parse('actions_merge.xml')
countries = xmldoc.getElementsByTagName('Country')

stats = ["Footprint","GHG Emissions"]
excludedCountries = ["Azores Islands", "Czechoslovakia", "Tibet", "Tasmania", "Kosovo", "Somaliland", "Guinea-Bissau"]
years = {}

for country in countries:
    countryName = country.attributes['name'].value

    if countryName in excludedCountries:
        continue

    datasets = country.getElementsByTagName("Dataset")
    for dataset in datasets:
        datasetName = dataset.attributes['name'].value
        if datasetName not in stats:
            continue
        records = dataset.getElementsByTagName("Record")
        for record in records:
            year = str(record.getElementsByTagName("Date")[0].firstChild.nodeValue.strip()[:4])
            if datasetName == "GHG Emissions":
                value = float(record.getElementsByTagName("Entry")[0].firstChild.nodeValue)
            if datasetName == "Footprint":
                if countryName == "Nepal":
                    value2 = float(record.getElementsByTagName("Entry")[0].firstChild.nodeValue)
                else:
                    value = float(record.getElementsByTagName("Entry")[0].firstChild.nodeValue)
                    value2 = float(record.getElementsByTagName("Entry")[1].firstChild.nodeValue)

            if countryName not in years: years[countryName] = {}
            if year not in years[countryName]: years[countryName][year] = {}
            if datasetName not in years[countryName][year]: years[countryName][year][datasetName] = 0
            years[countryName][year][datasetName] = value
            if value2:
                years[countryName][year]["Biocapacity"] = value2

            if countryName not in years: years[countryName] = {}
            if year not in years[countryName]: years[countryName][year] = {}
            if datasetName not in years[countryName][year]: years[countryName][year][datasetName] = 0
            years[countryName][year][datasetName] = value

print(years)
import pprint as pp
pp.pprint(years)
