# importation
import re
import numpy as np

def extract_age(text:str)->int:
    """ look for the age of a patient in a text """

    # parameters
    age = np.nan

    # try to catch something like 'XXX-year-old'
    match = re.findall('([0-9]{1,3})[-\s]year[s]{0,1}[-\s]old', text)
    if(len(match) > 0):
        age = int(match[0])

    # return extracted age
    return age


