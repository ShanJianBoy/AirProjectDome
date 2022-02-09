import requests
import json

from Comm.phone_data import random_phone, faker_maker


def add_lead(num):

    for i in range(num):
        phone = random_phone()
        faker = faker_maker()
        name = faker.name()

        url = "https://pre-release-scrm-server.m-insight.com.cn/crm/web/acq/lead/add"

        headers = {'Content-Typ': 'application/json',
                   'X-APP-ID': '7aac08b625424186', 'X-IDENTITY-ID': '503',
                   'X-PROJECT-ID': '84', 'X-ROLE-ID': '20',
                   'X-TOKEN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                              '.eyJtdWlkIjoxOTk4NTUsInVpZCI6MTk5ODU1LCJleHAiOjE2NDQ0NjUzNzR9'
                              '.khkI8juVJLseasbDTUnUT_4IRTJk20UJI9bljpcE6sc'}

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
        print(r.text)


# add_lead(1)
