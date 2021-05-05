# SetuVaccineAppointmentAlerter
Based on Co-WIN Public APIs. Thanks to Open API Policy.

# Description
SetuVaccineAppointmentAlerter checks the Co-WIN Public APIs periodically to find vaccination slots available for your pin code. If vaccine session with appointment is found, details of same will be displayed with an alert sound (ding.wav). Also, CSV and TXT file will be created in dir './CSVs, each time an appointment is found'

# Running the script
You should have python installed on your system. You can download Python from https://www.python.org/downloads/ 
After installing Python, execute following commands in Powershell/CMD for windows or Terminal on Linux/Unix systems.

>>> ## pip install requests
```Shell
      $ pip install fake-useragent
      $ pip install playsound
```

>>> ## Finally to Run the script
>>> Open Powershell/CMD or Terminal at the location and run using follwoing command
```shell
      $ python main.py
```




# COWIN APIs Reference

Information regarding APIs can be found at https://apisetu.gov.in/public/marketplace/api/cowin/cowin-public-v2
