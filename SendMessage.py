# -*- coding:utf-8 -*-
import http.client
import urllib.parse
host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"
account = "C95966820"
password = "2b6907e898646cd8b4e0cefe72a5bffb"

def send_sms(number, mobile):
    text = "您的验证码是：%d。请不要把验证码泄露给其他人。" % (number)
    params = urllib.parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    print(response_str.decode('raw_unicode_escape'))
    return
