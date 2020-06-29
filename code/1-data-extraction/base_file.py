from dbfread import DBF
from collections import Counter
import xlrd
import datetime
import csv
import json
import xml.etree.ElementTree as ET
import math
import pprint
pp = pprint.PrettyPrinter(indent=2)

def droughts(dataset):
    drought_dict = {}
    table = DBF(dataset)
    iso3_list = []

    for record in table:
        if record['iso3'] not in iso3_list:
            iso3_list.append(record['iso3'])

    for record in table:
        if record['iso3'] not in drought_dict:
            drought_dict[str(record['iso3'])] = [str(record['year'])]
        else:
            drought_dict[str(record['iso3'])].append(str(record['year']))

    for k, y in drought_dict.items():
        conto_dict = dict(Counter(y))
        for y, c in conto_dict.items():
            c = str(c)
            drought_dict[k] = conto_dict

    return drought_dict

#######################################################################################

def floods(dataset):
    xl_workbook = xlrd.open_workbook(dataset)
    floods_dict = {}
    xl_sheet = xl_workbook.sheet_by_index(0)
    num_cols = xl_sheet.ncols
    workbook_datemode = xl_workbook.datemode
    for row_idx in range(1, xl_sheet.nrows):
        for col_idx in range(0, num_cols):
            if col_idx == 2:
                country_raw = xl_sheet.cell(row_idx, col_idx).value
                country_space = country_raw.replace(u'\xa0', u' ')
                country = country_space.strip()
            if col_idx == 3:
                other_country = xl_sheet.cell(row_idx, col_idx).value
            if col_idx == 7:
                began_raw = xl_sheet.cell(row_idx, col_idx).value
                year, month, day, hour, minute, second = xlrd.xldate_as_tuple(began_raw, workbook_datemode)
                began_unform = datetime.datetime(year, month, day, hour, minute, second)
            if col_idx == 8:
                ended_raw = xl_sheet.cell(row_idx, col_idx).value
                year, month, day, hour, minute, second = xlrd.xldate_as_tuple(ended_raw, workbook_datemode)
                ended_unform = datetime.datetime(year, month, day, hour, minute, second)
            if col_idx == 10:
                dead = str(int(xl_sheet.cell(row_idx, col_idx).value))
            if col_idx == 11:
                displaced = str(int(xl_sheet.cell(row_idx, col_idx).value))
            if col_idx == 12:
                cause = xl_sheet.cell(row_idx, col_idx).value
            if col_idx == 13:
                severity = str(xl_sheet.cell(row_idx, col_idx).value)
        duration = str(abs((ended_unform - began_unform).days))
        began = began_unform.strftime("%Y/%m/%d")

        if country in floods_dict:
            if began in floods_dict:
                floods_dict[country][began]['duration'] = duration
                floods_dict[country][began]['dead'] = dead
                floods_dict[country][began]['displaced'] = displaced
                floods_dict[country][began]['main_cause'] = cause
                floods_dict[country][began]['severity'] = severity
            else:
                if '2020' not in began:
                    floods_dict[country][began] = {}
                    floods_dict[country][began]['duration'] = duration
                    floods_dict[country][began]['dead'] = dead
                    floods_dict[country][began]['displaced'] = displaced
                    floods_dict[country][began]['main_cause'] = cause
                    floods_dict[country][began]['severity'] = severity
        else:
            if '2020' not in began:
                floods_dict[country] = {}
                floods_dict[country][began] = {}
                floods_dict[country][began]['duration'] = duration
                floods_dict[country][began]['dead'] = dead
                floods_dict[country][began]['displaced'] = displaced
                floods_dict[country][began]['main_cause'] = cause
                floods_dict[country][began]['severity'] = severity

        if other_country in floods_dict:
            if other_country != 0.0:
                if other_country != '':
                    if began in floods_dict:
                        floods_dict[other_country][began]['duration'] = duration
                        floods_dict[other_country][began]['dead'] = dead
                        floods_dict[other_country][began]['displaced'] = displaced
                        floods_dict[other_country][began]['main_cause'] = cause
                        floods_dict[other_country][began]['severity'] = severity
                    else:
                        if '2020' not in began:
                            floods_dict[other_country][began] = {}
                            floods_dict[other_country][began]['duration'] = duration
                            floods_dict[other_country][began]['dead'] = dead
                            floods_dict[other_country][began]['displaced'] = displaced
                            floods_dict[other_country][began]['main_cause'] = cause
                            floods_dict[other_country][began]['severity'] = severity
        else:
            if other_country != 0.0:
                if other_country != '':
                    if '2020' not in began:
                        floods_dict[other_country] = {}
                        floods_dict[other_country][began] = {}
                        floods_dict[other_country][began]['duration'] = duration
                        floods_dict[other_country][began]['dead'] = dead
                        floods_dict[other_country][began]['displaced'] = displaced
                        floods_dict[other_country][began]['main_cause'] = cause
                        floods_dict[other_country][began]['severity'] = severity

    return floods_dict

#######################################################################################

def hurricanes(dataset):
    with open(dataset, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        initial_list = list()
        hurricanes_dict = {}
        for row in csv_reader:
            initial_list.append(row)
        index=0
        index2=len(initial_list)
        while index2 != 0:
            item1 = initial_list[index]
            item2 = initial_list[index+1]
            for i in item2:
                if ' addr:country' in i:
                    if i[15:] not in hurricanes_dict:
                        hurricanes_dict[i[15:]] = {}
                        hurricanes_dict[i[15:]][item1[1][1:]] = 1
                    else:
                        if item1[1][1:] not in hurricanes_dict[i[15:]]:
                            hurricanes_dict[i[15:]][item1[1][1:]] = 1
                        else:
                            hurricanes_dict[i[15:]][item1[1][1:]] += 1
            index += 2
            index2 -= 2
    return hurricanes_dict

#######################################################################################

def global_fires(fire):
    with open(fire) as csv_file:
        next(csv_file, None)
        csv_reader = csv.reader(csv_file, delimiter=',')
        dict_fire = {}
        year_list = []

        for row in csv_reader:
            key = row.pop(0)
            dict_fire[key] = row

        year_list.extend(dict_fire['area'])
        year_list.pop()
        del dict_fire ['area']

        for k, v in dict_fire.items():
            v.pop()
            d = dict(zip(year_list, v))
            dict_fire[k] = d

    return dict_fire

#######################################################################################

def temperature(dataset):
    with open(dataset) as csv_file:
        data = json.load(csv_file)
        temperature_data= data['data']

    return temperature_data

#######################################################################################

def threatened_species(dataset):
    global species_dict, endg_dict, cri_dict, vul_dict, threat_dict, country, final, tot_dict
    tree = ET.parse(dataset)
    root = tree.getroot()
    list_dict_attributes = []
    start_tag = root[1]
    for child in start_tag:
        for subchild in child:
            for tag in subchild:
                for value in tag.iter():
                    list_dict_attributes.append(value.attrib)
    del list_dict_attributes[-9:]

    for attribute_dicts in list_dict_attributes:
        for k, v in attribute_dicts.items():
            if k == 'value' and v == 'I' or v == 'E':
                list_dict_attributes.remove(attribute_dicts)
    while {} in list_dict_attributes:
        list_dict_attributes.remove({})

    list_series_file = [list_dict_attributes[i:i + 6] for i in range(0, len(list_dict_attributes),6)]

    list_all_country_series = []
    countries = ["AUS", "AUT", "BEL", "CAN", "CZE", "DNK", "FIN", "FRA", "DEU", "GRC", "HUN", "ISL", "IRL", "ITA",
                 "JPN", "KOR", "LUX", "MEX", "NLD", "NZL", "NOR", "POL", "PRT", "SVK", "ESP", "SWE", "CHE", "TUR",
                 "GBR", "USA", "CHL", "COL", "EST", "LVA", "BRA", "ISR", "RUS", "SVN", "CRI", "LTU"]
    species_dict = {}
    for country in countries:
        for list_one_series in list_series_file:
            for one_attribute_dict in list_one_series:
                for b in one_attribute_dict.values():
                    if b == country and one_attribute_dict in list_one_series:
                        list_all_country_series.append(list_one_series)

        list_tot = []
        list_endangered = []
        list_critical = []
        list_vulnerable = []
        list_threatened = []

        for six_attribute_country_list in list_all_country_series:
            for series_attribute_dict in six_attribute_country_list:
                for c, d in series_attribute_dict.items():
                    if c == 'value' and d == 'TOT_KNOWN' or d == 'TOT_KNOWN_IND':
                        list_tot.append(six_attribute_country_list)
                    elif c == 'value' and d == 'ENDANGERED' or d == 'ENDANGERED_IND':
                        list_endangered.append(six_attribute_country_list)
                    elif c == 'value' and d == 'CRITICAL' or d == 'CRITICAL_IND':
                        list_critical.append(six_attribute_country_list)
                    elif c == 'value' and d == 'VULNERABLE' or d == 'VULNERABLE_IND':
                        list_vulnerable.append(six_attribute_country_list)
                    else:
                        if c == 'value' and d == 'THREATENED' or d == 'THREATENED_IND':
                            list_threatened.append(six_attribute_country_list)

        list_tot_value = []
        list_endangered_value = []
        list_critical_value = []
        list_vulnerable_value = []
        list_threatened_value = []

        for totv in list_tot:
            list_tot_value.append(totv[-1])
        for en1 in list_endangered:
            list_endangered_value.append(en1[-1])
        for cri in list_critical:
            list_critical_value.append(cri[-1])
        for vul in list_vulnerable:
            list_vulnerable_value.append(vul[-1])
        for thre in list_threatened:
            list_threatened_value.append(thre[-1])

        count_list_tot = []
        count_list_endangered = []
        count_list_critical = []
        count_list_vulnerable = []
        count_list_threatened = []
        conditions = ['TOT_KNOWN','ENDANGERED', 'CRITICAL', 'VULNERABLE', 'THREATENED', 'PERCENT_THREATENED']

        for dic_to in list_tot_value:
            for to in dic_to.values():
                count_list_tot.append(int(to))
                tot_dict = {conditions[0]: str(sum(count_list_tot))}
        for dic_e in list_endangered_value:
            for en in dic_e.values():
                count_list_endangered.append(int(en))
                endg_dict = {conditions[1]: str(sum(count_list_endangered))}
        for dic_c in list_critical_value:
            for cr in dic_c.values():
                count_list_critical.append(int(cr))
                cri_dict = {conditions[2]: str(sum(count_list_critical))}
        for dic_v in list_vulnerable_value:
            for vu in dic_v.values():
                count_list_vulnerable.append(int(vu))
                vul_dict = {conditions[3]: str(sum(count_list_vulnerable))}
        for dic_t in list_threatened_value:
            for thr in dic_t.values():
                count_list_threatened.append(int(thr))
                threat_dict = {conditions[4]: str(sum(count_list_threatened))}

                percent_dict = {conditions[5]: str(sum(count_list_threatened) / sum(count_list_tot)*100)}
                species_dict[country] = [tot_dict, endg_dict, cri_dict, vul_dict, threat_dict, percent_dict]
    return species_dict

#######################################################################################

def precipitation(pres):
    with open(pres) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for skip in range(7):
            next(csv_file)
        final_dict={}
        for row in csv_reader:
            list_iteration = iter(row)
            precipitations = dict(zip(list_iteration, list_iteration))

            for k, v in precipitations.items():
                final_dict[k] = str(v)

    return final_dict

#######################################################################################

def seaice(dataset):
    tree = ET.parse(dataset)
    root = tree.getroot()

    sea_ice_dict = {}

    for child in root:
        for subchild in child:
            for d in subchild.iter('date'):
                d.text
            for a in subchild.iter('anom'):
                a.text
                sea_ice_dict[d.text] = a.text

    return sea_ice_dict

#######################################################################################

def ghg_emissions(dataset):
    tree = ET.parse(dataset)
    root = tree.getroot()
    ghg_dict = {}
    ghg_list = list()
    lulu_list=list()
    for child in root[1]:
        series_list = list()
        for subchild in child:
            for i in subchild:
                for x in i.iter():
                    if x.tag == '{http://www.SDMX.org/resources/SDMXML/schemas/v2_0/generic}Time':
                        series_list.append(x.text)
                    else:
                        series_list.append(x.attrib)
        for i in series_list:
            if isinstance(i, str) == False:
                for k, v in i.items():
                    if k == 'value' and v == 'GHG':
                        ghg_list.append(series_list)

    for l in ghg_list:
        for m in l:
            if isinstance(m, str) == False:
                for a, b in m.items():
                    if a == 'value' and b == 'TOTAL_LULU':
                        lulu_list.append(l)
    for u in lulu_list:
        country = u[0].get('value')
        ghg_dict[country] = {}
        index=6
        n=len(u[7:])//2
        while n != 0:
            ghg_dict[country][u[index]] = u[index+1].get('value')
            index += 2
            n -= 1
    return ghg_dict

#######################################################################################

def footprint(dataset):
    with open(dataset) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        footprint_dict = {}
        for row in csv_reader:
            if row[3] == 'AreaTotHA':
                if row[0] in footprint_dict:
                    if row[1] in footprint_dict:
                        footprint_dict[row[0]][row[1]]['AreaTotHA'] = row[10]
                    else:
                        footprint_dict[row[0]][row[1]] = {}
                        footprint_dict[row[0]][row[1]]['AreaTotHA'] = row[10]
                else:
                    footprint_dict[row[0]] = {}
                    footprint_dict[row[0]][row[1]] = {}
                    footprint_dict[row[0]][row[1]]['AreaTotHA'] = row[10]
            if row[3] == 'BiocapTotGHA':
                if row[0] in footprint_dict:
                    footprint_dict[row[0]][row[1]]['BiocapTotGHA'] = row[10]
                else:
                    footprint_dict[row[0]] = {}
                    footprint_dict[row[0]][row[1]] = {}
                    footprint_dict[row[0]][row[1]]['BiocapTotGHA'] = row[10]
    return footprint_dict

#######################################################################################

def paris_agreement(dataset):
    xl_workbook = xlrd.open_workbook(dataset)
    xl_sheet = xl_workbook.sheet_by_index(1)
    paris_dict = {}
    num_cols = xl_sheet.ncols

    for row_idx in range(1, xl_sheet.nrows):
        for col_idx in range(0, num_cols):
            if col_idx == 0:
                country = xl_sheet.cell(row_idx, col_idx)
            if col_idx == 1:
                summary = xl_sheet.cell(row_idx, col_idx)
            if col_idx == 47:
                string_date = xl_sheet.cell(row_idx, col_idx).value
                year, month, day, hour, minute, second = xlrd.xldate_as_tuple(string_date, xl_workbook.datemode)
                date = datetime.datetime(year, month, day, hour, minute, second)

                paris_dict[country.value] = {}
                paris_dict[country.value][date.strftime("%d/%m/%Y")] = summary.value
    return(paris_dict)

#######################################################################################

def global_funds(dataset):
    xl_workbook = xlrd.open_workbook(dataset)
    xl_sheet = xl_workbook.sheet_by_index(0)
    funds_dict = {}
    num_cols = xl_sheet.ncols

    for row_idx in range(1, xl_sheet.nrows):
        row_dict = {}
        for col_idx in range(0, num_cols):
            if col_idx == 0:
                contributor = xl_sheet.cell(row_idx, col_idx)
            if col_idx == 1:
                income = xl_sheet.cell(row_idx, col_idx)
            if col_idx == 2:
                country = xl_sheet.cell(row_idx, col_idx)
            if col_idx == 3:
                deposited = xl_sheet.cell(row_idx, col_idx)
            if col_idx == 6:
                fund = xl_sheet.cell(row_idx, col_idx)
            if col_idx == 8:
                pledged = xl_sheet.cell(row_idx, col_idx)

        row_dict[contributor.value] = [income.value, country.value, str(deposited.value), fund.value, str(pledged.value)]

        for key, value in row_dict.items():
            if key not in funds_dict:
                    funds_dict[key] = [value]
            else:
                funds_dict[key].append(value)

    return funds_dict

#######################################################################################

def eurobarometer_2009(dataset):
    xl_workbook = xlrd.open_workbook(dataset)
    opinions2009_dict = {}

    # QE1a
    first_xl_sheet = xl_workbook.sheet_by_index(3)
    first_answer_list = list()
    for row_idx in range(2, 25):
        first_question = 'Amongst the problems facing the world, is climate change the most serious?'
        if row_idx == 8:
            for col_idx in range(3, first_xl_sheet.ncols):
                country_answer = [first_xl_sheet.cell(row_idx, col_idx).value, (int(first_xl_sheet.cell(row_idx+3, col_idx).value*100))]
                first_answer_list.append(country_answer)

    # QE2
    second_xl_sheet = xl_workbook.sheet_by_index(6)
    second_answer_dict = {}
    answer2_list = list()
    for row_idx in range(2, second_xl_sheet.nrows):
        second_question = 'On a scale from 1 (not at all a serious problem) to 10 (an extremely serious problem), how serious do you consider the problem of climate change?'
        if row_idx == 8:
            for col_idx in range(4, second_xl_sheet.ncols):
                country_answer = [second_xl_sheet.cell(row_idx, col_idx).value]
                index = 3
                n = 11
                while n != 0:
                    if isinstance(second_xl_sheet.cell(row_idx + index, col_idx).value, float):
                        country_answer.append(int(second_xl_sheet.cell(row_idx + index, col_idx).value * 100))
                        index += 2
                        n -= 1
                    else:
                        country_answer.append('-')
                        index += 2
                        n -= 1
                answer2_list.append(country_answer)

    for m in answer2_list:
        sum1 = 0
        sum2 = 0
        sum3 = 0
        x = 4
        y = 6
        z = 10
        while x != 0:
            if m[x] != '-':
                sum1 += m[x]
            x -= 1

        while y != 4:
            if m[y] != '-':
                sum2 += m[y]
            y -= 1

        while z != 6:
            if m[z] != '-':
                sum3 += m[z]
            z -= 1

        second_answer_dict[m[0]] = {}
        second_answer_dict[m[0]]['Not a serious problem (1-4)'] = str(sum1)
        second_answer_dict[m[0]]['A fairly serious problem (5-6)'] = str(sum2)
        second_answer_dict[m[0]]['A very serious problem (7-10)'] = str(sum3)
        second_answer_dict[m[0]]['DK'] = str(m[11])

    # QE4.6
    third_xl_sheet = xl_workbook.sheet_by_index(15)
    third_answer_dict = {}
    answer3_list = list()
    options3_list = list()
    for row_idx in range(2, third_xl_sheet.nrows):
        third_question = 'Have you personally taken any action to fight climate change recently?'
        if row_idx == 4:
            for col_idx in range(5, 20):
                if col_idx == 10:
                    climate = third_xl_sheet.cell(row_idx, col_idx).value
        if row_idx == 8:
            for col_idx in range(3, third_xl_sheet.ncols):
                country_answer = [third_xl_sheet.cell(row_idx, col_idx).value]
                index = 11
                n = 3
                while n != 0:
                    if isinstance(third_xl_sheet.cell(row_idx + index, col_idx).value, float):
                        country_answer.append(int(third_xl_sheet.cell(row_idx + index, col_idx).value * 100))
                        index += 2
                        n -= 1
                    else:
                        country_answer.append('-')
                        index += 2
                        n -= 1
                answer3_list.append(country_answer)
        if row_idx == 19:
            for col_idx in range(1, 5):
                if col_idx == 1:
                    options3_list.append(third_xl_sheet.cell(row_idx, col_idx).value)
                    n = 2
                    index = 2
                    while n != 0:
                        options3_list.append(third_xl_sheet.cell(row_idx + index, col_idx).value)
                        n -= 1
                        index += 2

    for m in answer3_list:
        third_answer_dict[m[0]] = {}
        i = 0
        for w in m[1:]:
            third_answer_dict[m[0]][options3_list[i]] = str(w)
            i += 1

    # mashup
    for l in first_answer_list:
        country = l[0]
        opinions2009_dict[country] = {}
        opinions2009_dict[country][first_question] = str(l[1])

    for key in opinions2009_dict:
        opinions2009_dict[key][second_question] = second_answer_dict.get(key)
        opinions2009_dict[key][third_question] = third_answer_dict.get(key)

    return opinions2009_dict

#######################################################################################

def get_right_number(number):
    frac, whole = math.modf(number)
    if frac > 0.5:
        new_number = math.ceil(number)
    else:
        new_number = int(math.floor(number))
    return new_number

#######################################################################################

def eurobarometer_2013(dataset):
    global climate_change, first_question, fourth_question, third_question, second_question
    xl_workbook = xlrd.open_workbook(dataset)
    opinions2013_dict = {}

    #QA1a
    first_xl_sheet = xl_workbook.sheet_by_index(3)
    first_answer_list = list()
    for row_idx in range(2, 25):
        first_question = 'Amongst the problems facing the world, is climate change the most serious?'
        if row_idx == 11:
            for col_idx in range(0,20):
                if col_idx == 1:
                    climate_change= first_xl_sheet.cell(row_idx, col_idx).value
        if row_idx == 8:
            for col_idx in range(3, first_xl_sheet.ncols):
                country_answer = [first_xl_sheet.cell(row_idx, col_idx).value, get_right_number(first_xl_sheet.cell(row_idx+3, col_idx).value*100)]
                first_answer_list.append(country_answer)
    #QA2.2
    second_xl_sheet = xl_workbook.sheet_by_index(7)
    second_answer_dict = {}
    answer2_list = list()
    options2_list = list()
    for row_idx in range(2, second_xl_sheet.nrows):
        second_question = 'On a scale from 1 (not at all a serious problem) to 10 (an extremely serious problem), how serious do you consider the problem of climate change?'
        if row_idx == 8:
            for col_idx in range(3, second_xl_sheet.ncols):
                country_answer = [second_xl_sheet.cell(row_idx, col_idx).value]
                index = 3
                n = 4
                while n != 0:
                    if isinstance(second_xl_sheet.cell(row_idx + index, col_idx).value, float):
                        country_answer.append(get_right_number(second_xl_sheet.cell(row_idx + index, col_idx).value*100))
                        index += 2
                        n -= 1
                    else:
                        country_answer.append('-')
                        index += 2
                        n -= 1
                answer2_list.append(country_answer)
        if row_idx == 11:
            for col_idx in range(1, 5):
                if col_idx == 1:
                    options2_list.append(second_xl_sheet.cell(row_idx, col_idx).value)
                    n = 3
                    index = 2
                    while n != 0:
                        options2_list.append(second_xl_sheet.cell(row_idx+index, col_idx).value)
                        n -= 1
                        index += 2

    for m in answer2_list:
        second_answer_dict[m[0]] = {}
        i = 0
        for w in m[1:]:
            second_answer_dict[m[0]][options2_list[i]] = str(w)
            i += 1

    #QA3
    third_xl_sheet = xl_workbook.sheet_by_index(8)
    third_answer_dict = {}
    answer3_list = list()
    options3_list = list()
    for row_idx in range(2, third_xl_sheet.nrows):
        third_question = 'Who within the EU is responsible for tackling climate change?'
        if row_idx == 8:
            for col_idx in range(3, third_xl_sheet.ncols):
                country_answer = [third_xl_sheet.cell(row_idx, col_idx).value]
                index = 3
                n = 10
                while n != 0:
                    if isinstance(third_xl_sheet.cell(row_idx + index, col_idx).value, float):
                        country_answer.append(get_right_number(third_xl_sheet.cell(row_idx + index, col_idx).value * 100))
                        index += 2
                        n -= 1
                    else:
                        country_answer.append('-')
                        index += 2
                        n -= 1
                answer3_list.append(country_answer)
        if row_idx == 11:
            for col_idx in range(1, 5):
                if col_idx == 1:
                    options3_list.append(third_xl_sheet.cell(row_idx, col_idx).value)
                    n = 9
                    index = 2
                    while n != 0:
                        options3_list.append(third_xl_sheet.cell(row_idx + index, col_idx).value)
                        n -= 1
                        index += 2

    options3_list[6] = 'Other'
    options3_list[7] = 'All of them'
    options3_list[8] = 'None'

    for f in answer3_list:
        third_answer_dict[f[0]] = {}
        i = 0
        for a in f[1:]:
            third_answer_dict[f[0]][options3_list[i]] = str(a)
            i += 1

    #QA5
    fourth_xl_sheet = xl_workbook.sheet_by_index(11)
    fourth_answer_dict = {}
    answer4_list = list()
    options4_list = list()
    for row_idx in range(2, fourth_xl_sheet.nrows):
        fourth_question = 'Have you personally taken any action to fight climate change recently?'
        if row_idx == 8:
            for col_idx in range(3, fourth_xl_sheet.ncols):
                country_answer = [fourth_xl_sheet.cell(row_idx, col_idx).value, get_right_number(fourth_xl_sheet.cell(row_idx+3, col_idx).value*100), get_right_number(fourth_xl_sheet.cell(row_idx+5, col_idx).value*100)]
                if isinstance(fourth_xl_sheet.cell(row_idx+7, col_idx).value, float):
                    country_answer.append(get_right_number(fourth_xl_sheet.cell(row_idx+7, col_idx).value*100))
                else:
                    country_answer.append('-')
                answer4_list.append(country_answer)
        if row_idx == 11:
            for col_idx in range(1, 5):
                if col_idx == 1:
                    options4_list.append(fourth_xl_sheet.cell(row_idx, col_idx).value)
                    options4_list.append(fourth_xl_sheet.cell(row_idx+2, col_idx).value)
                    options4_list.append(fourth_xl_sheet.cell(row_idx+4, col_idx).value)

    for b in answer4_list:
        fourth_answer_dict[b[0]] = {}
        i = 0
        for h in b[1:]:
            fourth_answer_dict[b[0]][options4_list[i]] = str(h)
            i += 1

    #mashup
    for l in first_answer_list:
        country = l[0]
        opinions2013_dict[country] = {}
        opinions2013_dict[country][first_question] = str(l[1])

    for key in opinions2013_dict:
        opinions2013_dict[key][second_question] = second_answer_dict.get(key)
        opinions2013_dict[key][fourth_question] = fourth_answer_dict.get(key)
        opinions2013_dict[key][third_question] = third_answer_dict.get(key)

    return opinions2013_dict

#######################################################################################

def eurobarometer_2019(dataset):
    xl_workbook = xlrd.open_workbook(dataset)
    opinions2019_dict = {}

    #QB1a
    first_xl_sheet = xl_workbook.sheet_by_index(3)
    first_answer_list = list()
    for row_idx in range(2, 25):
        first_question = 'Amongst the problems facing the world, is climate change the most serious?'
        if row_idx == 8:
            for col_idx in range(4, first_xl_sheet.ncols):
                country_answer = [first_xl_sheet.cell(row_idx, col_idx).value, get_right_number(first_xl_sheet.cell(row_idx+3, col_idx).value*100)]
                first_answer_list.append(country_answer)

    #QB2R
    second_xl_sheet = xl_workbook.sheet_by_index(7)
    second_answer_dict = {}
    answer2_list = list()
    options2_list = list()
    for row_idx in range(2, second_xl_sheet.nrows):
        second_question = 'On a scale from 1 (not at all a serious problem) to 10 (an extremely serious problem), how serious do you consider the problem of climate change?'
        if row_idx == 8:
            for col_idx in range(4, second_xl_sheet.ncols):
                country_answer = [second_xl_sheet.cell(row_idx, col_idx).value]
                index = 3
                n = 4
                while n != 0:
                    if isinstance(second_xl_sheet.cell(row_idx + index, col_idx).value, float):
                        country_answer.append(get_right_number(second_xl_sheet.cell(row_idx + index, col_idx).value*100))
                        index += 2
                        n -= 1
                    else:
                        country_answer.append('-')
                        index += 2
                        n -= 1
                answer2_list.append(country_answer)
        if row_idx == 11:
            for col_idx in range(1, 5):
                if col_idx == 1:
                    options2_list.append(second_xl_sheet.cell(row_idx, col_idx).value)
                    n = 3
                    index = 2
                    while n != 0:
                        options2_list.append(second_xl_sheet.cell(row_idx+index, col_idx).value)
                        n -= 1
                        index += 2

    for m in answer2_list:
        second_answer_dict[m[0]] = {}
        i = 0
        for w in m[1:]:
            second_answer_dict[m[0]][options2_list[i]] = str(w)
            i += 1

    #QB3
    third_xl_sheet = xl_workbook.sheet_by_index(8)
    third_answer_dict = {}
    answer3_list = list()
    options3_list = list()
    for row_idx in range(2, third_xl_sheet.nrows):
        third_question = 'Who within the EU is responsible for tackling climate change?'
        if row_idx == 8:
            for col_idx in range(4, third_xl_sheet.ncols):
                country_answer = [third_xl_sheet.cell(row_idx, col_idx).value]
                index = 3
                n = 10
                while n != 0:
                    if isinstance(third_xl_sheet.cell(row_idx + index, col_idx).value, float):
                        country_answer.append(get_right_number(third_xl_sheet.cell(row_idx + index, col_idx).value * 100))
                        index += 2
                        n -= 1
                    else:
                        country_answer.append('-')
                        index += 2
                        n -= 1
                answer3_list.append(country_answer)
        if row_idx == 11:
            for col_idx in range(1, 5):
                if col_idx == 1:
                    options3_list.append(third_xl_sheet.cell(row_idx, col_idx).value)
                    n = 9
                    index = 2
                    while n != 0:
                        options3_list.append(third_xl_sheet.cell(row_idx + index, col_idx).value)
                        n -= 1
                        index += 2

    options3_list[6] = 'Other'
    options3_list[7] = 'All of them'
    options3_list[8] = 'None'

    for f in answer3_list:
        third_answer_dict[f[0]] = {}
        i = 0
        for a in f[1:]:
            third_answer_dict[f[0]][options3_list[i]] = str(a)
            i += 1

    #QB5
    fourth_xl_sheet = xl_workbook.sheet_by_index(14)
    fourth_answer_dict = {}
    answer4_list = list()
    options4_list = list()
    for row_idx in range(2, fourth_xl_sheet.nrows):
        fourth_question = 'Have you personally taken any action to fight climate change recently?'
        if row_idx == 8:
            for col_idx in range(4, fourth_xl_sheet.ncols):
                country_answer = [fourth_xl_sheet.cell(row_idx, col_idx).value, get_right_number(fourth_xl_sheet.cell(row_idx+3, col_idx).value*100), get_right_number(fourth_xl_sheet.cell(row_idx+5, col_idx).value*100)]
                if isinstance(fourth_xl_sheet.cell(row_idx+7, col_idx).value, float):
                    country_answer.append(get_right_number(fourth_xl_sheet.cell(row_idx+7, col_idx).value*100))
                else:
                    country_answer.append('-')
                answer4_list.append(country_answer)
        if row_idx == 11:
            for col_idx in range(1, 5):
                if col_idx == 1:
                    options4_list.append(fourth_xl_sheet.cell(row_idx, col_idx).value)
                    options4_list.append(fourth_xl_sheet.cell(row_idx+2, col_idx).value)
                    options4_list.append(fourth_xl_sheet.cell(row_idx+4, col_idx).value)

    for b in answer4_list:
        fourth_answer_dict[b[0]] = {}
        i = 0
        for h in b[1:]:
            fourth_answer_dict[b[0]][options4_list[i]] = str(h)
            i += 1

    #mashup
    for l in first_answer_list:
        country = l[0]
        opinions2019_dict[country] = {}
        opinions2019_dict[country][first_question] = str(l[1])

    for key in opinions2019_dict:
        opinions2019_dict[key][second_question] = second_answer_dict.get(key)
        opinions2019_dict[key][fourth_question] = fourth_answer_dict.get(key)
        opinions2019_dict[key][third_question] = third_answer_dict.get(key)

    return opinions2019_dict