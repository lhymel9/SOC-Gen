from nltk.corpus import stopwords

def process_data_dict(dictionary):
    """ @param: A DataProfile _dict member """
    """ @return: A processed (ready for comparison) DataProfile _dict member """

    processed_dict = {
        "title": preprocess_str(dictionary["title"]),
        "description": preprocess_str(dictionary["description"]),
        "jobs": preprocess_str_list(dictionary["jobs"]),
        "tasks": preprocess_str_list(dictionary["tasks"]),
        "dwa": preprocess_str_list(dictionary["dwa"]),
        "skills": preprocess_tup_list(dictionary["skills"])
    }
    return processed_dict


def preprocess_str(single):
    """ @param: A string """
    """ @return: A lowercased, stopped, split list of the string """

    stops = set(stopwords.words('english'))
    return [word for word in single.lower().split() if word.isalpha() and word not in stops]


def preprocess_str_list(arr):
    """ @param: A list of strings """
    """ @return: A lowercased and stopped list """

    stops = set(stopwords.words('english'))
    return [word.lower() for word in arr if word.isalpha() and word not in stops]


def preprocess_tup_list(arr):
    """ @param: A list of 2-variable string tuples """
    """ @return: A lowercased and stopped list of 2-variable string tuples """

    titles, descriptions = zip(*arr)
    titles = preprocess_str_list(list(titles))
    descriptions = preprocess_str_list(list(descriptions))
    return list(zip(titles, descriptions))