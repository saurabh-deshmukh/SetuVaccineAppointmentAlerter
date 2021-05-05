import urllib.request
import urllib.error
import json
import os


os.makedirs('./metadata', mode=777, exist_ok=True)
path = './metadata/'
stateID_url = 'https://cdn-api.co-vin.in/api/v2/admin/location/states'
districtID_baseurl = 'https://cdn-api.co-vin.in/api/v2/admin/location/districts/'
states = {}
state_destricts = {}
districtsids = {}

def getstateids():
    stateidcsv = str()
    try:
        data = urllib.request.urlopen(stateID_url)
    except urllib.error.HTTPError as e:
        print(f'Could not get latest "state IDs"\nError {e.code}: {e.reason}')
    finally:
        sidjson = json.loads(data.read())
        # print(str(states).replace(', ','\n'))
        for i in sidjson["states"]:
            stateidcsv = "{0}\n{1},{2}".format(stateidcsv, i["state_name"], i["state_id"])
            states[i["state_name"]] = i["state_id"]
        del data, sidjson
        f = open(f'{path}stateID.csv', 'w+')
        f.write(stateidcsv)
        f.close()
        t = open(f'{path}stateID.txt', 'w+')
        t.write(stateidcsv.replace(',', ': '))
        t.close()
        return states


def getdistid():
    distidcsv = str()
    if not bool(states):
        getstateids()
    for k, v in states.items():
        districtID_url = f'{districtID_baseurl}{v}'
        data = urllib.request.urlopen(districtID_url)
        didjson = json.loads(data.read())
        for i in didjson["districts"]:
            state_destricts[i["district_name"]] = k
            districtsids[i["district_name"]] = i["district_id"]
            distidcsv = f'{distidcsv}\n{k},{i["district_name"]},{i["district_id"]}'
    print(state_destricts.items())
    print(districtsids.items())
    f = open(f'{path}districtid.csv', 'w+')
    f.write(distidcsv)
    f.close()
    t = open(f'{path}district.txt', 'w+')
    t.write(distidcsv.replace(',', '\t'))
    t.close()


if __name__ == "__main__":
    getstateids()
    getdistid()







