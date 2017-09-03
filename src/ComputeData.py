import OccupationProfile as oc
from collections import Counter

"""
def remove_not_industry(naics, occup_list):
    filtered = []
    for occup in occup_list:
        if occup[0][:2] == naics:
            filtered.append(occup)

    return filtered
"""

def has_dec(code):
    for c in code[-2:]:
        if c != '0':
            return True
    return False

def generate_profiles(occup_list):
    return [oc.OccupationProfile(occup[0]) for occup in occup_list if not has_dec(occup[0])]

def remove_outliers(survey, occup_profiles):
    profile_filter = []
    word_blob = make_blob(occup_profiles, survey['data'])
    word_counts = Counter(word_blob)
    for idx in range(0,len(occup_profiles)):
        for word in occup_profiles[idx].data.all['title']:
            if word_counts[word] < 6 and word not in survey['data']:
                profile_filter.append(occup_profiles[idx])
                break
    return [x for x in occup_profiles if x not in profile_filter]

def make_blob(occup_profiles, survey):
    final_blob = ""
    for i in range(0, len(occup_profiles)):
        shattered_list = shatter_list(occup_profiles[i].data.all['title']) + shatter_listoflist(occup_profiles[i].data.all['jobs'])
        final_blob = final_blob + " " + shattered_list.rstrip()
    return final_blob

def shatter_list(unshattered):
    return " ".join(unshattered)

def shatter_listoflist(unshattered):
    result = ""
    for arr in unshattered:
        result += shatter_list(arr) + " "
    return result


def calc_total(survey, target):
    from_title = calc_single(survey, target, 'title')
    from_description = calc_single(survey, target, 'description')
    from_jobs = calc_many(survey, target, 'jobs')
    return from_title + from_jobs

def calc_single(survey, target, key):
    if key == 'title': 
        factor = 3.0 
    else: 
        factor = .15

    count = make_count(survey['data'], target[key])
    return count*factor

def calc_many(survey, target, key):
    count = 0
    for arr in target[key]:
        count += make_count(survey['data'], arr)
    return count*1.5
    
def make_count(survey_arr, target_arr):
    count = 0
    for word in survey_arr:
        if word.lower() in target_arr:
            count = count + 1
    return count


