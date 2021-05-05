# SetuVaccineAppointmentAlerter
Based on Co-WIN Public APIs. Thanks to Open API Policy.

# Description
SetuVaccineAppointmentAlerter checks the Co-WIN Public APIs periodically to find vaccination slots available for your pin code. If vaccine session is found, it will play an alert sound (ding.wav) and write a CSV and TXT file in dir './CSVs'

# Running the script
You should have python installed on your machine. You can download Python from https://www.python.org/downloads/ Once downloaded, execute following commands

> pip install requests
> pip install fake-useragent

# COWIN APIs Reference

Information regarding APIs can be found at https://apisetu.gov.in/public/marketplace/api/cowin/cowin-public-v2
