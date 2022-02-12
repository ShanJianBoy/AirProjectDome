# -*- coding:utf-8 -*-
import random

from faker import Faker


def ran_num(num):
    """随机生成1~9位长度的数"""
    j = num
    # num_id = []
    num_id = ''.join(str(i) for i in random.sample(range(0, 10), j))  # sample(seq, n) 从序列seq中选择n个随机且独立的元素；
    return num_id


def random_phone():
    """随机生成手机号"""
    relist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
              "153", "155", "156", "157", "158", "159", "186", "187", "188"]
    randomize = random.choice(relist)
    number = "".join(random.choice("0123456789") for i in range(8))
    iphone = randomize + number
    return iphone


def ran_list(num):
    """循环生成序号与手机号插入列表"""
    f = faker_maker()
    faker_lists = []

    for j in range(num):
        for i in range(num):
            faker_list = []

            phone1 = random_phone()
            # name = f.name()
            # num_three = f.numerify()
            # word = f.word()

            faker_list.append(str(i + 1))
            faker_list.append(phone1)
            # faker_list.append(name)
            # faker_list.append(word)
            # faker_list.append(num_three)

            faker_lists.append(faker_list)

        # print(faker_list_1)
        return faker_lists

# def faker_maker_0(num, *tests):
#
#     faker_lists = []
#
#     for j in range(num):
#         for i in range(num):
#             faker_list = []
#             for test in tests:
#                 faker_list.append(test)
#
#             faker_lists.append(faker_list)
#
#             # print(faker_list_1)
#         return faker_lists


# import random
#
# phone = random_phone()
# num_0 = random.randint(0, 5)
# num_1 = random.randint(5, 10)
# # print(num_0)
# # print(num_1)
#
# l = faker_maker_0(5, random_phone(), random.randint(0, 5), random.randint(5, 10))
# print(num_0)
# print(num_1)
# print(l)

# print(ran_num(4))