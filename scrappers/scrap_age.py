# importation
import re
import numpy as np

def extract_age(text:str)->int:
    """ """

    # parameters
    age = np.nan

    # try to catch something like 'XXX-year-old'
    match = re.findall('([0-9]{1,3})[-\s]year[s]{0,1}[-\s]old', text)
    if(len(match) > 0):
        age = int(match[0])



    # return extracted age
    return age






if __name__ == "__main__":
    
    text = "Case one: A 20-year-old man of Dravidian origin presented to our out-patient department with a complaint of facial asymmetry, difficulty in speech, and loss of taste sensation over the last 2 years"
    text = " Case two: A 53-year-old woman ﻿of Dravidian origin presented to our out-patient department with a complaint of gradually decreasing mouth opening over the past 7 years"
    text = "We describe a 40-year-old woman with systemic scleroderma who had hundreds of firm nodules that developed on the trunk and upper extremities during several months"
    text = "We report a case of a 13 year-old female presenting with widespread skin thickening and joint contractures from infancy"
    age = extract_age(text)
    print(age)
