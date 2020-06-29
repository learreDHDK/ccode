from xml.dom import minidom
from collections import Counter
import pprint
pp = pprint.PrettyPrinter(indent=2)

countriesDict = {
      "Afghanistan": [
        "AF",
        "AFG"
      ],
      "Albania": [
        "AL",
        "ALB"
      ],
      "Algeria": [
        "DZ",
        "DZA"
      ],
      "American Samoa": [
        "AS",
        "ASM"
      ],
      "Andorra": [
        "AD",
        "AND"
      ],
      "Angola": [
        "AO",
        "AGO"
      ],
      "Anguilla": [
        "AI",
        "AIA"
      ],
      "Antarctica": [
        "AQ",
        "ATA"
      ],
      "Antigua and Barbuda": [
        "AG",
        "ATG"
      ],
      "Argentina": [
        "AR",
        "ARG"
      ],
      "Armenia": [
        "AM",
        "ARM"
      ],
      "Aruba": [
        "AW",
        "ABW"
      ],
      "Australia": [
        "AU",
        "AUS"
      ],
      "Austria": [
        "AT",
        "AUT"
      ],
      "Azerbaijan": [
        "AZ",
        "AZE"
      ],
      "Bahamas": [
        "BS",
        "BHS"
      ],
      "Bahrain": [
        "BH",
        "BHR"
      ],
      "Bangladesh": [
        "BD",
        "BGD"
      ],
      "Barbados": [
        "BB",
        "BRB"
      ],
      "Belarus": [
        "BY",
        "BLR"
      ],
      "Belgium": [
        "BE",
        "BEL"
      ],
      "Belize": [
        "BZ",
        "BLZ"
      ],
      "Benin": [
        "BJ",
        "BEN"
      ],
      "Bermuda": [
        "BM",
        "BMU"
      ],
      "Bhutan": [
        "BT",
        "BTN"
      ],
      "Bolivia": [
        "BO",
        "BOL"
      ],
      "Bosnia and Herzegovina": [
        "BA",
        "BIH"
      ],
      "Botswana": [
        "BW",
        "BWA"
      ],
      "Brazil": [
        "BR",
        "BRA"
      ],
      "Brunei Darussalam": [
        "BN",
        "BRN"
      ],
      "Bulgaria": [
        "BG",
        "BGR"
      ],
      "Burkina Faso": [
        "BF",
        "BFA"
      ],
      "Burundi": [
        "BI",
        "BDI"
      ],
      "Cambodia": [
        "KH",
        "KHM"
      ],
      "Cameroon": [
        "CM",
        "CMR"
      ],
      "Canada": [
        "CA",
        "CAN"
      ],
      "Cabo Verde": [
        "CV",
        "CPV"
      ],
      "Cayman Islands": [
        "KY",
        "CYM"
      ],
      "Central African Republic": [
        "CF",
        "CAF"
      ],
      "Chad": [
        "TD",
        "TCD"
      ],
      "Chile": [
        "CL",
        "CHL"
      ],
      "China": [
        "CN",
        "CHN"
      ],
      "Colombia": [
        "CO",
        "COL"
      ],
      "Comoros Islands": [
        "KM",
        "COM"
      ],
      "Republic of the Congo": [
        "CG",
        "COG"
      ],
      "Democratic Republic of the Congo": [
        "CD",
        "COD"
      ],
      "Cook Islands": [
        "CK",
        "COK"
      ],
      "Costa Rica": [
        "CR",
        "CRI"
      ],
      "Ivory Coast": [
        "CI",
        "CIV"
      ],
      "Croatia": [
        "HR",
        "HRV"
      ],
      "Cuba": [
        "CU",
        "CUB"
      ],
      "Cyprus": [
        "CY",
        "CYP"
      ],
      "Czech Republic": [
        "CZ",
        "CZE"
      ],
      "Denmark": [
        "DK",
        "DNK"
      ],
      "Djibouti": [
        "DJ",
        "DJI"
      ],
      "Dominica": [
        "DM",
        "DMA"
      ],
      "Dominican Republic": [
        "DO",
        "DOM"
      ],
      "Ecuador": [
        "EC",
        "ECU"
      ],
      "Egypt": [
        "EG",
        "EGY"
      ],
      "El Salvador": [
        "SV",
        "SLV"
      ],
      "Equatorial Guinea": [
        "GQ",
        "GNQ"
      ],
      "Eritrea": [
        "ER",
        "ERI"
      ],
      "Estonia": [
        "EE",
        "EST"
      ],
      "Ethiopia": [
        "ET",
        "ETH"
      ],
      "Fiji": [
        "FJ",
        "FJI"
      ],
      "Finland": [
        "FI",
        "FIN"
      ],
      "France": [
        "FR",
        "FRA"
      ],
      "French Polynesia": [
        "PF",
        "PYF"
      ],
      "Gabon": [
        "GA",
        "GAB"
      ],
      "Gambia": [
        "GM",
        "GMB"
      ],
      "Georgia": [
        "GE",
        "GEO"
      ],
      "Germany": [
        "DE",
        "DEU"
      ],
      "Ghana": [
        "GH",
        "GHA"
      ],
      "Gibraltar": [
        "GI",
        "GIB"
      ],
      "Greece": [
        "GR",
        "GRC"
      ],
      "Greenland": [
        "GL",
        "GRL"
      ],
      "Grenada": [
        "GD",
        "GRD"
      ],
      "Guam": [
        "GU",
        "GUM"
      ],
      "Guatemala": [
        "GT",
        "GTM"
      ],
      "Guernsey": [
        "GG",
        "GGY"
      ],
      "Guinea": [
        "GN",
        "GIN"
      ],
      "Guinea Bissau": [
        "GW",
        "GNB"
      ],
      "Guyana": [
        "GY",
        "GUY"
      ],
      "Haiti": [
        "HT",
        "HTI"
      ],
      "Holy See (Vatican City State)": [
        "VA",
        "VAT"
      ],
      "Honduras": [
        "HN",
        "HND"
      ],
      "Hong Kong": [
        "HK",
        "HKG"
      ],
      "Hungary": [
        "HU",
        "HUN"
      ],
      "Iceland": [
        "IS",
        "ISL"
      ],
      "India": [
        "IN",
        "IND"
      ],
      "Indonesia": [
        "ID",
        "IDN"
      ],
      "Iran": [
        "IR",
        "IRN"
      ],
      "Iraq": [
        "IQ",
        "IRQ"
      ],
      "Ireland": [
        "IE",
        "IRL"
      ],
      "Israel": [
        "IL",
        "ISR"
      ],
      "Italy": [
        "IT",
        "ITA"
      ],
      "Jamaica": [
        "JM",
        "JAM"
      ],
      "Japan": [
        "JP",
        "JPN"
      ],
      "Jordan": [
        "JO",
        "JOR"
      ],
      "Kazakhstan": [
        "KZ",
        "KAZ"
      ],
      "Kenya": [
        "KE",
        "KEN"
      ],
      "Kiribati": [
        "KI",
        "KIR"
      ],
      "South Korea": [
        "KR",
        "KOR"
      ],
      "Kuwait": [
        "KW",
        "KWT"
      ],
      "Kyrgyzstan": [
        "KG",
        "KGZ"
      ],
      "Laos": [
        "LA",
        "LAO"
      ],
      "Latvia": [
        "LV",
        "LVA"
      ],
      "Lebanon": [
        "LB",
        "LBN"
      ],
      "Lesotho": [
        "LS",
        "LSO"
      ],
      "Liberia": [
        "LR",
        "LBR"
      ],
      "Libya": [
        "LY",
        "LBY"
      ],
      "Liechtenstein": [
        "LI",
        "LIE"
      ],
      "Lithuania": [
        "LT",
        "LTU"
      ],
      "Luxembourg": [
        "LU",
        "LUX"
      ],
      "Macedonia": [
        "MK",
        "MKD"
      ],
      "Madagascar": [
        "MG",
        "MDG"
      ],
      "Malawi": [
        "MW",
        "MWI"
      ],
      "Malaysia": [
        "MY",
        "MYS"
      ],
      "Maldives": [
        "MV",
        "MDV"
      ],
      "Mali": [
        "ML",
        "MLI"
      ],
      "Malta": [
        "MT",
        "MLT"
      ],
      "Marshall Islands": [
        "MH",
        "MHL"
      ],
      "Mauritania": [
        "MR",
        "MRT"
      ],
      "Mauritius": [
        "MU",
        "MUS"
      ],
      "Mexico": [
        "MX",
        "MEX"
      ],
      "Micronesia": [
        "FM",
        "FSM"
      ],
      "Moldova": [
        "MD",
        "MDA"
      ],
      "Monaco": [
        "MC",
        "MCO"
      ],
      "Mongolia": [
        "MN",
        "MNG"
      ],
      "Montenegro": [
        "ME",
        "MNE"
      ],
      "Montserrat": [
        "MS",
        "MSR"
      ],
      "Morocco": [
        "MA",
        "MAR"
      ],
      "Mozambique": [
        "MZ",
        "MOZ"
      ],
      "Myanmar": [
        "MM",
        "MMR"
      ],
      "Namibia": [
        "NA",
        "NAM"
      ],
      "Nauru": [
        "NR",
        "NRU"
      ],
      "Nepal": [
        "NP",
        "NPL"
      ],
      "Netherlands": [
        "NL",
        "NLD"
      ],
      "New Caledonia": [
        "NC",
        "NCL"
      ],
      "New Zealand": [
        "NZ",
        "NZL"
      ],
      "Nicaragua": [
        "NI",
        "NIC"
      ],
      "Niger": [
        "NE",
        "NER"
      ],
      "Nigeria": [
        "NG",
        "NGA"
      ],
      "Niue": [
        "NU",
        "NIU"
      ],
      "North Korea": [
        "KP",
        "PRK"
      ],
      "Norway": [
        "NO",
        "NOR"
      ],
      "Oman": [
        "OM",
        "OMN"
      ],
      "Pakistan": [
        "PK",
        "PAK"
      ],
      "Palau": [
        "PW",
        "PLW"
      ],
      "Palestine": [
        "PS",
        "PSE"
      ],
      "Panama": [
        "PA",
        "PAN"
      ],
      "Papua New Guinea": [
        "PG",
        "PNG"
      ],
      "Paraguay": [
        "PY",
        "PRY"
      ],
      "Peru": [
        "PE",
        "PER"
      ],
      "Philippines": [
        "PH",
        "PHL"
      ],
      "Poland": [
        "PL",
        "POL"
      ],
      "Portugal": [
        "PT",
        "PRT"
      ],
      "Puerto Rico": [
        "PR",
        "PRI"
      ],
      "Qatar": [
        "QA",
        "QAT"
      ],
      "Romania": [
        "RO",
        "ROU"
      ],
      "Russia": [
        "RU",
        "RUS"
      ],
      "Rwanda": [
        "RW",
        "RWA"
      ],
      "Saint Kitts and Nevis": [
        "KN",
        "KNA"
      ],
      "Saint Lucia": [
        "LC",
        "LCA"
      ],
      "Saint Vincent and the Grenadines": [
        "VC",
        "VCT"
      ],
      "Samoa": [
        "WS",
        "WSM"
      ],
      "San Marino": [
        "SM",
        "SMR"
      ],
      "Sao Tome and Principe": [
        "ST",
        "STP"
      ],
      "Saudi Arabia": [
        "SA",
        "SAU"
      ],
      "Senegal": [
        "SN",
        "SEN"
      ],
      "Serbia": [
        "RS",
        "SRB"
      ],
      "Serbia and Montenegro": [
        "CS",
        "SCG"
      ],
      "Seychelles": [
        "SC",
        "SYC"
      ],
      "Sierra Leone": [
        "SL",
        "SLE"
      ],
      "Singapore": [
        "SG",
        "SGP"
      ],
      "Slovakia": [
        "SK",
        "SVK"
      ],
      "Slovenia": [
        "SI",
        "SVN"
      ],
      "Solomon Islands": [
        "SB",
        "SLB"
      ],
      "Somalia": [
        "SO",
        "SOM"
      ],
      "South Africa": [
        "ZA",
        "ZAF"
      ],
      "South Sudan": [
        "SS",
        "SSD"
      ],
      "Spain": [
        "ES",
        "ESP"
      ],
      "Sri Lanka": [
        "LK",
        "LKA"
      ],
      "Sudan": [
        "SD",
        "SDN"
      ],
      "Suriname": [
        "SR",
        "SUR"
      ],
      "Eswatini": [
        "SZ",
        "SWZ"
      ],
      "Sweden": [
        "SE",
        "SWE"
      ],
      "Switzerland": [
        "CH",
        "CHE"
      ],
      "Syria": [
        "SY",
        "SYR"
      ],
      "Taiwan": [
        "TW",
        "TWN"
      ],
      "Tajikistan": [
        "TJ",
        "TJK"
      ],
      "Tanzania": [
        "TZ",
        "TZA"
      ],
      "Thailand": [
        "TH",
        "THA"
      ],
      "East Timor": [
        "TL",
        "TLS"
      ],
      "Tibet": [
        "00",
        "TIB"
      ],
      "Togo": [
        "TG",
        "TGO"
      ],
      "Tonga": [
        "TO",
        "TON"
      ],
      "Trinidad and Tobago": [
        "TT",
        "TTO"
      ],
      "Tunisia": [
        "TN",
        "TUN"
      ],
      "Turkey": [
        "TR",
        "TUR"
      ],
      "Turkmenistan": [
        "TM",
        "TKM"
      ],
      "Turks and Caicos Islands": [
        "TC",
        "TCA"
      ],
      "Tuvalu": [
        "TV",
        "TUV"
      ],
      "Uganda": [
        "UG",
        "UGA"
      ],
      "Ukraine": [
        "UA",
        "UKR"
      ],
      "United Arab Emirates": [
        "AE",
        "ARE"
      ],
      "United Kingdom": [
        "GB",
        "GBR"
      ],
      "USA": [
        "US",
        "USA"
      ],
      "Uruguay": [
        "UY",
        "URY"
      ],
      "Uzbekistan": [
        "UZ",
        "UZB"
      ],
      "Vanuatu": [
        "VU",
        "VUT"
      ],
      "Venezuela": [
        "VE",
        "VEN"
      ],
      "Vietnam": [
        "VN",
        "VNM"
      ],
      "British Virgin Islands": [
        "VG",
        "VGB"
      ],
      "Virgin Islands, U.S.": [
        "VI",
        "VIR"
      ],
      "Western Sahara": [
        "EH",
        "ESH"
      ],
      "Yemen": [
        "YE",
        "YEM"
      ],
      "Yugoslavia": [
        "YU",
        "YUG"
      ],
      "Zambia": [
        "ZM",
        "ZMB"
      ],
      "Zimbabwe": [
        "ZW",
        "ZWE"
      ]
    }




xmldoc = minidom.parse('natural_events.xml')
countries = xmldoc.getElementsByTagName('Country')

stats = ["Droughts", "Floods", "Wildfires", "Hurricanes"]
excludedCountries = ["Azores Islands", "Czechoslovakia", "Tibet", "Tasmania", "Kosovo", "Somaliland", "Guinea-Bissau"]
years = {}

for country in countries:
    countryName = country.attributes['name'].value

    if countryName in excludedCountries:
        continue

    alpha3 = countriesDict[countryName][1]
    datasets = country.getElementsByTagName("Dataset")
    for dataset in datasets:
        datasetName = dataset.attributes['name'].value
        if datasetName not in stats:
            continue
        if datasetName == "Floods":
            records = dataset.getElementsByTagName("Record")
            date_list = []
            for record in records:
                year_flood = int(record.getElementsByTagName("Date")[0].firstChild.nodeValue.strip()[:4])
                year_flood = str(year_flood)
                date_list.append(year_flood)
            conto = dict(Counter(date_list))
            for year, tot in conto.items():
                if year not in years: years[year] = {}
                if alpha3 not in years[year]: years[year][alpha3] = {}
                if datasetName not in years[year][alpha3]: years[year][alpha3][datasetName] = 0
                years[year][alpha3][datasetName] = tot

        else:
            records = dataset.getElementsByTagName("Record")
            for record in records:
                year = int(record.getElementsByTagName("Date")[0].firstChild.nodeValue.strip()[:4])
                year = str(year)
                value = int(record.getElementsByTagName("Entry")[0].firstChild.nodeValue)

                if year not in years: years[year] = {}
                if alpha3 not in years[year]: years[year][alpha3] = {}
                if datasetName not in years[year][alpha3]: years[year][alpha3][datasetName] = 0
                years[year][alpha3][datasetName] += value

dr_idx = 0
flood_idx = 0
fire_idx = 0
hurr_idx = 0

for anno, data in years.items():
    for a3, sets in data.items():
        for set, t in sets.items():
            if set == "Droughts":
                if t > dr_idx:
                    dr_idx = t
            if set == "Floods":
                if t > flood_idx:
                    flood_idx = t
            if set == "Wildfires":
                if t > fire_idx:
                    fire_idx = t
            if set == "Hurricanes":
                if t > hurr_idx:
                    hurr_idx = t

for anno, data in years.items():
    for a3, sets in data.items():
        for set, t in sets.items():
            if set == "Droughts":
                if t == dr_idx:
                    t = 200
                    years[anno][a3][set] = t
                else:
                    t = (t * 200) // dr_idx
                    years[anno][a3][set] = t
            if set == "Floods":
                if t == flood_idx:
                    t = 200
                    years[anno][a3][set] = t
                else:
                    t = (t * 200) // flood_idx
                    years[anno][a3][set] = t
            if set == "Wildfires":
                if t == fire_idx:
                    t = 200
                    years[anno][a3][set] = t
                else:
                    t = (t * 200) // fire_idx
                    years[anno][a3][set] = t
            if set == "Hurricanes":
                if t == hurr_idx:
                    t = 200
                    years[anno][a3][set] = t
                else:
                    t = (t * 200) // hurr_idx
                    years[anno][a3][set] = t

print(years)



