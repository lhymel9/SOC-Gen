import OccupationProfile as oc
from collections import Counter
import edit_distance as ed

from difflib import SequenceMatcher

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
    word_blob = make_blob(occup_profiles, survey['data']).split(' ')
    word_counts = Counter(word_blob)
    for idx in range(0,len(occup_profiles)):
        for word in occup_profiles[idx].data.all['title']:
            if similarity(" ".join(survey['data'])," ".join(occup_profiles[idx].data.all['title'])) < 2.2:
            #if word_counts[word]-6 > Counter(occup_profiles[idx].data.all['title'])[word] and word not in survey['data']:
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
        factor = 5.0
    else: 
        factor = 0.5

    count = make_count(survey['data'], target[key])
    return count*factor

def calc_many(survey, target, key):
    count = 0
    for arr in target[key]:
        count += make_count(survey['data'], arr)
    return count*2.5
    
def make_count(survey_arr, target_arr):
    count = 0
    for word1 in survey_arr:
        for word2 in target_arr:
            if similarity(word1, word2) >= 0.9:
                count += 1
    return count

def similarity(word1, word2):
    count = 0
    if len(word1) > len(word2):
        for c2 in word2:
            for c1 in word1:
                if c1 == c2:
                    count += 1
        return count/len(word2)
    else:
        for c1 in word1:
            for c2 in word2:
                if c1 == c2:
                    count += 1
        return count/len(word1)


