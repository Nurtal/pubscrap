# importation
import pandas as pd
import scrap_gender


def test_scrap_gender(data_file):
    """ """

    # parameters
    cmpt = 0

    # load data
    df = pd.read_csv(data_file)

    # loop over data 
    for index, row in df.iterrows():
        
        # extract information
        test_id = row["ID"]
        text = row["TEXT"]
        expected = int(row["EXPECTED"])

        # run function
        assert scrap_gender.extract_gender(text) == expected

        # update test cmpt
        cmpt+=1

    # display success
    print(f"[TEST][GENDER] => SUCCESS ({cmpt} tests performed)")

