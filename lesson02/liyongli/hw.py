# -*- coding:utf-8 -*-
# author: lyl

"""
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
3. 格式化输出
"""

# 标准模块
import sys

# 定义变量
RESULT = []
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("51reboot", "123456")
FIELDS = ['username', 'age', 'tel', 'email']
RESULT.append(FIELDS)


# 定义功能函数

# 检测用户是否存在
def check_user(name):
    for i in RESULT:
        if name == i[0]:
            return True
    return False


# 判断用户更新字段
def foo(tag):
    # add monkey 12 132xxx monkey@51reboot.com
    # update monkey set age = 18
    return {

        'username': lambda: 0,
        'age': lambda: 1,
        'tel': lambda: 2,
        'email': lambda: 3,
    }[tag]()


# 增加用户
def add(infolist):  # 之所以写infolist是因为如果定义成info_list 不符合PEP8规范
    # add monkey 12 132xxx monkey@51reboot.com
    name = infolist[1]
    if check_user(name):
        return "添加失败{}已存在".format(name)

    RESULT.append(infolist[1:])
    return "用户{}添加成功".format(name)


# 删除用户
def delete(infolist):
    # delete monkey
    name = infolist[1]
    if check_user(name):
        for i in range(len(RESULT)):
            if name == RESULT[i][0]:
                RESULT.remove(RESULT[i])
                return "用户{}删除成功".format(name)
    return "用户{}删除失败，无此用户".format(name)


# 更新用户
def update(infolist):
    # ['username', 'age', 'tel', 'email']
    # update monkey set age = 18
    name = infolist[1]
    if check_user(name):
        for i in range(len(RESULT)):
            if name == RESULT[i][0]:
                result_tag = foo(info_list[3])
                RESULT[i][result_tag] = infolist[5]
        return "用户{}更新成功".format(name)
    return "用户{}更新失败，无此用户".format(name)


while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username: ")
    password = input("Please input your password: ")
    if username == USERINFO[0] and password == USERINFO[1]:
        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        while True:
            # 业务逻辑
            info = input("Please input your operation: ")
            # string -> list
            info_list = info.split()
            action = info_list[0]
            if action == "add":
                # 判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
                result = add(info_list)
                print(result)
            elif action == "delete":
                # .remove
                result = delete(info_list)
                print(result)
            elif action == "update":
                result = update(info_list)
                print(result)
            elif action == "list":
                # 如果没有一条记录， 那么提示为空

                # print(RESULT)
                for x in RESULT:
                    print("{} {} {} {}".format(x[0], x[1], x[2], x[3]), end="\t")
                    print()
                    print("-" * 50)
            elif action == "find":
                pass
            elif action == "exit":
                sys.exit(0)
            else:
                print("invalid action.")
    else:
        # 带颜色
        print("username or password error.")
        INIT_FAIL_CNT += 1

print("\nInput {} failed, Terminal will exit.".format(MAX_FAIL_CNT))
