from nltk.corpus import stopwords as sw
from nltk.stem import WordNetLemmatizer

stops = set(sw.words('english'))
wnl = WordNetLemmatizer()

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

def process_survey_dict(dictionary):
    """ @param: A dictionary formed from job survey data (similar to DataProfile _dict member) """
    """ @return: A processed (ready for comparison) job survey data dictionary """

    processed_dict = {
        "data": preprocess_str(dictionary["data"]),
        "naics": dictionary["naics"]
    }
    return processed_dict


def preprocess_str(single):
    """ @param: A string """
    """ @return: A lowercased, stopped, split, unique list of the string """

    unlemmatized = [word for word in single.lower().split() if word.isalpha() and word not in stops]
    return uniquify([wnl.lemmatize(word) for word in unlemmatized])

def preprocess_str_list(arr):
    """ @param: A list of strings """
    """ @return: A list of lists of lowercased and stopped words """

    if arr:
        return [preprocess_str(statement) for statement in arr]
    return []

def preprocess_tup_list(arr):
    """ @param: A list of 2-variable string tuples """
    """ @return: A list of 2-variable list, lowercased, stopped, string tuples """
    
    if arr:
        titles, descriptions = zip(*arr) #unzip operation
        titles = preprocess_str_list(list(titles))
        descriptions = preprocess_str_list(list(descriptions))
        return list(zip(titles, descriptions))
    return []


def uniquify(arr):
    """ @param: A list of strings """
    """ @return: The same list with duplicate elements removed """

    if has_dup(arr):
        return list(set(arr))
    return arr

def has_dup(arr):
    """ @param: A list of strings """
    """ @return: A boolean value corresponding to whether or not the input list has unique elements """

    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False