from faker import Faker
import time
import datetime
from NamedTuple import NUM_PROFILE

faker = Faker()


def form_profile_dict():
    profile_dict = {}
    for i in range(NUM_PROFILE):
        profile_dict[i] = faker.profile()
    return profile_dict


def form_profile_dict_from_namedtuple(profile_named_tuple):
    profile_dict = {}
    i = 0
    for profile in profile_named_tuple:
        profile_dict[i] = dict(profile._asdict())
        i += 1
    return profile_dict


def calculate_largest_blood_type(profile_dict):
    """

    :param profileList:
    :return:
    """
    start_time = time.time()
    grp_count = {}
    for profile in profile_dict.values():
        grp = profile['blood_group']
        count = grp_count.get(grp, 0)
        count += 1
        grp_count[grp] = count
        # print(grp_count)
    max_blood_grp = max(grp_count, key = grp_count.get)
    # print(max_blood_grp)
    end_time = time.time()
    return max_blood_grp, end_time-start_time


def calculate_mean_current_location(profile_dict):
    start_time = time.time()
    sum_x = 0
    sum_y = 0
    for profile in profile_dict.values():
        sum_x += profile['current_location'][0]
        sum_y += profile['current_location'][1]
    mean_current_location = sum_x/ NUM_PROFILE, sum_y / NUM_PROFILE
    end_time = time.time()
    return mean_current_location, end_time - start_time


def calculate_oldest_person_age(profile_dict):
    start_time = time.time()
    max_age = max((datetime.date.today() - profile['birthdate']).days for profile in profile_dict.values()) / 365.25
    end_time = time.time()
    return max_age, end_time - start_time


def calculate_avg_age(profile_dict):
    start_time = time.time()
    avg_age = sum((datetime.date.today() - profile['birthdate']).days for profile in profile_dict.values()) / NUM_PROFILE / 365.25
    end_time = time.time()
    return avg_age, end_time - start_time