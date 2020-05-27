# coding=utf-8

import requests

"""
response header:
Connection: keep-alive
Content-Length: 157
Content-Type: text/html
Date: Wed, 20 May 2020 01:54:32 GMT
Set-Cookie: Sessionid=2773343261-1;Expires=Fri, 19 Jun 2020 09:54:32 GMT;Path=/;HttpOnly
Set-Cookie: AUTHSESSID=f2196c24e906; HttpOnly;Secure;
X-Frame-Options: SAMEORIGIN
X-Frame-Options: SAMEORIGIN

request header:


"""
if __name__ == '__main__':
    url = "http://1.1.1.2/ac_portal/login.php"

    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "60",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "1.1.1.2",
        "Origin": "http://1.1.1.2",
        "Referer": "http://1.1.1.2/ac_portal/default/pc.html?tabs=pwd",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    params = {
        "opr": "pwdLogin",
        "userName": "19030237",
        "pwd": "Lujiang-618",
        "rememberPwd": 1,
    }

    # python中的bool真是True
    response = requests.post(url, data=params, headers=header, timeout=3)

    if response.status_code == 200:
        result = response.text.replace("true", 'True')
        result = eval(result)

        if result['success']:
            print("success!")
        else:
            print("failed!")
    else:
        print("failed!")

    print(response.text)
