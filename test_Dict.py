import os
import inspect
import re
from decimal import Decimal

import Dict
import datetime

MANDATORY_FUNCTIONS = [
    'form_profile_dict',
    'form_profile_dict_from_namedtuple',
    'calculate_largest_blood_type',
    'calculate_mean_current_location',
    'calculate_oldest_person_age',
    ]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 350, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in MANDATORY_FUNCTIONS:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(Dict)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(Dict, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_mandatory_fuctions_availability():
    MANDATORY_FUNCTIONS_AVAILABILITY = True
    f = open("Dict.py", "r")
    content = f.read()
    f.close()
    for c in MANDATORY_FUNCTIONS:
        if c not in content:
            MANDATORY_FUNCTIONS_AVAILABILITY = False
            pass
    assert MANDATORY_FUNCTIONS_AVAILABILITY == True, "You have not implemented all the functions"


def test_dict_avg_age():
    profile_dict = {"0":{"birthdate":datetime.date(1980, 1, 1)}, "1":{"birthdate":datetime.date(2000, 1, 1)}}
    assert Dict.calculate_avg_age(profile_dict)[0] == 30.747433264887064

def test_dict_oldest_age():
    profile_dict = {"0":{"birthdate":datetime.date(1980, 1, 1)}, "1":{"birthdate":datetime.date(2000, 1, 1)}}
    assert Dict.calculate_oldest_person_age(profile_dict)[0] == 40.747433264887064

def test_dict_mean_current_location():
    profile_dict = {"0":{"current_location":(Decimal(20),Decimal(300))}, "1":{"current_location":(Decimal(100),Decimal(400))}}
    assert Dict.calculate_mean_current_location(profile_dict)[0] == (Decimal('60'), Decimal('350'))

def test_dict_largest_blood_grp():
    profile_dict = {"0":{"blood_group":'AB+ve'}, "1":{"blood_group":'AB+ve'}, "2":{"blood_group":'O+ve'}}
    assert Dict.calculate_largest_blood_type(profile_dict)[0] == 'AB+ve'
