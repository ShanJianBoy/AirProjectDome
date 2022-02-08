# -*- coding:utf-8 -*-
import random

from faker import Faker


def random_phone():
    relist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
              "153", "155", "156", "157", "158", "159", "186", "187", "188"]
    randomize = random.choice(relist)
    number = "".join(random.choice("0123456789") for i in range(8))
    iphone = randomize + number
    return iphone


def faker_maker(num):
    f = Faker(locale='zh_CN')
    faker_lists = []

    for j in range(num):
        for i in range(num):
            faker_list = []

            phone1 = random_phone()
            name = f.name()
            num_three = f.numerify()
            word = f.word()

            faker_list.append(str(i + 1))
            faker_list.append(phone1)
            faker_list.append(name)
            faker_list.append(word)
            faker_list.append(num_three)

            faker_lists.append(faker_list)

        # print(faker_list_1)
        return faker_lists


def faker_maker_0(num, *tests):

    faker_lists = []

    for j in range(num):
        for i in range(num):
            faker_list = []
            for test in tests:
                faker_list.append(test)

            faker_lists.append(faker_list)

            # print(faker_list_1)
        return faker_lists


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
