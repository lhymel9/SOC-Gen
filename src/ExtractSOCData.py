from urllib.request import urlopen, Request, HTTPError
import xml.etree.ElementTree as ET

"""                                 Access Functions                                    """

def get_xml(page_url):
    """ @param: A string link to a particular O*NET API endpoint """
    """ @return: An xml tree associated with the entered API endpoint """

    req = Request(page_url)
    req.add_header('Authorization',
                       'Basic <O*NET_Dev_Key>')
    page_xml = ET.fromstring(urlopen(req).read())

    return page_xml


def get_search_results(keyword):
    """ @param: A keyword used to search the O*NET system """
    """ @return: A list of 2-variable tuples -> [(<soc>, <Occupation Title>), ...] """

    occupTuples = []
    keyword = keyword.replace(" ", "+")

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


def get_dwa_xml(soc_code):
    """ See get_xml function """

    url = 'https://services.onetcenter.org/ws/online/occupations/' + soc_code + '/summary/detailed_work_activities'
    tree = get_xml(url)

    return tree


def get_skills_xml(soc_code):
    """ See get_xml function """

    url = 'https://services.onetcenter.org/ws/online/occupations/' + soc_code + '/summary/skills'
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


def get_occup_descr(tree):
    """ @param: An xml tree for a particular occupation page """
    """ @return: A string description of an occupation associated with a particular soc code -> Ex. "Perform duties that are instructional in nature or deliver..." """

    return tree.find('description').text


def get_tasks(soc_code):
    """ @param: A string soc code corresponding to a particular occupation """
    """ @return: A list of string task descriptions corresponding to each task for a particular occupation -> [<Task 1 Description>, <Task 2 Description>, ... , <Task N Description>] """

    tree = get_task_xml(soc_code)

    return list(map(get_tag_text, tree.findall('task')))


def get_dwa(soc_code):
    """ @param: A string soc code corresponding to a particular occupation """
    """ @return: A list of string task descriptions corresponding to each DWA for a particular occupation -> [<DWA 1 Description>, <DWA 2 Description>, ... , <DWA N Description>] """

    tree = get_dwa_xml(soc_code)

    return list(map(get_tag_text, tree.findall('activity')))


def get_skills(soc_code):
    """ @param: A string soc code corresponding to a particular occupation """
    """ @return: A list of skill title and description tuples corresponding to each skill for a particular occupation -> [(<Skill 1 Title>, <Skill 1 Description>), ... , (<Skill N Title>, <Skill N Description>)] """

    titles, descriptions = [], []

    try:
        tree = get_skills_xml(soc_code)
    except HTTPError:
        return []

    for elem in tree.findall('element'):
        titles.append(elem.find('name').text)
        descriptions.append(elem.find('description').text)
            
    return list(zip(titles, descriptions))
