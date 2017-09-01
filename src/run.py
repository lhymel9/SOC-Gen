import sys
import OccupationProfile as oc
import ExtractSOCData as extract
import ProcessData  as proc
import ComputeData as compute

keywords = "+".join(sys.argv[1:len(sys.argv)-1])
survey = {
    "data": " ".join(sys.argv[1:len(sys.argv)-1]),
    "naics": sys.argv[len(sys.argv)-1]
}

occupations = compute.remove_not_industry(survey['naics'], extract.get_search_results(keywords))

occupation_profiles = compute.generate_profiles(occupations)
survey = proc.process_survey_dict(survey)

ranks = []
for profile in occupation_profiles:
    ranks.append((profile.soc, profile.compute_against(survey)))

ranks = sorted(ranks, key=lambda x:x[1], reverse=True)

print(ranks)