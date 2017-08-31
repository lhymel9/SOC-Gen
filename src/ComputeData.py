from OccupationProfile import OccupationProfile

def remove_not_industry(naics, occup_list):
    filtered = []
    for occup in occup_list:
        if occup[1][:2] == naics:
            filtered.append(occup)

    return filtered

def generate_profiles(occup_list)
    profile_list = []
    for occup in remove_not_industry(occup_list):
        profile_list.append(OccupationProfile(occup[0]))
    
    return profile_list


def make_count(survey_arr, target_arr):
    count = 0
    for word in survey_arr:
        if word in target_arr:
            count = count + 1
    return count

def calc_total(survey, target):
    return calc_single(survey, target, 'title') + calc_single(survey, target, 'description') +
           calc_many(survey, target, 'jobs') + calc_many(survey, target, 'tasks') +
           calc_many(survey, target, 'dwa') + calc_skills(survey, target)

def calc_single(survey, target, key):
    factor = <float> if key == 'title' else factor = <float>
    count = make_count(survey['data'], target[key])
    return count*factor

def calc_many(survey, target, key)
    if key == 'jobs':
        factor = <float>
    elif key == 'tasks':
        factor = <float>
    else:
        factor = <float>

    count = 0
    for arr in target[key]:
        count += make_count(survey['data'], arr)
    return count*factor

def calc_skills(survey, target):
    titles, descriptions =  zip(*target['skills'])
    
    titles_count, descriptions_count = 0, 0
    for arr in list(titles):
        titles_count += make_count(survey['data'], arr)
    for arr in list(descriptions):
        descriptions_count += make_count(survey['data'], arr)

    return titles_count*<float> + descriptions_count*<float>



