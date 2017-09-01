import OccupationProfile as oc
from collections import Counter

def remove_not_industry(naics, occup_list):
    filtered = []
    for occup in occup_list:
        if occup[0][:2] == naics:
            filtered.append(occup)

    return filtered

def generate_profiles(occup_list):
    profile_list = []
    for occup in occup_list:
        profile_list.append(oc.OccupationProfile(occup[0]))
    
    return profile_list


def remove_outliers(survey, occup_profiles):
    filter = []
    for idx in range(0,len(occup_profiles)):
        word_blob = make_blob(idx, occup_profiles,survey['data'])
        for word in occup_profiles[idx].data.all['title']:
            if word not in word_blob:
                filter.append(occup_profiles[idx])
                break
    return [x for x in occup_profiles if x not in filter]

def make_blob(index, occup_profiles, survey):
    final_blob = ""
    for i in range(0, len(occup_profiles)):
        if index != i and occup_profiles[i]:
            shattered_list = [shatter_list(occup_profiles[i].data.all['title']), shatter_list(occup_profiles[i].data.all['description']), shatter_listoflist(occup_profiles[i].data.all['jobs'])]
            shattered = " ".join(shattered_list)
            final_blob = " ".join([final_blob, shattered])
    return final_blob.split(" ")

def shatter_list(unshattered):
    return " ".join(unshattered)

def shatter_listoflist(unshattered):
    result = ""
    for arr in unshattered:
        result = " ".join([result, shatter_list(arr)])
    return result


def calc_total(survey, target):
    #print(target['title'])
    #print("-------------------")
    from_title = calc_single(survey, target, 'title')
    from_description = calc_single(survey, target, 'description')
    from_jobs = calc_many(survey, target, 'jobs')
    #print("From Title: ", from_title)
    #print("From Description: ", from_description)
    #print("From Jobs: ", from_jobs)
    #print("")
    return from_title + from_jobs

def calc_single(survey, target, key):
    if key == 'title': 
        factor = 2.5 
    else: 
        factor = 1.0

    count = make_count(survey['data'], target[key])
    return count*factor

def calc_many(survey, target, key):
    count = 0
    for arr in target[key]:
        count += make_count(survey['data'], arr)
    return count*2.0
    
def make_count(survey_arr, target_arr):
    print("Comparing: " + "[" + ",".join(survey_arr) + "], " + "Against: " + "[" + ",".join(target_arr) + "]")
    count = 0
    for word in survey_arr:
       # print("Is " + word + " in " + ",".join(target_arr) + "?")
        if word.lower() in target_arr:
            #print("yes")
            count = count + 1
    return count


