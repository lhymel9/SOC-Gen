from nltk.corpus import stopwords as sw
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

stops = set(sw.words('english'))
wnl = WordNetLemmatizer()

def process_data_dict(dictionary):
    """ @param: A DataProfile _dict member """
    """ @return: A processed (ready for comparison) DataProfile _dict member """

    processed_dict = {
        "title": preprocess_str(dictionary["title"]),
        "description": preprocess_str(dictionary["description"]),
        "jobs": preprocess_str_list(dictionary["jobs"])
    }
    return processed_dict

def process_survey_dict(dictionary):
    """ @param: A dictionary formed from job survey data (similar to DataProfile _dict member) """
    """ @return: A processed (ready for comparison) job survey data dictionary """

    processed_dict = {
        "data": preprocess_str(dictionary["data"]),
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