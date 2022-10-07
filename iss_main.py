import requests
import time
from datetime import datetime as dt
import smtplib
my_email="saddikutivishnu2019@iiitkottayam.ac.in"
my_password="ramahyma"

my_lat=17.000538
my_lng=81.804031

def is_iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    data=response.json()
    iss_longitude=float(data["iss_position"]["longitude"])
    iss_latitude=float(data["iss_position"]["latitude"])

    #iss_position=(longitude,latitude)

    #print(iss_position)
    if my_lat-5<= iss_latitude <= my_lat+5 and  my_lng-5<= iss_latitude <= my_lng+5:
         return True
def is_night():
    parameters={
        "lat":my_lat,
        "lng":my_lng,
        "formatted":0
    }
    response=requests.get(url="http://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data=response.json()
    print(data)
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now=dt.now().hour
    #print(sunrise.split("T")[1].split(":")[0])
    if time_now>=sunset or time_now<=sunrise:
        return True



if is_iss_overhead() and is_night():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email,my_password)
    connection.sendmail(from_addr=my_email,to_addrs="kamalakarvishnu.2001@gmail.com",
                            msg=f"Subject:Look Up!\n\nThe ISS is above you in the sky")



