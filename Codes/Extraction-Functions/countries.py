from base_file import *
import pycountry

def standard_name(dict_1, dict_2):
    for key in dict_1.keys():
        if key not in dict_2:
            dict_2[key] = [key]
    return dict_2

def alpha_2(dict_1, dict_2):
    for key in dict_1.keys():
        country_name = pycountry.countries.get(alpha_2=key)
        if country_name is not None:
            if country_name.name not in dict_2:
                dict_2[country_name.name] = [country_name.name, country_name.alpha_2]
            else:
                if country_name.alpha_2 not in dict_2[country_name.name]:
                    dict_2[country_name.name].append(country_name.alpha_2)
    return dict_2

def alpha_3(dict_1, dict_2):
    for key in dict_1.keys():
        country_name = pycountry.countries.get(alpha_3=key)
        if country_name is not None:
            if country_name.name not in dict_2:
                dict_2[country_name.name] = [country_name.name, country_name.alpha_3]
            else:
                if country_name.alpha_3 not in dict_2[country_name.name]:
                    dict_2[country_name.name].append(country_name.alpha_3)
    return dict_2

#funzione per togliere gli errori
def exceptions(dict, dict_exc):
    for key, value in dict_exc.items():
        for item in value:
            dict[key].append(item)
            if dict.get(item) != None:
                del dict[item]
    return dict


def final(dict):
    flooddict = standard_name(floods('floods.xlsx'), dict)
    flooddict_2 = exceptions(flooddict, {'Uzbekistan':[' Uzbekistan'], 'Bangladesh':['Bangaldesh', 'Bangledesh'], 'Bolivia':['Boliva'], 'Bosnia-Herzegovina':['Bosnia and Herzegovina', 'Bosnia and Herzogovina', 'Bosnia-Herzegovenia'], 'Burkina Faso':['Burkino Faso'], 'Cameroon':['Camaroon', 'Camaroun'], 'Colombia':['Columbia'], 'Comoros Islands':['Comoros islands'], 'Democratic Republic of the Congo':['Democratic Republic of Congo', 'DR Congo', 'Democratic Republic Congo', 'Democratic  Republic of the Congo'], 'Republic of Congo':['Congo Republic'], 'El Salvador':['El Savador'], 'Guatemala':['Guatamala', 'Gutamala'], 'India':['Inda'], 'Indonesia':['Inonesia'], 'Kazakhstan':['Kazahkstan', 'Kazahkistan'], 'Malaysia':['Malayasia'], 'Moldova':['Moldovo', 'Moldava'], 'Papua New Guinea':['Papua New Gunea'], 'Myanmar':['Myanamar', 'Burma/Myanmar', 'Burma'], 'Philippines':['Phillipines', 'Philippine', 'Philipines', 'Phillippines'], 'Serbia-Montenegro':['Serbia and Montenegro'], 'Tajikistan':['Tajikstan'], 'Thailand':['Thiland'], 'USA':['USA.'], 'United Kingdom':['Unitd Kingdom'], 'United Arab Emirates':['United Arab Emerates'], 'Uruguay':['Uruguay,'], 'Venezuela':['Venezulea'], 'Vietnam':['Viet Nam'], 'Zimbabwe':['Zimbawe']})
    hurricanesdict = standard_name(hurricanes('hurricanes.csv'), flooddict_2)
    hurricanesdict2 = exceptions(hurricanesdict, {'China': ['China 中国'], 'Spain': ['España'], 'Mozambique': ['Moçambique'], 'Mexico': ['México'], 'Dominican Republic': ['República Dominicana'], 'Samoa': ['Sāmoa'], 'USA': ['United States', 'United States of America'], 'Vietnam': ['Việt Nam'], 'India': ['भारत - India'], 'Japan': ['日本 (Japan)']})
    firedict = standard_name(global_fires('global_fires.csv'), hurricanesdict2)
    footdict = standard_name(footprint('footprint.csv'), firedict)
    footdict_2 = exceptions(footdict, {'Brunei': ['Brunei Darussalam'], 'Comoros Islands': ['Comoros'], 'Ethiopia': ['Ethiopia PDR'], 'Laos': ['Lao People\'s Democratic Republic'], 'Macedonia': ['Macedonia TFYR'], 'Sudan': ['Sudan (former)']})
    parisdict = standard_name(paris_agreement('paris_agreement_clean.xlsx'), footdict_2)
    fundsdict = standard_name(global_funds('global_funds.xlsx'), parisdict)
    fundsdict_2 = exceptions(fundsdict, {'Czech Republic':['Czech republic']})
    eu_2009 = alpha_2(eurobarometer_2009('eurobarometer_2009.xlsm'), fundsdict_2)
    eu_2013 = alpha_2(eurobarometer_2013('eurobarometer_2013.xls'), eu_2009)
    eu_2019 = alpha_2(eurobarometer_2019('eurobarometer_2019.xls'), eu_2013)
    drdict = alpha_3(droughts('droughts.dbf'), eu_2019)
    threatdict = alpha_3(threatened_species('threatened_species.xml'), drdict)
    ghgdict = alpha_3(ghg_emissions('ghg-emissions.xml'), threatdict)
    del_list = ['11th EDF intra ACP allocation', '5 EU Member States', 'APBN', 'Africa', 'Alaska', 'Antarctica', 'Antigua', 'BP Technology Ventures', 'Belgium (Brussels Capital Region)', 'Belgium (Flanders)', 'Belgium (Wallonia Regions)', 'Belgium (Wallonia)', 'Britain, Ireland', 'Bosnia', 'Canada and USA', 'Canary Islands', 'Caribbean', 'Corporacion Andina de Fomento (CAF)', 'Cocos (Keeling) Islands', 'EC Fast Start Funding', 'England', 'ENRTP programme', 'Europe', 'European Commission', 'European Development Fund', 'European Union (28)', 'Falkland Islands', 'Flanders', 'France (Paris)', 'French Guiana', 'Gaza', 'Global Goods and Challenges Programme (GPGC)', 'Guadeloupe', 'Intra Africa Caribbean and Pacific (ACP) Programme', 'Investment Income', 'Macao', 'Martinique', 'Northern Cyprus', 'Northern Ireland', 'Others', 'Petrobras - Brasil', 'Private Sector Investors (24 investors from North America, Europe and Australasia)', 'Reunion', 'RÃ©union', 'Réunion', 'Sale of CERs', 'Scotland', 'Siberia', 'Sudan and Eritrea', 'Svalbard and Jan Mayen', 'TNC', 'Texas', 'Tobago', 'Tokelau', 'Trinidad', 'United Nations Fund', 'West Bank', 'West Germany', 'World', 'الجزائر']
    for i in del_list:
        del ghgdict[i]
    final_countries = exceptions(ghgdict, {'Ivory Coast': ['"Côte dIvoire"', "Cote d'Ivoire", "CÃ´te d'Ivoire", "Côte d'Ivoire", 'CIV'], 'Bahamas': ['The Bahamas'], 'Bolivia': ['Bolivia, Plurinational State of', 'BOL'], 'Bosnia and Herzegovina': [ 'Bosnia-Herzegovina', 'Bosnia and Herzogovina', 'Bosnia-Herzegovenia'], 'British Virgin Islands': ['Virgin Islands, British', 'VGB'], 'United Kingdom': ['Britain', 'UK'], 'Brunei Darussalam': ['Brunei'], 'Cabo Verde': ['Cape Verde'], 'Comoros Islands': ['Comoros', 'COM'], 'Republic of the Congo': ['Republic of Congo','Congo Republic','Congo', 'COG'], 'Democratic Republic of the Congo': [ 'Congo, The Democratic Republic of the', 'COD', 'Congo, Democratic Republic of', 'Zaire'], 'Czech Republic': ['Czechia', 'CZ', 'CZE'], 'East Timor': ['Timor', 'Timor-Leste', 'TLS'], 'Eswatini': ['Swaziland'], 'Micronesia': ['Micronesia, Federated States of', 'FSM', 'Federated States of Micronesia'], 'Gambia':['The Gambia'], 'Iran': ['Iran, Islamic Republic of', 'IRN'], 'North Korea': [ "Korea, Democratic People's Republic of", 'PRK', '북조선'], 'South Korea': ['Korea, Rep.', 'Korea, Republic of', 'KOR', '대한민국'], 'Laos': [ "Lao People's Democratic Republic", 'LAO'], 'Libya': ['Libyan Arab Jamahiriya'], 'Moldova': ['Moldova, Republic of', 'MDA'], 'Morocco': ['Maroc'], 'Macedonia': ['North Macedonia'], 'Oman': ['سلطنة عُمان Oman'], 'Pakistan': ['پاکستان'], 'Palestine': ['Palestine, State of', 'PSE'], 'Serbia': ['Republic of Serbia'], 'Russia': ['Russian Federation', 'RUS', 'Soviet Union', 'USSR', 'Россия'], 'Saint Lucia': ['St. Lucia'], 'Saint Vincent and the Grenadines': ['Saint Vincent', 'St Vincent & the Grenadines'], 'Serbia and Montenegro': ['Serbia-Montenegro'], 'Seychelles': ['Sesel'], 'Syria': ['Syrian Arab Republic', 'SYR'], 'Taiwan': ['Taiwan, Province of China', 'TWN', '臺灣'], 'Tanzania': ['Tanzania, United Republic of', 'TZA', 'United Republic of Tanzania'], 'Thailand': ['ประเทศไทย'], 'USA': ['United States', 'United States of America'], 'Venezuela': [ 'Venezuela, Bolivarian Republic of', 'VEN'], 'Vietnam': ['Viet Nam', 'VNM'], 'Virgin Islands, U.S.': ['Virgin Islands'], 'Yemen': ['اليَمَن al-Yaman'], 'Yugoslavia': ['Yugoslav SFR']})
    #mi da problemi con il vaticano
    return final_countries

countries_dict = {}
pp.pprint(final(countries_dict))