import urllib.request
import urllib.error
import json
import datetime
from playsound import playsound
import os
from fake_useragent import UserAgent


ua = UserAgent()


def checkappointments(jsn, v=False, age = 18):
    aflag = int(0)
    for i in jsn["centers"]:
        if v:
            print(f'\nName:\t\t{i["name"]}\nAddress:\t{i["block_name"]} {i["district_name"]} {i["pincode"]} '
                  f'{i["state_name"]}\nTiming: \t{i["from"]} to {i["to"]}\nVaccine Fee: \t{i["fee_type"]}')
        for n, j in enumerate(i["sessions"]):
            if v:
                print(f'_____Sessions:_____\n\tSession ID:\t\t{j["session_id"]}\n\tDate:\t\t{j["date"]}'
                      f'\n\tAvailable:\t{j["available_capacity"]}\n\tMin Age:\t{j["min_age_limit"]}'
                      f'\n\tVaccine:\t{j["vaccine"]}\n\t_____Slots:_____')
            for k in j["slots"]:
                if v:
                    print(f'\t\t{k}')

            if (j["min_age_limit"] == age) & (j["available_capacity"] != 0):
                aflag += 1
                if not v:
                    print(f'\nDate:\t\t{j["date"]}\nName:\t\t{i["name"]}\n'
                          f'Address 1:\t{i["address"]}\n'
                          f'Address 2:\t{i["block_name"]} {i["district_name"]} {i["pincode"]}\n'
                          f'Available:\t{j["available_capacity"]} appointment(s)\n'
                          f'Type: \t\t{i["fee_type"]} {j["vaccine"]}')
                    print('\n-------xx-------xx-------xx-------xx-------')
                playsound('C:/Users/SSD.SAURABH/OneDrive/Documents/Python_workspace/API/ding.wav')
                # input("Press enter to continue")
    return int(aflag)


def createcsvstr(jsn):
    s = str()
    for i in jsn["centers"]:
        for n, j in enumerate(i["sessions"]):
            s = s + f'{i["name"]},' \
                    f'{i["block_name"]},{i["district_name"]},{i["pincode"]},' \
                    f'{i["from"]},{i["to"]},' \
                    f'{i["fee_type"]},{j["date"]},{j["available_capacity"]},{j["min_age_limit"]},{j["vaccine"]},'
            for k in j["slots"]:
                s = s + f'{k},'
            s = s + f'{j["session_id"]}'
            s = s + '\n'
    return s


def writetofile(csvstring, pins):
    os.makedirs('./CSVs', mode=777, exist_ok=True)
    path = './CSVs/'
    f_name = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    f_pin = str(pins[0]) + str(pins[len(pins) - 1])
    f = open('./sethu_CSVs/' + str(f_name) + "_" + f_pin + '.csv', 'w+')
    f.write(csvstring)
    f.close()
    t = open('./sethu_CSVs/' + str(f_name) + "_" + f_pin + '.txt', 'w+')
    t.write(csvstring.replace(',', '\t'))
    t.close()
    del f, t, f_name, f_pin


def setu(pins, v=False, createcsv=False, age=18):
    dt = datetime.datetime.now()
    cweb_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?"
    counter = 0
    if not v:
        print("Searching", end="", flush=True)

    # CSV Header
    csv_string = f'Date (YYYY-MM-DD),{dt.strftime("%Y-%m-%d")},,,,Start,End' \
                 f'\nTime (HH:MM:SS),{dt.strftime("%I:%M:%S %p")},,,Pincodes,{pins[0]},{pins[len(pins) - 1]}' \
                 f'\n\nName,Block,District,Pincode,sTime,eTime,Fee,Date,Available,Min-Age,Vaccine, Slot1,' \
                 f'Slot2, Slot3, Slot4\n'

    # Loop over all the pins
    for n, pin in enumerate(pins):
        # Create Request URL
        url = cweb_url + "pincode=" + str(pin) + "&date=" + str(dt.strftime("%d-%m-%Y"))
        # Open Url
        try:
            req = urllib.request.Request(url, data=None,
                                             headers={'User-Agent': ua.random})
            web_url= urllib.request.urlopen(req)
            data = web_url.read()
            jsn = json.loads(data)
            counter += checkappointments(jsn, v, age)
            csv_string = "{0}{1}".format(csv_string, createcsvstr(jsn))
        except urllib.error.HTTPError as e:
            print(f'Pincode {pin}: Error {e.code}: {e.reason}')
        if (not v) & (counter == 0):
            print('.', end="", flush=True)
            if (n % 54 == 0) & (n != 0):
                print('\n\t  ', end="", flush=True)

    # If appointments available
    if (counter != 0) or createcsv:
        print(f'\nAppointments available for {counter} vaccination session(s)\n\nWriting csv and txt files')
        writetofile(csv_string, pins)

    # If appointments not found
    if counter == 0:
        print("\n\nSorry! No appointments available.")


    print('\n-------xx-------xx-------xx-------xx-------'
          '\n\t\tSearch Complete'
          '\n-------xx-------xx-------xx-------xx-------')

    try:
        del csv_string, pins, counter
    except UnboundLocalError:
        print("Failed to delete one or more variables")



if __name__ == "__main__":
    setu(v=False, createcsv=False, age = 18)
