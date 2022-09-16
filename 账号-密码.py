import os
import uuid
import time
import requests
import socket
from json import loads
from urllib import request

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'}


def automatic_logon(userid, passwd):
    net_request_no1 = request.urlopen('http://1.1.1.1/', timeout=2)
    url = net_request_no1.geturl()
    if not url.find("logout.html"):
        net_request_no2 = request.urlopen('http://2.2.2.2/')
        url_str = net_request_no2.geturl()[32:]
        net_request_no3 = requests.get(
            f'http://192.168.251.75/PortalJsonAction.do?{url_str}&viewStatus=1', timeout=(5, 5), headers=headers)
        personal_info = loads(net_request_no3.text)
        wlanacIp = personal_info['serverForm']['serverip']
        wlanacname = personal_info['serverForm']['servername']
        timestamp = str(personal_info['portalconfig']['timestamp'])
        uuid_my = personal_info['portalconfig']['uuid']
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        wlanuserip = s.getsockname()[0]
        s.close()
        address = hex(uuid.getnode())[2:]
        mac = '%3A'.join(address[i:i + 2] for i in range(0, len(address), 2))
        net_request_no4 = requests.get(f'http://192.168.251.75/quickauth.do?'
                                       f'userid={userid}&passwd={passwd}&'
                                       f'wlanuserip={wlanuserip}&wlanacname={wlanacname}&'
                                       f'wlanacIp={wlanacIp}&ssid=&vlan=0&'
                                       f'mac={mac}&version=0&portalpageid=1&'
                                       f'timestamp={timestamp}&'
                                       f'uuid={uuid_my}&'
                                       f'portaltype=&hostname=', timeout=(5, 5), headers=headers)
        live_status = loads(net_request_no4.text)['code']
        if live_status == '0':
            print('登录成功')
        else:
            print('登录失败')
            time.sleep(3)
    else:
        print('已登录')


if __name__ == '__main__':
    # 获取当前文件名
    file_name = os.path.basename(__file__)
    base_name = os.path.splitext(file_name)[0]
    uid = base_name[:8]
    password = base_name[9:]
    automatic_logon(uid, password)
