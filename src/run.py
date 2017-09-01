import sys
import OccupationProfile as oc
import ExtractSOCData as extract
import ProcessData  as proc
import ComputeData as compute

def run_main(keywords, industry):
    survey = {
        "data": keywords,
        "naics": industry
    }

    print("Searching... " + industry + " " + keywords)
    occupations = compute.remove_not_industry(survey['naics'], extract.get_search_results(keywords))
    print("Found: " + str(len(occupations)) + " results")

    survey = proc.process_survey_dict(survey)
    profiles = compute.generate_profiles(occupations)
    occupation_profiles = compute.remove_outliers(survey, profiles)

    ranks = []
    for profile in occupation_profiles:
        if profile:
            ranks.append((profile.soc, profile.compute_against(survey)," ".join(profile.data.all['title'])))

    ranks = sorted(ranks, key=lambda x:x[1], reverse=True)
    
    if ranks:
        return ",".join([keywords,ranks[0][0],ranks[0][2]]) + " at " + str(ranks[0][1])
    return keywords + ",Null"