from faker import Faker
from collections import namedtuple
import time
import datetime

faker = Faker()

NUM_PROFILE = 5
Profile = namedtuple('Profile', 'job, company, ssn, residence, current_location, blood_group, website, username, name, sex, address, mail, birthdate')
ProfileList = namedtuple('ProfileList', list(range(NUM_PROFILE)), rename=True)


# def timeit(method):
#     def timed(*args, **kw):
#         ts = time.time()
#         result = method(*args, **kw)
#         te = time.time()
#         if 'log_time' in kw:
#             name = kw.get('log_name', method.__name__.upper())
#             kw['log_time'][name] = int((te - ts) * 1000)
#         else:
#             print('%r  %2.2f ms' % \
#                   (method.__name__, (te - ts) * 1000))
#         return result
#     return timed


def form_profile_list():
    """

    :return:
    """
    profile_tuple_list = list()
    for i in range(NUM_PROFILE):
        profile_tuple_list.append(Profile(**faker.profile()))
    profileList = ProfileList(*profile_tuple_list)
    return profileList


def calculate_largest_blood_type(profileList):
    """

    :param profileList:
    :return:
    """
    start_time = time.time()
    grp_count = {}
    for profile in profileList:
        grp = profile.blood_group
        count = grp_count.get(grp, 0)
        count += 1
        grp_count[grp] = count
        # print(grp_count)
    max_blood_grp = max(grp_count, key = grp_count.get)
    # print(max_blood_grp)
    end_time = time.time()
    return max_blood_grp, end_time-start_time


def calculate_mean_current_location(profileList):
    start_time = time.time()
    sum_x = 0
    sum_y = 0
    for profile in profileList:
        sum_x += profile.current_location[0]
        sum_y += profile.current_location[1]
    mean_current_location = sum_x/ NUM_PROFILE, sum_y / NUM_PROFILE
    end_time = time.time()
    return mean_current_location, end_time - start_time


def calculate_oldest_person_age(profileList):
    start_time = time.time()
    max_age = max((datetime.date.today() - profile.birthdate).days for profile in profileList) / 365.25
    end_time = time.time()
    return max_age, end_time - start_time


def calculate_avg_age(profileList):
    start_time = time.time()
    avg_age = sum((datetime.date.today() - profile.birthdate).days for profile in profileList) / NUM_PROFILE / 365.25
    end_time = time.time()
    return avg_age, end_time - start_time