import sys
import OccupationProfile as oc
import ExtractSOCData as extract
import ProcessData  as proc
import ComputeData as compute

import pandas as pd

def run_main(keywords):
    print("Searching... " + keywords)
    survey = {
        "data": keywords
    }

    keywords_search = proc.preprocess_str(keywords)
    occupations = extract.get_search_results("+".join(keywords_search))

    survey = proc.process_survey_dict(survey)
    profiles = compute.generate_profiles(occupations)
    occupation_profiles = compute.remove_outliers(survey, profiles)

    print("Found: ",len(profiles))
    print("Removed: ",len(profiles)-len(occupation_profiles))

    ranks = []
    for profile in occupation_profiles:
        if profile:
            ranks.append((profile.soc, profile.compute_against(survey)," ".join(profile.data.all['title'])))

    ranks = sorted(ranks, key=lambda x:x[1], reverse=True)
    
    if ranks:
        return ",".join([keywords,ranks[0][0],ranks[0][2]]) + "," + str(ranks[0][1])
    return keywords + ",Null,Null,Null"


def format(unformated):
    return ''.join([c for c in unformated if c.isalpha() or c.isspace()])


with open('./data/in') as f:
    keywords = f.read()
f.closed

keywords = keywords.split(',')

results = []
for kw in keywords:
    search = format(kw)
    results.append(run_main(search))

with open('./data/out', 'w') as out:
    out.write('Search Criteria,SOC_Code,SOC_Name,Score\n')
    for result in results:
        out.write(result + '\n')
out.closed