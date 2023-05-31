# importation
import re
import numpy as np

def extract_gender(text:str)->int:
    """ look for the gender of a patient in a text
        * 1 for male
        * 0 for female
    """

    # parameters
    gender = np.nan

    # try to catch something like 'XXX-year-old XXX'
    match = re.findall('[0-9]{1,3}[-\s]year[s]{0,1}[-\s]old\s([woman|female|girl])', text)
    if(len(match) > 0):
        gender = 0

    match = re.findall('[0-9]{1,3}[-\s]year[s]{0,1}[-\s]old\s([man|male|boy])', text)
    if(len(match) > 0):
        gender = 1

    # return extracted gender
    return gender

