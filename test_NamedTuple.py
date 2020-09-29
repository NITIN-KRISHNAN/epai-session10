from decimal import Decimal
from collections import namedtuple
import NamedTuple
import datetime

def test_namedtuple_avg_age():
    ProfileListExt = namedtuple("ProfileListExt", 'a')
    profile_list = ProfileListExt(*(NamedTuple.Profile('job1', 'comp1', 'ssn1', 'res1', (Decimal(20),Decimal(300)), 'AB+ve', 'w', 'u', 'nam2', 'M', 'a', 'mail', datetime.date(2000, 1, 1)),))
    assert NamedTuple.calculate_avg_age(profile_list)[0] == 20.747433264887064

def test_namedtuple_oldest_age():
    ProfileListExt = namedtuple("ProfileListExt", 'a')
    profile_list = ProfileListExt(*(
    NamedTuple.Profile('job1', 'comp1', 'ssn1', 'res1', (Decimal(20), Decimal(300)), 'AB+ve', 'w', 'u', 'nam2', 'M',
                       'a', 'mail', datetime.date(2000, 1, 1)),))
    assert NamedTuple.calculate_oldest_person_age(profile_list)[0] == 20.747433264887064

def test_namedtuple_mean_current_location():
    ProfileListExt = namedtuple("ProfileListExt", 'a')
    profile_list = ProfileListExt(*(
    NamedTuple.Profile('job1', 'comp1', 'ssn1', 'res1', (Decimal(20), Decimal(300)), 'AB+ve', 'w', 'u', 'nam2', 'M',
                       'a', 'mail', datetime.date(2000, 1, 1)),))
    assert NamedTuple.calculate_mean_current_location(profile_list)[0] == (Decimal('20'), Decimal('300'))

def test_namedtuple_largest_blood_grp():
    ProfileListExt = namedtuple("ProfileListExt", 'a')
    profile_list = ProfileListExt(*(
    NamedTuple.Profile('job1', 'comp1', 'ssn1', 'res1', (Decimal(20), Decimal(300)), 'AB+ve', 'w', 'u', 'nam2', 'M',
                       'a', 'mail', datetime.date(2000, 1, 1)),))
    assert NamedTuple.calculate_largest_blood_type(profile_list)[0] == 'AB+ve'