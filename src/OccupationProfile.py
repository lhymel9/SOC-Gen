import ExtractSOCData as extract
import ProcessData as proc
import ComputeData as compute

class DataProfile:
    """ Data componenet for an OccupationProfile """

    def __init__(self, soc_code):
        occup_xml = extract.get_occup_xml(soc_code)
        self._dict = {
            "title": occup_xml.find('title').text,
            "description": occup_xml.find('description').text,
            "jobs": extract.get_job_titles(occup_xml),
            "tasks": extract.get_tasks(soc_code),
            "dwa": extract.get_dwa(soc_code),
            "skills": extract.get_skills(soc_code)
        }

    @property
    def all(self):
        """ @param: self """
        """ @return: DataProfile _dict member """

        return self._dict

    @property
    def processed(self):
        """ @param: self """
        """ @return: DataProfile _dict memeber after application of nltk processing """

        return proc.process_data_dict(self._dict)


    def set_attrib(self, key, value):
        """ @params: self, the dictionary key  element of choice, proposed new value """

        self._dict[key] = value



class OccupationProfile:
    """ Profile for a particular occupation (SOC code) """

    def __init__(self, soc_code):
        self._soc = soc_code
        self._data = DataProfile(soc_code)
        self._total = 0

    @property
    def soc(self):
        """ @param: self """
        """ @return: OccupationProfile _soc member """

        return self._soc

    @property
    def data(self):
        """ @param: self """
        """ @return: OccupationProfile _data member """

        return self._data

    @property
    def total(self):
        """ @param: self """
        """ @return: OccupationProfile _total member """

        return self._total


    def compute_against(self, survey_data):
        """ @param: self, job information survey data (in the form of a dictionary) """
        """ @return: correlation total between the survey data and OccupationProfile _data memeber """

        computed = compute.compute_score(self._data, survey_data)
        self._total = computed

        return computed
