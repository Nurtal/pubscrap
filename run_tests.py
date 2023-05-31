# importation
import sys
sys.path.append('scrappers')
sys.path.append('tests')
import test_scrap_age


if __name__ == "__main__":

    # parameters
    age_test_data = "utils/age.csv"

    # run test to extact age
    test_scrap_age.test_scrap_age(age_test_data)

