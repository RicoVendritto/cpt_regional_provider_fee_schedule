import csv
import requests


def insurance_fee_schedules():

    with open('optum_neuropsych_insurance.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
            else:
                post_new_line(list_to_dict(row))
                # print(list_to_dict(row))
            line_count += 1


def list_to_dict(row):
    keys = ["cptCode", "providerType", "amount"]
    res_dct = dict(zip(keys, row))
    nest_dct = "feeSchedules": [res_dct]}
    return res_dct


def post_new_line(row):
    auth_string = "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJiMWMzOGE4Y2JhMTZmYmJjMjg2YjIzZDY4ZWM4ODMxMDVlNjU0Yjc3OWNhNWMzYjA4ZDMzZjI2MTJjZGQ1N2RlIiwic3ViIjoiOSIsImV4cCI6MTY0MjE1NDQwMCwiaXNzIjoiSGVhZHdheSIsInNjb3BlcyI6WyJkZWZhdWx0Il0sImlhdCI6MTY0MjEwOTE5Miwicm9sZXMiOlsiQVRMQVNfVVNFUiIsIlpPQ0RPQyIsIkFETUlOIiwiUFJPVklERVJfSU1QRVJTT05BVE9SIiwiUEFUSUVOVF9JTVBFUlNPTkFUT1IiXX0.fnpLLuLDKuMOILluSZsNxFNScS0540q_P84f0CO4J5Y"
    url = "localhost:5000/insurance-fee-schedule"

    response = requests.post(url, data=row, headers={
                             "authorization": auth_string, "Content-Type": "application/json"})
    print(response.status_code)


if __name__ == '__main__':
    insurance_fee_schedules()
