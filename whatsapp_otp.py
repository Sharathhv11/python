import random as r
import time
import pywhatkit as py
from datetime import datetime

def whatsOtp(num):
    #tracking destop time
    c_time = datetime.now().time()
    f_time = str(c_time)
    final_time = f_time.split(":")
    hour = int(final_time[0])
    min = int(final_time[1]) + 2
    if min >= 59:
        min = 1
        hour += 1
    #generating OTP
    dig = [0,1,2,3,4,5,6,7,8,9]
    otp = ""
    for x in range(0, 6):
        gotp = r.choice(dig)
        otp = otp + str(gotp)
    fotp = int(otp)
    if len(otp) == 5:
        otp = otp + str(r.choice(dig))
    mesg=f"your OTP is {fotp}"
    #sending otp through whatsapp
    try:
        py.sendwhatmsg(num,mesg,hour,min)
        str_time=time.time()
    except Exception as e:
        print(e)
    #verifing otp
    inp2 = int(input("enter the OTP>>"))
    end_time=time.time()
    final_time=int(end_time-str_time)
    if final_time<100:
        str1, str2 = str(inp2), str(fotp)
        if inp2 == fotp and len(str1) == len(str2):
            print("otp is right")
    else:
        print("invalid otp / time out")
        time.sleep(5)
        inp3 = input("resend>>yes/no>>")
        if inp3.lower() == "yes":
            whatsOtp(num)


num = input("Enter your number with country code>>")
if num.isnumeric and len(num) == 13:
    whatsOtp(num)
else:
    print("invalid  number/number should be with (+91)country code!!!")