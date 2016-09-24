import sys
import os
import re

def guess_strength_code_from_description(description):
    #Strength_Code is a number(25)_unit(MG,mg,ML,ml,G,%) 
    p = re.compile(r'(\s|^)(\d+(\.\d+)?(MG|mg|G|g|ml|ML|l|L|%|MU|mu|IU|U|MCG|mcg|CM|cm|U|u)[-/+]\d+(\.\d+)?(MG|mg|G|g|ml|ML|l|L|%|MU|mu|IU|U|MCG|mcg|CM|cm|U|u))(\s|$)')
    #p = re.compile(r'\b(\d+(MG|mg|G|g|ml|ML|l|L|%|MU|mu|IU|U|MCG|mcg|CM|cm|U|u)[-/+]\d+(MG|mg|G|g|ml|ML|l|L|%|MU|mu|IU|U|MCG|mcg|CM|cm|U|u))\b')
    m = p.findall(description)
    if m :
        if len(m)==1:
            return m[0][1]
        elif len(m) > 1:
            return ''
    
    p = re.compile(r'(\s|^)(\d+(\.\d+)?(MG|mg|G|g|ml|ML|l|L|%|IU|U|MCG|mcg|MU|mu|CM|cm|U|u))(\b|$)')
    m = p.findall(description)
    if m :
        if len(m)==1:
            return m[0][1]
        elif len(m) > 1:
            return ''

    return ''

    # below code for debug only
    print('desc: ', description)
    if m:
        #print ('found strength_code: ', m[0][0], m[1][0])
        print ('found strength_code: ', m)
    else:
        print ('Not found strength code')

def guess_packsize_qty_from_description(description):
    #PackSize_Qty is a number(25)
    p = re.compile(r'(\s|^)(\d+)(\s|$)')
    m = p.findall(description)
    if m :
        if len(m)==1:
            return m[0][1]
        elif len(m) > 1:
            return ''
    
    return ''

    # below code for debug only
    print('desc: ', description)
    if m:
        #print ('found strength_code: ', m[0][0], m[1][0])
        print ('found : ', m)
    else:
        print ('Not found ')

def get_drugform_code_dict(infile="D:\\Data\\DrugForm_Code.txt") :
    form_code_dict = []
    with open(infile, 'r') as fr:
        for line in fr:
            form_code_dict.append(line.strip('\b').strip('\n').strip('\r').strip('\t'))
    return form_code_dict

#test get_drugform_code_dict
test_get_drugform_code_dict = 0
if test_get_drugform_code_dict :
    print ( get_drugform_code_dict() )
    exit()
#end of test get_drugform_code_dict

def guess_drugform_code_from_description(description) :
    form_code_dict = get_drugform_code_dict()
    #DrugForm_Code defined in dictionary

    spaced_desc = " " + description + " "
    for code in form_code_dict :
        spaced_code = " " + code + " "
        if spaced_desc.find(spaced_code) >= 0 :
            return code
    return ''

    # below code for debug only
    print('desc: ', description)
    if m:
        #print ('found strength_code: ', m[0][0], m[1][0])
        print ('found : ', m)
    else:
        print ('Not found ')

#start test code for strength_code
test_guess_strength_code = 0
if test_guess_strength_code :
    print ("testing guess strength code ... ")
    desc = 'SUDOCREM CRM 400IU 125MG fd'
    print ( desc, " : ", guess_strength_code_from_description(desc) )
    desc = 'SUDOCREM CRM 12.5MG-4.00IU'
    print ( desc, " : ", guess_strength_code_from_description(desc) )
    desc = 'SUDOCREM CRM 125MG'
    print ( desc, " : ", guess_strength_code_from_description(desc) )
    desc = 'SUDOCREM CRM 125%/400IU '
    print ( desc, " : ", guess_strength_code_from_description(desc) )
    desc = 'SUDOCREM CRM 125MG+400mg'
    print ( desc, " : ", guess_strength_code_from_description(desc) )
    desc = 'SUDOCREM CRM 125G nothing400IU '
    print ( desc, " : ", guess_strength_code_from_description(desc) )
    desc = 'SUDOCREM CRM 3.5mcg nothing400IU '
    print ( desc, " : ", guess_strength_code_from_description(desc) )
    desc = '2.5U SUDOCREM CRM a3.5mcg nothing400IU '
    print ( desc, " : ", guess_strength_code_from_description(desc) )
    exit()
#end of test code for strength_code



#start test code for packsize_qty
test_guess_packsize_qty = 0
if test_guess_packsize_qty :
    print ('testing guess packsize qty ... ')
    desc = 'SUDOCREM CRM 125MG-400IU 100'
    print ( desc, " : ", guess_packsize_qty_from_description(desc) )
    desc = 'SUDOCREM CRM 125MG'
    print ( desc, " : ", guess_packsize_qty_from_description(desc) )
    desc = 'SUDOCREM CRM 1000 CAP 125%/400IU '
    print ( desc, " : ", guess_packsize_qty_from_description(desc) )
    desc = 'SUDOCREM CRM 125MG+400mg'
    print ( desc, " : ", guess_packsize_qty_from_description(desc) )
    desc = 'SUDOCREM CRM 125MG 400IU '
    print ( desc, " : ", guess_packsize_qty_from_description(desc) )
    desc = '12 SUDOCREM CRM 125G nothing400IU '
    print ( desc, " : ", guess_packsize_qty_from_description(desc) )
    desc = ' 12 SUDOCREM CRM 125G nothing400IU '
    print ( desc, " : ", guess_packsize_qty_from_description(desc) )
    desc = '12 SUDOCREM 15 CRM 125G nothing400IU '
    print ( desc, " : ", guess_packsize_qty_from_description(desc) )
    desc = '12 SUDOCREM 15CRM 125G nothing400IU '
    print ( desc, " : ", guess_packsize_qty_from_description(desc) )
    desc = 'No12 SUDOCREM 15CRM 125G nothing400IU '
    print ( desc, " : ", guess_packsize_qty_from_description(desc) )
    desc = '12+ SUDOCREM 15CRM 125G nothing400IU '
    print ( desc, " : ", guess_packsize_qty_from_description(desc) )
    desc = '%12 SUDOCREM 15CRM 125G nothing400IU '
    print ( desc, " : ", guess_packsize_qty_from_description(desc) )
    exit()
#end of test code for packsize_qty


#start test code for DrugForm_Code
test_guess_drugform_code = 0
if test_guess_drugform_code :
    print ('testing guess drugform code ... ')
    desc = 'SUDOCREM CRM 125MG-400IU'
    print ( desc, " : ", guess_drugform_code_from_description(desc) )
    desc = 'SUDOCREM CODE2 125MG'
    print ( desc, " : ", guess_drugform_code_from_description(desc) )
    desc = 'SUDOCREM CODE2CRM 125%/400IU '
    print ( desc, " : ", guess_drugform_code_from_description(desc) )
    desc = 'CODE1 SUDOCREM CRM 125MG+400mg'
    print ( desc, " : ", guess_drugform_code_from_description(desc) )
    desc = 'CODE1 SUDOCREM CODE2 CRM 125MG 400IU '
    print ( desc, " : ", guess_drugform_code_from_description(desc) )
    desc = 'SUDOCREM CRM 125G nothing400IU CODE3'
    print ( desc, " : ", guess_drugform_code_from_description(desc) )
    desc = 'SUDOCREM CRM 125G nothing400IU MULTI WORD CODEX'
    print ( desc, " : ", guess_drugform_code_from_description(desc) )
    exit()
#end of test code for DrugForm_Code


def get_contents(infile, deliminator='\t'):
    header = []
    rows = []
    lineNo = 0
    with open(infile, 'r') as fr:
        for line in fr:
            lineNo = lineNo + 1
            if (lineNo == 1):
                header = line.strip('\n').split(deliminator)
                continue

            cols = line.strip('\n').split(deliminator)
            row = {}
            colno = 0
            for col in cols:
                row[header[colno]] = col
                colno = colno + 1

            rows.append(row)
    return rows

def choose_orig_or_guessed_value(orig_value, guessed_value) :
    result = orig_value
    if (result == 'NULL' or result == '') :
        if ( (guessed_value != 'NULL') and (guessed_value != '') ) :
            result = guessed_value
    return result

def variant_equal(value1, value2) :
    return 'NO'

def ignore_delimitor_set(value, delimitors = ('/', '-', '"', ',', '(', ')', 'X') ) :
    tmpstr = value
    for delimit in delimitors :
        tmpstr = tmpstr.replace(delimit, ' ')
    resultlist = tmpstr.strip().split(' ')
    resultset = set(resultlist)-set([''])
    return resultset

# test ignore_delimitor_set
test_ignore_delimitor_set = 0
if test_ignore_delimitor_set :
    delimitors = ('/', '-', '"', ',', '(', ')')
    print (ignore_delimitor_set('"2.5MCG-2.5MCG, 60DOSE"', delimitors))
    print (ignore_delimitor_set('2.5MCG/2.5MCG 60DOSE', delimitors))
    exit()
         

def ignore_delimitor_set_relationship(value1, value2) :
    delimitors = ('/', '-', '"', ',', '(', ')')
    set1 = ignore_delimitor_set(value1, delimitors)
    set2 = ignore_delimitor_set(value2, delimitors)

    diff12 = set1 - set2
    diff21 = set2 - set1

    if ( len(diff12) == 0 ) and ( len(diff21) == 0 ) :
        return 'IGNORE_DELIMITOR_EQUAL'
    elif len(diff12) == 0 :
        return 'IGNORE_DELIMITOR_CONTAIN_BWD'
    elif len(diff21) == 0 :
        return 'IGNORE_DELIMITOR_CONTAIN_FWD'
    else :
        diff12str = ' '.join(diff12)
        diff21str = ' '.join(diff21)

        contain_bwd = 1
        for item12 in diff12 :
            if ( diff21str.find(item12) == -1 ) :
                contain_bwd = 0

        if contain_bwd :
            return 'IGNORE_DELIMITOR_CONTAIN_BWD'

        contain_fwd = 1
        for item21 in diff21 :
            if ( diff12str.find(item21) == -1 ) :
                contain_fwd = 0

        if contain_fwd :
            return 'IGNORE_DELIMITOR_CONTAIN_FWD'

        for item12 in diff12 :
            virtual_match = 0
            for item21 in diff21 :
                if ( item12.find(item21) == 0 or item21.find(item12) == 0 ) :
                    virtual_match = 1
                    break
            if not virtual_match :
                return 'CONFLICT'

        for item21 in diff21 :
            virtual_match = 0
            for item12 in diff12 :
                if ( item12.find(item21) == 0 or item21.find(item12) == 0 ) :
                    virtual_match = 1
                    break
            if not virtual_match :
                return 'CONFLICT'

    return 'IGNORE_DELIMITOR_CONTAIN_MIX'



def value_relationship(value1, value2) :
    if ( value1 == 'NULL' or value1 == '' ) and ( value2 == 'NULL' or value2 == '' ) :
        return 'NO_CONFLICT_BOTH_NULL'
    elif ( value1 == 'NULL' or value1 == '' ) or ( value2 == 'NULL' or value2 == '' ) :
        return 'NO_CONFLICT_ONE_NULL'
    elif ( value1 == value2 ) :
        return 'EQUAL'
    elif ( value1.find(value2) >=0 ) :
        return 'CONTAIN_FWD'
    elif ( value2.find(value1) >=0 ) :
        return 'CONTAIN_BWD'
    elif variant_equal(value1, value2) == 'YES' :
        return 'EQUAL'
    else :
        return ignore_delimitor_set_relationship(value1, value2)

def value_all_null(value1, value2, value3) :
    if ( value1 == 'NULL' or value1 == '' ) and ( value2 == 'NULL' or value2 == '' ) and ( value3 == 'NULL' or value3 == '' ) :
        return 'ALL_NULL'
    return 'NOT_ALL_NULL'

def get_t3_drugmaster_codes_list_for_t1_zdispense(table1, table3) :
    t3_drugmaster_codes_list = {}
    for record1 in table1 :
        if not ( record1['SourceSystem_Code'] == 'ZDISPENSE' ) :
            continue;
        if ( record1['Universal_Code'] == 'NULL' or record1['Universal_Code'] == '' ) :
            continue;

        t3_drugmaster_codes_list[record1['Universal_Code']] = []
        for record3 in table3 :
            if ( record3['Universal_Code_Key'] == record1['Universal_Code'] ) :
                t3_drugmaster_codes_list[record1['Universal_Code']].append( record3['DrugMaster_Code_Key'] )

    return t3_drugmaster_codes_list


# return 'SUCCESS',''  or 'FAIL','reject reason'
def map_record_rule2_zdispense(record1, record2, t3_drugmaster_code_lists) :
    if not ( record1['SourceSystem_Code'] == 'ZDISPENSE' ) :
        return 'FAIL', 'record1 SourceSystem_Code is not ZDISPENSE'
    if ( record1['Universal_Code'] == 'NULL' or record1['Universal_Code'] == '' ) :
        return 'FAIL', 'record1 is ZDISPENSE but Universal_Code is NULL'

    if not (record1['Universal_Code'] in t3_drugmaster_code_lists) :
        print ( "EXCPETION: record1_Universal_Code not in t3_drugmaster_code_lists? Mean get_t3_drugmaster_codes_list_for_t1_zdispense is wrong." +  record1['Universal_Code'] )
        exit()

    if len(t3_drugmaster_code_lists[record1['Universal_Code']]) == 0 :
        return 'FAIL', 'record1 Universal_Code not found in table3'

    if record2['DrugMaster_Code_Key'] in t3_drugmaster_code_lists[record1['Universal_Code']] :
        #matched
        return 'SUCCESS', ''
    else :
        return 'FAIL', 'record 2 DrugMaster_Code_Key not match with table3'

    print ("EXCEPTION: something wrong, code should NEVER reach here")
    exit()

def extract_number_unit(strength_code_item) :
    number = ''
    unit = ''
    item = strength_code_item.strip()
    idx = 0
    while idx < len(item) :
        if item[idx] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.') :
            number += item[idx]
            idx += 1
        else :
            break
    while idx < len(item) :
        unit += item[idx]
        idx += 1

    return number, unit


def transform_unit_number(strength_code_item) :
    number, unit = extract_number_unit(strength_code_item.upper())
    if unit == 'MCG' :
        try :
            number = str(float(number)/1000)
            unit = 'MG'
        except :
            print ("ignoring transform invalid number:", number, unit)
    elif unit == 'G':
        try :
            number = str(float(number)*1000)
            unit = 'MG'
        except :
            print ("ignoring transform invalid number:", number, unit)
    return number, unit

# test transform_unit_number
test_transform_unit_number = 0
if test_transform_unit_number :
    num1, unit1 = transform_unit_number('500MCG')
    print (str(num1), unit1)
    print (transform_unit_number('500mcg'))
    num2, unit2 = transform_unit_number('0.5mg')
    print ( str(num2), unit2 )
    if (str(num1) == num2):
        print('num1 == num2')
    if (unit1 == unit2):
        print('unit1 == unit2')

    print ('test012abc'.upper())
    exit()

def strength_code_after_transform(strength_code) :
    ignore_delimitor_strength_code_set = ignore_delimitor_set(strength_code)

    only_keep_numbers = []
    for item in set(ignore_delimitor_strength_code_set) :
        number, unit = transform_unit_number(item)
        only_keep_numbers.append( number )
    return set(only_keep_numbers)-set([''])

def set_value_relationship(set1, set2) :
    if ( len(set1 - set2) ==0 ) and ( len(set2 - set1) ==0 ):
        return 'EQUAL'
    elif ( len(set1 - set2) ==0 ) :
        return 'CONTAIN_BWD'
    elif ( len(set2 - set1) ==0 ) :
        return 'CONTAIN_FWD'
    else :
        return 'CONFLICT'

# test strength_code_after_transform
test_strength_code_after_transform = 0
if test_strength_code_after_transform :
    set1 = strength_code_after_transform("50MG/150g 12")
    set2 = strength_code_after_transform("50MG 150g 23")
    print (set_value_relationship(set1, set2))
    set1 = strength_code_after_transform('"0.05%, 0.47G, 2"')
    set2 = strength_code_after_transform('0.05%  0.47G X2')
    print (set1)
    print (set2)
    print (set_value_relationship(set1, set2))
    set1 = strength_code_after_transform('18MG/3ML (PEN) ')
    set2 = strength_code_after_transform('6MG/ML 3ML')
    print (set1)
    print (set2)
    print (set_value_relationship(set1, set2))
    exit()
# end test strength_code_after_transform


# return 'SUCCESS',''  or 'FAIL','reject reason'
def map_record_rule1_strict(record1, record2, debug='FALSE') :
    record1_Strength_Code = choose_orig_or_guessed_value (record1['Strength_Code'], record1['Guess_Strength_Code'])
    record1_PackSize_Qty = choose_orig_or_guessed_value (record1['PackSize_Qty'], record1['Guess_PackSize_Qty'])
    record1_Form_Code = choose_orig_or_guessed_value (record1['Form_Code'], record1['Guess_Form_Code'])

    if ( debug == 'DEBUG-VERY-DETAIL' ) :
        print ("record1['Strength_Code']: ", record1['Strength_Code'], "   ", "record1['Guess_Strength_Code']: ", record1['Guess_Strength_Code'], "   choosed record1_Strength_Code : ", record1_Strength_Code)

    drug_desc_compatible_set = ('EQUAL', 'CONTAIN_FWD', 'CONTAIN_BWD', 'IGNORE_DELIMITOR_EQUAL', 'IGNORE_DELIMITOR_CONTAIN_FWD', 'IGNORE_DELIMITOR_CONTAIN_BWD', 'IGNORE_DELIMITOR_CONTAIN_MIX')
    if not ( value_relationship(record1['Drug_Description'], record2['DrugMaster_Name']) in drug_desc_compatible_set \
            or value_relationship(record1['Drug_Description'], record2['OverrideDrugMaster_Name']) in drug_desc_compatible_set \
            or value_relationship(record1['AltDrug_Description'], record2['DrugMaster_Name']) in drug_desc_compatible_set \
            or value_relationship(record1['AltDrug_Description'], record2['OverrideDrugMaster_Name']) in drug_desc_compatible_set ) :
        return 'FAIL', 'Drug_Desc/Alt and DrugMaster_Name not compatible'

    strength_code_compatible_set = ('EQUAL', 'CONTAIN_BWD', 'CONTAIN_FWD')

    record1_strength_code_after_transform = strength_code_after_transform(record1_Strength_Code)
    record2_strength_code_after_transform = strength_code_after_transform(record2['DrugStrength_Code'])
    record2_override_strength_code_after_transform = strength_code_after_transform(record2['OverrideDrugStrength_Code'])

    if ( debug == 'DEBUG-VERY-DETAIL' ) :
        print ("record1_strength_code_after_transform: ", record1_strength_code_after_transform)
        print ("record2_strength_code_after_transform: ", record2_strength_code_after_transform)
        print ("record2_override_strength_code_after_transform: ", record2_override_strength_code_after_transform)
        print ("set_value_relationship(record1_strength_code_after_transform, record2_strength_code_after_transform) : ", set_value_relationship(record1_strength_code_after_transform, record2_strength_code_after_transform))
        print ("set_value_relationship(record1_strength_code_after_transform, record2_override_strength_code_after_transform) : ", set_value_relationship(record1_strength_code_after_transform, record2_override_strength_code_after_transform))
        print ("value_all_null(record1_Strength_Code, record2['DrugStrength_Code'], record2['OverrideDrugStrength_Code']) : ", value_all_null(record1_Strength_Code, record2['DrugStrength_Code'], record2['OverrideDrugStrength_Code']))

    if not ( set_value_relationship(record1_strength_code_after_transform, record2_strength_code_after_transform) in strength_code_compatible_set \
            or set_value_relationship(record1_strength_code_after_transform, record2_override_strength_code_after_transform) in strength_code_compatible_set \
            or value_all_null(record1_Strength_Code, record2['DrugStrength_Code'], record2['OverrideDrugStrength_Code']) == 'ALL_NULL'  ) :
        return 'FAIL', 'DrugStrength_Code NOT MATCH'

    if not ( value_relationship(record1_PackSize_Qty, record2['PackSize_Qty']) == 'EQUAL' \
            or value_relationship(record1_PackSize_Qty, record2['OverridePackSize_Qty']) == 'EQUAL' \
            or value_all_null(record1_PackSize_Qty, record2['PackSize_Qty'], record2['OverridePackSize_Qty']) == 'ALL_NULL' 
            or record1['PackSize_Qty'] == 1 or str(record2['PackSize_Qty']) == '1' ) :
               # here we do not use record1_PackSize_Qty, we make assumption there will be few cases where packsize is '1' in description
        return 'FAIL', 'PackSize_Qty NOT MATCH'

    #if not ( value_relationship(record1_Form_Code, record2['DrugForm_Code']) == 'EQUAL' \
    if (0) and not ( value_relationship(record1_Form_Code, record2['DrugForm_Code']) == 'EQUAL' \
            or value_relationship(record1_Form_Code, record2['OverrideDrugForm_Code']) == 'EQUAL' \
            or value_all_null(record1_Form_Code, record2['DrugForm_Code'], record2['OverrideDrugForm_Code']) == 'ALL_NULL'  ) :
        return 'FAIL', 'Form_Code NOT MATCH with DrugForm_Code'

    if not ( value_relationship(record1['Manufacturer_Name'], record2['Manufacturer_Code']) == 'EQUAL' \
            or record1['Manufacturer_Name'] == 'NULL' ) :
        return 'FAIL', 'Manufacturer_Name NOT MATCH with Manufacturer_Code'

    return 'SUCCESS', ''


def find_match_records_rule1_strict(table1, table2, rulename) :
    matchresult = []

    for record1 in table1:
        # map to record in table2
        matcheditems = {}
        matcheditems['table1record'] = record1
        #matcheditems[record1['DrugMaster_ID']] = []
        matcheditems['rulename'] = rulename
        matcheditems['table2records'] = []

        for record2 in table2:
            mapresult, rejectreason = map_record_rule1_strict(record1, record2)
            if mapresult == 'SUCCESS' :
                matcheditems['table2records'].append(record2)

        matchresult.append(matcheditems)

        if ( record1['Manufacturer_Name'] == 'NULL') and (len(matcheditems['table2records']) > 1) :
            print ("Clear map records because Manufacturer_Name is NULL and there are multiple matches")
            print ("----------------------------------------------------------")
            print ("DrugMaster_ID:", record1['DrugMaster_ID'], "   Matched ", len(matcheditems['table2records']), " records")
            for tmprec2 in matcheditems['table2records'] :
                print ("DrugMaster_Code_Key:", tmprec2['DrugMaster_Code_Key'])
            print ("----------------------------------------------------------")
            # if Manu name is empty, only keep 1:1 map record. Clear the map records if more than 1 maps.
            matcheditems['table2records'] = []

        if ( record1['PackSize_Qty'] == '1') and (len(matcheditems['table2records']) > 1) :
            print ("Clear map records because PackSize_Qty=1 and there are multiple matches")
            print ("----------------------------------------------------------")
            print ("DrugMaster_ID:", record1['DrugMaster_ID'], "   Matched ", len(matcheditems['table2records']), " records")
            for tmprec2 in matcheditems['table2records'] :
                print ("DrugMaster_Code_Key:", tmprec2['DrugMaster_Code_Key'])
            print ("----------------------------------------------------------")
            # if table1 packsize is 1, only keep 1:1 map record. Clear the map records if more than 1 maps.
            matcheditems['table2records'] = []

    return matchresult

def find_match_records_rule2_zdispense(table1, table2, table3, rulename):
    matchresult = []
    t3_drugmaster_codes_list = get_t3_drugmaster_codes_list_for_t1_zdispense(table1, table3)

    for record1 in table1:
        # map to record in table2
        matcheditems = {}
        matcheditems['table1record'] = record1
        matcheditems['rulename'] = 'NO_RULE_NAME'
        matcheditems['table2records'] = []
        for record2 in table2:
            result, rejectreason = map_record_rule2_zdispense(record1, record2, t3_drugmaster_codes_list)
            if ( result == 'SUCCESS' ) :
                matcheditems['rulename'] = rulename
                matcheditems['table2records'].append(record2) 

        matchresult.append(matcheditems)

    return matchresult

def get_guess_transform_record(record) :
    #Add new columns: 'Guess_Strength_Code', 'Guess_PackSize_Qty', 'Guess_Form_Code'  based on 'Drug_Description' and 'AltDrug_Description'
        if 'Drug_Description' not in record:
            print ('Drug_Description not exist. Error. Please make sure you are using the right table.')
            exit()
        if 'AltDrug_Description' not in record:
            print ('AltDrug_Description not exist. Error. Please make sure you are using the right table.')
            exit()
        newrecord = record
        guess1 = guess_strength_code_from_description(record['Drug_Description'])
        guess2 = guess_strength_code_from_description(record['AltDrug_Description'])
        if ( (guess1 == '') or (guess1 == 'NULL') ) :
            newrecord['Guess_Strength_Code'] = guess2
        elif ( (guess2 == '') or (guess2 == 'NULL') ) :
            newrecord['Guess_Strength_Code'] = guess1
        elif ( guess1 == guess2 ):
            newrecord['Guess_Strength_Code'] = guess1
        else :
            #guess1 and guess2 are conflicting, do not use any one
            newrecord['Guess_Strength_Code'] = ''

        guess1 = guess_packsize_qty_from_description(record['Drug_Description'])
        guess2 = guess_packsize_qty_from_description(record['AltDrug_Description'])
        if ( (guess1 == '') or (guess1 == 'NULL') ) :
            newrecord['Guess_PackSize_Qty'] = guess2
        elif ( (guess2 == '') or (guess2 == 'NULL') ) :
            newrecord['Guess_PackSize_Qty'] = guess1
        elif ( guess1 == guess2 ):
            newrecord['Guess_PackSize_Qty'] = guess1
        else :
            #guess1 and guess2 are conflicting, do not use any one
            newrecord['Guess_PackSize_Qty'] = ''

        guess1 = guess_drugform_code_from_description(record['Drug_Description'])
        guess2 = guess_drugform_code_from_description(record['AltDrug_Description'])
        if ( (guess1 == '') or (guess1 == 'NULL') ) :
            newrecord['Guess_Form_Code'] = guess2
        elif ( (guess2 == '') or (guess2 == 'NULL') ) :
            newrecord['Guess_Form_Code'] = guess1
        elif ( guess1 == guess2 ):
            newrecord['Guess_Form_Code'] = guess1
        else :
            #guess1 and guess2 are conflicting, do not use any one
            newrecord['Guess_Form_Code'] = ''

        return newrecord



def get_guess_transform_table(table):
    #Add new columns: 'Guess_Strength_Code', 'Guess_PackSize_Qty', 'Guess_Form_Code'  based on 'Drug_Description' and 'AltDrug_Description'
    transformed_table = []
    for record in table:
        transformed_record = get_guess_transform_record(record)
        transformed_table.append(transformed_record)

    return transformed_table


def find_match_records_rule1_guess_transform_rule1_strict(table1, table2, rulename):
    transformed_table1 = get_guess_transform_table(table1)
    matchresult = find_match_records_rule1_strict(transformed_table1, table2, rulename)

    return matchresult


def find_match_records_rule2_guess_transform_rule2_zdispense(table1, table2, table3, rulename):
    transformed_table1 = get_guess_transform_table(table1)
    matchresult = find_match_records_rule2_zdispense(table1, table2, table3, rulename)

    return matchresult


def compare_records(table1, table2):
    diff = []
    missing = []
    skiplist = ('Created_DateTime')
    #mustprintlist = ('Form_Code', 'Strength_Code')
    mustprintlist = ()
    for record1 in table1:
        # map to record in table2
        found = 0
        for record2 in table2:
            if record2['Drug_Code'] == record1['Drug_Code']:
                found = 1
                diffitem = {}
                diffitem[record1['Drug_Code']] = {}
                for key in record1:
                    value = record1[key]
                    if key in skiplist:
                        continue
                    if key in mustprintlist:
                        diffitem[record1['Drug_Code']][key] = {}
                        diffitem[record1['Drug_Code']][key]['table1_MUSTPRINT'] = value
                        diffitem[record1['Drug_Code']][key]['table2_MUSTPRINT'] = record2[key]
                        continue
                    if (key in record2 and  record2[key] != value):
                        diffitem[record1['Drug_Code']][key] = {}
                        diffitem[record1['Drug_Code']][key]['table1'] = value
                        diffitem[record1['Drug_Code']][key]['table2'] = record2[key]

                diff.append(diffitem)
                break
        if (found == 0):
            missing.append(record1['Drug_Code'])

    return diff, missing


def is_no_null_contains(str1, str2) :
    if (str1 == "NULL" or str1 == "" ):
        return 0
    if (str2 == "NULL" or str2 == "" ):
        return 0
    if (str1.find(str2) >= 0) :
        return 1
    return 0

def format_print_two_records_grouped_key_fields_horizental_layout(record1, record2, map_fields_groups) :
        print ("+++++++++++++ table1mapfields value +++++++++++++++        --------------- table2mapfields value ------------")
        for map_fields_group in map_fields_groups:
            print (repeat_chars('-', 110), map_fields_group['groupname'], repeat_chars('-', 5) )
            for map_field in map_fields_group['map_fields'] :
                tabular_print(map_field[0]+":", record1[map_field[0]], "|", record2[map_field[1]], ":"+map_field[1] )


# print_additional_zdispense_info can be 'print-zdispense'(will print additional information for zdispense) or others (will not display zdispense)
def format_print_matched_array_ignore_empty_horizental_layout(array, print_additional_zdispense_info='not-print-dispense'):
    num_not_match = 0
    num_uniq_match = 0
    num_multi_match = 0
    actualoutputnum = 0
    
    map_fields_groups = [ \
            {'groupname' : 'Group 1: Drug Description', \
            'map_fields' : [ ['Drug_Description', 'DrugMaster_Name'],  ['AltDrug_Description', 'OverrideDrugMaster_Name'] ]  } , \
            {'groupname' : 'Group 2: Strength Code', \
            'map_fields' : [ ['Strength_Code', 'DrugStrength_Code'],  ['Guess_Strength_Code', 'OverrideDrugStrength_Code'] ]  } , \
            {'groupname' : 'Group 3: Packsize Qty', \
            'map_fields' : [ ['PackSize_Qty', 'PackSize_Qty'],  ['Guess_PackSize_Qty', 'OverridePackSize_Qty'] ]  } , \
            {'groupname' : 'Group 4: Form Code', \
            'map_fields' : [ ['Form_Code', 'DrugForm_Code'],  ['Guess_Form_Code', 'OverrideDrugForm_Code'] ]  } , \
            {'groupname' : 'Group 5: Manufacturer Name', \
            'map_fields' : [ ['Manufacturer_Name', 'Manufacturer_Code'] ]  } , \
            {'groupname' : 'Group 6: ProductExtension_Code', \
            'map_fields' : [ ['Drug_Description', 'ProductExtension_Code'] ]  } , \
            {'groupname' : 'Group 7: For Copy Paste', \
            'map_fields' : [ ['DrugMaster_ID', 'DrugMaster_Code_Key'] ]  } \
            ]

    for item in array:
        map_number_info = ''

        if (len(item['table2records']) == 0):
            continue
        elif (len(item['table2records']) == 1):
            num_uniq_match = num_uniq_match + 1
            map_number_info = '1:1 unique match'
        elif (len(item['table2records']) > 1):
            num_multi_match = num_multi_match + 1
            map_number_info = '1:' + str(len(item['table2records'])) + ' multiple match'

        actualoutputnum = actualoutputnum + 1
        print ("Result NO: ", actualoutputnum, "    ******  ", map_number_info, "   ******   ", "Map rulename : %s" % item['rulename'])
        table2_record_no = 0
        for table2record in item['table2records'] :
            table2_record_no += 1
            print ( 'map candidate: ', table2_record_no, '/', len(item['table2records']), repeat_chars('-',50) )
            format_print_two_records_grouped_key_fields_horizental_layout( item['table1record'], item['table2records'][table2_record_no-1], map_fields_groups )

            if ( print_additional_zdispense_info == "print-zdispense" ) :
                str_desc = ""
                if  is_no_null_contains ( item['table1record']['Drug_Description'], item['table2records'][table2_record_no-1]['DrugMaster_Name'] ) :
                    str_desc = "GOOD:" + str_desc + " Drug_Desc >> DrugMaster_Name. "
                if  is_no_null_contains ( item['table1record']['Drug_Description'], item['table2records'][table2_record_no-1]['OverrideDrugMaster_Name'] ) :
                    str_desc = "GOOD:" + str_desc + " Drug_Desc >> OverrideDrugMaster_Name. "
                if  is_no_null_contains ( item['table1record']['AltDrug_Description'], item['table2records'][table2_record_no-1]['DrugMaster_Name'] ) :
                    str_desc = "GOOD:" + str_desc + " AltDrug_Desc >> DrugMaster_Name. "
                if  is_no_null_contains ( item['table1record']['AltDrug_Description'], item['table2records'][table2_record_no-1]['OverrideDrugMaster_Name'] ) :
                    str_desc = "GOOD:" + str_desc + " AltDrug_Desc >> OverrideDrugMaster_Name. "

                if str_desc == "" :
                    str_desc = "BAD: Drug_Desc/Alt does NOT contain DrugMaster_Name/Alt"

                print (repeat_chars("=", 140))
                tabular_print ("Universal_Code:", item['table1record']['Universal_Code'], "|", str_desc, "") 

        print ("\n================= whole record of table1 content ====================")
        print ("\n%s \n" % item['table1record'])
        print ("--------- Number match: %s in table2 ---------\n" % len(item['table2records']))
        print ("================= whole records of table2 content(if more than one, display all ) ====================")
        print ("%s \n\n" % item['table2records'])

    print ("Size of array: %s" % len(array))
    print ("num_not_match: %s" % num_not_match)
    print ("num_uniq_match: %s" % num_uniq_match)
    print ("num_multi_match: %s" % num_multi_match)

def repeat_chars(char, num) :
    str = ""
    i = 0
    while i < num :
        str = str + char
        i = i + 1
    return str

def tabular_print(item1, item2, item3, item4, item5, pos1=0, space2=1, pos3=55, space4=1, pos5=80) :
    pos2 = pos3 - len(item2) - space2
    pos4 = pos3 + len(item3) + space4
    s1 = pos1
    s2 = pos2 - pos1 - len(item1)
    s3 = pos3 - pos2 - len(item2)
    s4 = pos4 - pos3 - len(item3)
    s5 = pos5 - pos4 - len(item4)

    output = repeat_chars('', s1) + item1 + repeat_chars(' ', s2) + item2 + repeat_chars(' ', s3) + item3 + repeat_chars(' ', s4) + item4 + repeat_chars(' ', s5) + item5
    print (output)

#test format1
test_format1 = 0

if test_format1 :
    mfg1 = {}
    mfg1['map_fields'] =  [{'table1_field_name':'t1fn111', 'table2_field_name':'t2fn111'}, {'table1_field_name':'t1fn222', 'table2_field_name':'t2fn222'}]
    print (mfg1['map_fields'][0]['table2_field_name'])
    exit()

#end of test format1

#test tabular_print
test_tabular_print = 0
if test_tabular_print :
    tabular_print("item1:", "item2", "|", "item4", "item5")
    tabular_print("item1:", "item2 dsffffffffffffffffffff", "|", "item4 dsfffffff", "item5")
    tabular_print("item1fdsfd :", "", "|", "item4", "item5")
    tabular_print("item1 so long :", "item2 nofdsffffffffffffffffffffffffffffffffffffffff", "|", "item4 not", "item5 xkjkbvjkjfkdsjfd")
    exit()
#end of test tabular_print

def debug_map_record1_rule1_strict_by_id_supper_slow(rec1_drugmaster_id, rec2_drugmaster_code_key) :
    table_orig = get_contents("d:\\data\\1.txt")
    table_select = get_contents("d:\\data\\2.txt")
    table1 = []
    for rec1 in table_orig :
        if rec1['DrugMaster_ID'] == rec1_drugmaster_id :
            table1.append(rec1)
    if ( len(table1) == 0 ) :
        print ("No such rec1_drugmaster_id : ", rec1_drugmaster_id)
        return
    if ( len(table1) > 1 ) :
        print ("WARNING: more than one rec1_drugmaster_id found, should be uniq: ")
        for tmprec in table1:
            print (tmprec)

    table2 = []
    for rec2 in table_select :
        if rec2['DrugMaster_Code_Key'] == rec2_drugmaster_code_key : 
            table2.append(rec2)
    if ( len(table2) == 0 ) :
        print ("No such rec2_drugmaster_code_key : ", rec2_drugmaster_code_key)
        return
    if ( len(table2) > 1 ) :
        print ("WARNING: more than one rec2_drugmaster_code_key found, should be uniq: ")
        for tmprec in table2 :
            print (tmprec)

    record1 = table1[0]
    record2 = table2[0]
    transformed_record1 = get_guess_transform_record(record1)
    result,message = map_record_rule1_strict(transformed_record1, record2, "DEBUG-VERY-DETAIL")
    print (result, message)


def compare_ann_result() :
    table_orig = get_contents("d:\\data\\ann11.txt")
    table1 = get_guess_transform_table(table_orig)
    table2 = get_contents("d:\\data\\2.txt")
    table3 = get_contents("d:\\data\\DimBarcode.txt")
    t3_drugmaster_codes_list = get_t3_drugmaster_codes_list_for_t1_zdispense(table1, table3)

    map_fields_groups = [ \
            {'groupname' : 'Group 1: Drug Description', \
            'map_fields' : [ ['Drug_Description', 'DrugMaster_Name'],  ['AltDrug_Description', 'OverrideDrugMaster_Name'] ]  } , \
            {'groupname' : 'Group 2: Strength Code', \
            'map_fields' : [ ['Strength_Code', 'DrugStrength_Code'],  ['Guess_Strength_Code', 'OverrideDrugStrength_Code'] ]  } , \
            {'groupname' : 'Group 3: Packsize Qty', \
            'map_fields' : [ ['PackSize_Qty', 'PackSize_Qty'],  ['Guess_PackSize_Qty', 'OverridePackSize_Qty'] ]  } , \
            {'groupname' : 'Group 4: Form Code', \
            'map_fields' : [ ['Form_Code', 'DrugForm_Code'],  ['Guess_Form_Code', 'OverrideDrugForm_Code'] ]  } , \
            {'groupname' : 'Group 5: Manufacturer Name', \
            'map_fields' : [ ['Manufacturer_Name', 'Manufacturer_Code'] ]  } , \
            {'groupname' : 'Group 6: ProductExtension_Code', \
            'map_fields' : [ ['Drug_Description', 'ProductExtension_Code'] ]  } , \
            {'groupname' : 'Group 7: For Copy Paste', \
            'map_fields' : [ ['DrugMaster_ID', 'DrugMaster_Code_Key'] ]  } \
            ]


    for record1 in table1:
        if record1['DrugMaster_Code'] != '!UNMAPPED' :
            for record2 in table2:
                if record2['DrugMaster_Code_Key'] == record1['DrugMaster_Code'] :
                    result1, rejectreason1 = map_record_rule1_strict(record1, record2)
                    print (record1['DrugMaster_ID'], ' : rule1_strict : ', result1, ' : ',rejectreason1)
                    result2, rejectreason2 = map_record_rule2_zdispense(record1, record2, t3_drugmaster_codes_list)
                    print (record1['DrugMaster_ID'], ' : rule2_zdispense : ', result2, ' : ',rejectreason2)
                    if (result1 == 'FAIL' and result2 == 'FAIL') :
                        format_print_two_records_grouped_key_fields_horizental_layout(record1, record2, map_fields_groups) 
                    break



# used to debug two records, very slow, only use to run several records, do NOT run large list!!!!
debug_map_record1_rule1_strict_by_id_supper_slow('588271','SAXE1')
exit()


# apply z-dispense rule to do the map, it is about 1 or 2 minutes.
table_orig = get_contents("d:\\data\\1.txt")
table_select = get_contents("d:\\data\\2.txt")
table_third = get_contents("d:\\data\\DimBarcode.txt")
matchresult = find_match_records_rule2_guess_transform_rule2_zdispense(table_orig, table_select, table_third, 'rule2_with_guess_zdispense')
format_print_matched_array_ignore_empty_horizental_layout(matchresult, 'print-zdispense')

exit()


# apply rule1 to do the map, it is about 30 minutes to run through a 1200 records in table1 with 13000 records in table2
table_orig = get_contents("d:\\data\\1.txt")
table_select = get_contents("d:\\data\\2.txt")
matchresult = find_match_records_rule1_guess_transform_rule1_strict(table_orig, table_select, 'rule1_with_guess_packsize1_ignore_formcode')
format_print_matched_array_ignore_empty_horizental_layout(matchresult, 'not-print-zdispense')

exit()


# run through ann result list, if ann's mapped record is not SUCCESS by our script, it gives the information why it fails to map
compare_ann_result()
exit()





###########other old testings, usually not used##############

table_orig = get_contents("d:\\data\\1.txt")
table_select = get_contents("d:\\data\\2.txt")
table1 = []
for rec1 in table_orig :
    if rec1['DrugMaster_ID'] == '673738' or rec1['DrugMaster_ID'] == '672488':
        table1.append(rec1)
table2 = []
for rec2 in table_select :
    if rec2['DrugMaster_Code_Key'] == 'DIP2' or rec2['DrugMaster_Code_Key'] == 'ALTV3' :
        table2.append(rec2)
transformed_table1 = get_guess_transform_table(table1)
 
#matchresult_to_compare = generate_psudo_map_for_debug(transformed_table1, '673738', table2, 'DIP2' )
#format_print_matched_array_ignore_empty_horizental_layout(matchresult_to_compare, 'not-print-zdispense' )

matchresult_to_see_error = find_match_records_rule1_strict(transformed_table1, table2, 'rule1_with_guess_packsize1_ignore_formcode', 'recordrejectreason')
format_print_matched_array_ignore_empty_horizental_layout(matchresult_to_see_error, 'not-print-zdispense' )

exit()


table_orig = get_contents("d:\\data\\1.txt")
table_select = get_contents("d:\\data\\2.txt")
matchresult = find_match_records_rule1_guess_transform_rule1_strict(table_orig, table_select, 'rule1_with_guess_packsize1_ignore_formcode')
format_print_matched_array_ignore_empty_horizental_layout(matchresult, 'not-print-zdispense')

exit()




table_orig = get_contents("d:\\data\\1.txt")
table_select = get_contents("d:\\data\\2.txt")
matchresult = find_match_records_rule1_strict(table_orig, table_select, 'rule1_strict')
format_print_matched_array_ignore_empty(matchresult)

exit()


table_orig = get_contents("d:\\data\\ann_original.txt")
table_later = get_contents("d:\\data\\ann_later.txt")

diff, missing = compare_records(table_orig, table_later)
print ('=====================different =======================')
format_print_array (diff)
print ('=====================missing=======================')
format_print_array (missing)



exit()

print (get_contents("d:\\data\\3.txt"))
print (len(get_contents("d:\\data\\3.txt")))

exit()

print (get_contents("d:\\data\\2.txt"))
print (len(get_contents("d:\\data\\2.txt")))

exit()


print (get_contents("d:\\data\\1.txt"))
print (len(get_contents("d:\\data\\1.txt")))

exit()


print ((get_contents("d:\\data\\1.txt")[27]))
mul = []
aaa = {}
aaa['testindex']='value'
aaa['testindexfs']=123
mul.append(aaa)
aaa['testindex']='value111'
aaa['testindexfs']=123111
mul.append(aaa)
print (mul)
print (mul[1]['testindexfs'])



