# importation
import pandas as pd
import scrap_age


def test_scrap_age(data_file):
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
        assert scrap_age.extract_age(text) == expected

        # update test cmpt
        cmpt+=1

    # display success
    print(f"[TEST][AGE] => SUCCESS ({cmpt} tests performed)")

