# importation
import sys
sys.path.append('scrappers')
sys.path.append('tests')
import test_scrap_age
import test_scrap_gender


if __name__ == "__main__":

    # parameters
    age_test_data = "utils/age.csv"
    gender_test_data = "utils/gender.csv"

    # run test to extact age
    test_scrap_age.test_scrap_age(age_test_data)

    # run test to gender age
    test_scrap_gender.test_scrap_gender(gender_test_data)

