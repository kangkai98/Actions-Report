# coding: utf-8

import datetime
import sys
import time
import traceback
from time import sleep
from numpy import random

from send_notify import *
from get_inform import get_inform
from seu_report import seu_report

if __name__ == '__main__':
    inform = get_inform()
    username = inform.seu['username']
    password = inform.seu['password']
    name = inform.seu['name']
    serverchan = inform.serverchan
    try:
        sleep(random.uniform(5, 15))
        date_time = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        print("时间:", date_time)
        province = ''
        city = ''
        district = ''
        lat = ''
        lon = ''
        res = seu_report(username, password, province, city, district, lat, lon)
        if res == "打卡成功!":
            person_msg = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n\n体温上报成功' + '\n\n'
            server_post(name + '\t' + '体温上报\t成功', person_msg, serverchan)
        else:
            person_msg = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n\n' + res + '\n\n'
            server_post(name + '\t' + '体温上报\t失败', person_msg, serverchan)
            sys.exit(1)
    except Exception as e:
        print(traceback.format_exc())
        server_post(name + '\t' + '体温上报\t失败', e, serverchan)
        sys.exit(1)
