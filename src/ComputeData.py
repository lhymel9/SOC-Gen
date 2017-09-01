import OccupationProfile as oc

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


def make_count(survey_arr, target_arr):
    count = 0
    for word in survey_arr:
        if word in target_arr:
            count = count + 1
    return count

def calc_total(survey, target):
    return calc_single(survey, target, 'title') + calc_single(survey, target, 'description') + calc_many(survey, target, 'jobs') + calc_many(survey, target, 'tasks') + calc_many(survey, target, 'dwa') + calc_skills(survey, target)

def calc_single(survey, target, key):
    if key == 'title': 
        factor = 2.5 
    else: 
        factor = 1.0

    count = make_count(survey['data'], target[key])
    return count*factor

def calc_many(survey, target, key):
    if key == 'jobs':
        factor = 2.0
    else:
        factor = 0.5

    count = 0
    for arr in target[key]:
        count += make_count(survey['data'], arr)
    return count*factor

def calc_skills(survey, target):
    try:
        titles, descriptions =  zip(*target['skills'])
    except ValueError:
        return 0
    
    titles_count, descriptions_count = 0, 0
    for arr in list(titles):
        titles_count += make_count(survey['data'], arr)
    for arr in list(descriptions):
        descriptions_count += make_count(survey['data'], arr)

    return titles_count*1.5 + descriptions_count*0.5



