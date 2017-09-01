from urllib.request import urlopen, Request, HTTPError
import xml.etree.ElementTree as ET

"""                                 Access Functions                                    """

def get_xml(page_url):
    """ @param: A string link to a particular O*NET API endpoint """
    """ @return: An xml tree associated with the entered API endpoint """
    try:
        req = Request(page_url)
        req.add_header('Authorization', 'Basic c3RhdGFfcXVlcnk6MzI3NnVjeg==')
        page_xml = ET.fromstring(urlopen(req).read())
    except HTTPError:
        return None

    return page_xml


def get_search_results(keyword):
    """ @param: A keyword used to search the O*NET system """
    """ @return: A list of 2-variable tuples -> [(<soc>, <Occupation Title>), ...] """

    occupTuples = []

    url = 'https://services.onetcenter.org/ws/online/search?keyword=' + keyword
    searched_xml = get_xml(url)

    for occup in searched_xml.findall('occupation'):
        occupTuples.append((occup.find('code').text,occup.find('title').text))

    return occupTuples



"""                                 XML HTTP Functions                                  """

def get_occup_xml(soc_code):
    """ See get_xml function """

    url = 'https://services.onetcenter.org/ws/online/occupations/' + soc_code + '/'
    tree = get_xml(url)

    return tree


def get_task_xml(soc_code):
    """ See get_xml function """

    url = 'https://services.onetcenter.org/ws/online/occupations/' + soc_code + '/summary/tasks'
    tree = get_xml(url)

    return tree



"""                                 Map Functions                                   """

def get_tag_text(elem):
    """ @param: A tag element from an Element Tree object """
    """ @return: A string description associated with the entered element -> Ex. "Provide extra assistance to students with special needs, ..." """

    return elem.text



"""                                     Drivers                                         """

def get_job_titles(tree):
    """ @param: An xml tree for a particular occupation page """
    """ @return: A list of job titles associated with a particular soc code -> [<Job Title 1>, <Job Title 2>, ... , <Job Title N>] """

    titles = []
    title_samples = tree.find('sample_of_reported_job_titles')
        
    if title_samples:
        titles = [title.text for title in title_samples.findall('title')]

    return titles
