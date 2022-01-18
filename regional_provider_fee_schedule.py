import csv
import json
import requests
from decouple import config


def regional_provider_fee_schedule():
    # neuropsych_list = 'optum_neuropsych_ny.csv'
    neuropsych_list = 'optum_neuropsych_non_ny.csv'

    with open(neuropsych_list) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
            else:
                # print(list_to_dict(row))
                create_new_line(list_to_dict(row))
            line_count += 1


def list_to_dict(row):
    keys = ["cptCode", "providerType", "amount"]
    res_dct = dict(zip(keys, row))
    res_dct["amount"] = res_dct["amount"].strip().replace('$', '')
    return res_dct


def create_new_line(dict):
    front_end_carriers = [10, 11, 23]
    ny_regions = [33, 34, 35, 36, 37, 38, 39]
    # regions = ny_regions ## NY REGIONS
    regions = list(set(range(1, 57)) - set(ny_regions))  # NON NY REGIONS

    for x in front_end_carriers:
        for y in regions:
            dict["frontEndCarrierId"] = x
            dict["effectiveDate"] = "2022-01-01T17:00:00.000Z"
            dict["providerRegionId"] = y
            rev_dict = {"feeSchedules": [dict]}
            json_body = json.dumps(rev_dict, indent=4)
            print(json_body)
            post_new_lines(json_body)


def post_new_lines(json_body):
    base_url = config('BASE_URL')
    auth = config('AUTH')

    x = requests.post(base_url, data=json_body, headers={
                      "Authorization": auth})

    print(x.text)
    print(x.status_code)


def main():
    regional_provider_fee_schedule()


if __name__ == '__main__':
    main()
