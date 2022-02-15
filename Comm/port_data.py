import requests
import json

from faker import Faker
from airtest.core.api import *

from Comm.phone_data import random_phone


def add_lead(num):
    for i in range(num):
        fake = Faker('zh_CN')
        phone = random_phone()
        name = fake.name()

        url = "https://pre-release-scrm-server.m-insight.com.cn/crm/web/acq/lead/add"

        headers = {'Content-Typ': 'application/json',
                   'X-APP-ID': '7aac08b625424186', 'X-IDENTITY-ID': '503',
                   'X-PROJECT-ID': '84', 'X-ROLE-ID': '20',
                   'X-TOKEN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                              '.eyJtdWlkIjoxOTk4NTUsInVpZCI6MTk5ODU1LCJleHAiOjE2NDQ5Nzk4NTF9'
                              '.uAiegKMvjb4y3cdCn__EkTbr6VNEbUKGG434UDWoN2A'}

        payload = {
            "name": name,
            "maskedMobile": phone,
            "wechatNumber": phone,
            "channelTypeDicId": 1,
            "departmentSrcId": 1931,
            "itemSrcId": 611,
            "gradeTypeDicId": 16,
            "details": "当前用户是高意向用户，想买比亚迪宋plus dmi",
            "firstCall": 1,
            "dccAccountIdentityId": 503,
            "dccAccountRoleId": 20,
            "collectTimestamp": "2022-02-09 00:00:00",
            "duplicateType": 0
        }

        r = requests.post(url, json=payload, headers=headers)
        log(r.text)

# add_lead(1)
