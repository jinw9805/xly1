"""
用户管理系统
=================V1===================
1、登录认证；
2、增删改查和搜索
    3.1 增 add      # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete   # delete mobkey
    3.3 改 update   # update monkey set age = 18
    3.4 查 list     # list
    3.5 搜 find     # find monkey
3、格式化输出
===================V2=================
1. 数据结构：列表 -> 字典；
2. 分页 display page 1 pagesize 5
3. 文件持久化
4. 异常处理
5. PrettyTable 优雅的格式化输出
6. 扩展：导出csv(可写可不写)
===================V3================
1. 函数
将用户管理系统v2面向过程 升级为 函数式
2. 导出csv
将用户列表导出csv文件
3. 日志审计
通过logging模块，记录用户登录和删除操作即可，其它操作不需要记录。
日志级别为debug
"""

# 标准模块
import sys
import json
import logging
import datetime
from prettytable import PrettyTable
import csv


# 定义变量
RESULT = {}
FIELDS = ('username', 'age', 'tel', 'email')
FILENAME = "51reboot.txt"
FILECSV = "users.csv"


USERINFO = ("51reboot", "123456")

helpinfo = '''{}
1.  增   add         : add monkey 12 132xxx monkey@51reboot.com
2.  删   delete      : delete monkey
3.  改   update      : update monkey set age = 20
4.  查   list        : list
5.  搜   find        : find monkey
6.  分页 display     : display page 2 pagesize 3 
7.  帮助 doc         : show help
8.  退出 exit        : exit
9.  保存 save        : save as 51reboot.txt
10. 加载 load        : load 51reboot.txt
11. 导出CSV saveCsv  : save as users.csv
12. 加载CSV loadVsv  : load from users.csv
{}
'''.format('=' * 70, '=' * 70)

def log(msg:str):
    logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                    filename='agent.log',  #日志存储文件名
                    filemode='a+'  #append 追加方式
                    )
    logging.info(msg)
    cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(cur_time + "  : " + msg)

def readFile():
    '''读取文件内容到内存'''
    try:
        with open(FILENAME, 'r') as fd:
            dateStr = fd.read()
            date = json.loads(dateStr)
            return date, True
    except Exception as e:
        return {}, False
    # try:
    #     # 1、打开文件
    #     fd = open(FILENAME, 'r')
    # except Exception as e:
    #     print("Read file fail, filename: {} not found.\n".format(FILENAME))
    # # 2. 操作文件 read
    # data = fd.read()
    # RESULT = json.loads(data)
    # # 3. 关闭文件
    # fd.close()
    # print("Load file:{} succ.".format(FILENAME))

def writeFile():
    with open(FILENAME, 'w') as fd:
        fd.write(json.dumps(RESULT))
    return "Save succ", True

def saveCsv():
    with open(FILECSV, 'w', newline='') as datacsv:
        csvwriter = csv.writer(datacsv, dialect="excel")
        csvwriter.writerow(['username', 'age', 'tel', 'email'])
        for x in RESULT.keys():
            csvwriter.writerow([x, RESULT[x]["age"], RESULT[x]["tel"], RESULT[x]["email"]])
    return "Save CSV succ", True

def loadCsv():
    try:
        csv_file = csv.reader(open(FILECSV,'r'))
        for x in csv_file:
            if x[0] == 'username':
                continue
            else:
                RESULT[x[0]] = {'username':x[0],'age':x[1],'tel':x[2],'email':x[3]}
        return "Load users.csv succ", True
    except Exception as e:
        return e, False

def login(username, password):
    '''
    验证账号和密码是否正确，如果正确返回True，否则返回False
    '''
    user_passwd_t = ("51reboot", "123456")
    if username == user_passwd_t[0] and password == user_passwd_t[1]:
        return "Login succ", True
    else:
        return "Login fail", False

def logout():
    sys.exit(0)

#添加用户
def addUser(input_user_manage_info:list):
    if len(input_user_manage_info) != 4:
        errMsg = print("Add info invalid, Please add again.")
        return errMsg, False

    #判断用户是否存在，如果用户存在，提示用户已经存在，不再添加
    username = input_user_manage_info[0]
    if username in RESULT:
        errMsg = "Username {} already exits.".format(username)
        return  errMsg, False
    else:
        RESULT[username] = dict(zip(FIELDS, input_user_manage_info))
        succMsg = "Add user {} succ.".format(username)
        return succMsg, True

def deleteUser(input_user_manage_info:list):
    # delete monkey
    username = input_user_manage_info[0]
    delete_flag = RESULT.pop(username, None)
    if delete_flag == None:
        errMsg = "User {} not found".format(username)
        return errMsg, False
    else:
        succMsg = "User {} Delete succ.".format(username)
        return succMsg, True

def updateUser(input_user_manage_info:list):
    ## update monkey set age = 20
    username = input_user_manage_info[0]
    where = input_user_manage_info[1]
    fuhao = input_user_manage_info[-2]
    if where != "set" or fuhao != "=":
        errMsg = "Update method error!"
        return  errMsg, False

    update_field = input_user_manage_info[-3]
    update_value = input_user_manage_info[-1]

    if username in RESULT:
        if update_field in RESULT[username]:
            RESULT[username][update_field] = update_value
            succMsg = "Username {} update succ.".format(username)
            return succMsg, True
        else:
            errMsg = "field: {} invalid.".format(update_field)
            return errMsg, False
    else:
        succMsg = "username: {} not found.".format(username)
        return succMsg, True

def listUser():
    # 如果没有一条记录， 那么提示为空
    if len(RESULT) == 0:
        errMsg = "not data."
        return errMsg, False
    xtb = PrettyTable()
    xtb.field_names = FIELDS
    for k, v in RESULT.items():
        xtb.add_row(v.values())
    return xtb, True

def displayUser(input_user_manage_info:list):
    # dispaly page 2 pagesize 5  #显示2页，每页显示5条
    # default = 5
    if len(input_user_manage_info) >= 2 and len(input_user_manage_info) <= 4:
        pagesize = 5
        if len(input_user_manage_info) == 2:
            if input_user_manage_info[0] == "page":
                pagesize = 5
            else:
                errMsg = "Display info invalid. Please input again."
                return errMsg, False

        else:
            if input_user_manage_info[0] == "page" and input_user_manage_info[2] == "pagesize":
                pagesize = int(input_user_manage_info[-1])
            else:
                errMsg = "Display info invalid. Please input again."
                return errMsg, False

        page = int(input_user_manage_info[1]) - 1
        data = []
        for k, v in RESULT.items():
            data.append(v.values())

        # start, end sep
        start = page * pagesize
        end = start + pagesize
        # print("Start: {}, End:{}".format(start, end))

        xtb = PrettyTable()
        xtb.field_names = FIELDS
        for userinfo in data[start:end]:
            xtb.add_row(userinfo)
        return xtb, True
    else:
        errMsg = "Input info invalid, Please input again."
        return errMsg, False

def findUser(input_user_manage_info):
    username = input_user_manage_info[0]
    userinfo = RESULT.get(username, None)
    if userinfo == None:
        errMsg = "User {} not found.".format(username)
        return errMsg, False
    else:
        xtb = PrettyTable()
        xtb.field_names = FIELDS
        xtb.add_row(userinfo.values())
        return xtb, True

def opLogic():
    #业务逻辑
    while True:
        # 业务逻辑
        info = input("Please input your operation:").strip()  # 去前后空格
        # string -> list
        info_list = info.split()
        if len(info) == 0:  # 如果为空， 则提示
            print("Input info invalid, Please input again.")
            continue
        action = info_list[0]
        input_user_manage_info = info_list[1:]
        if action == "add":
            # add monkey 12 132xxx monkey@51reboot.com
            addMsg, ok = addUser(input_user_manage_info)
            message = "{}, State: {}, Result: {}".format(action, ok, addMsg)
            log(message)
        elif action == "delete":
            delMsg, ok = deleteUser(input_user_manage_info)
            message = "{}, State: {}, Result: {}".format(action, ok, delMsg)
            log(message)
        elif action == "update":
            updateMsg, ok = updateUser(input_user_manage_info)
            message = "{}, State: {}, Result: {}".format(action, ok, updateMsg)
            log(message)
        elif action == "list":
            listMsg, ok = listUser()
            if not ok:
                message = "{}, State: {}, Result: {}".format(action, ok, listMsg)
                log(message)
            else:
                print(listMsg)
        elif action == "find":
            findMsg, ok = findUser(input_user_manage_info)
            if not ok:
                print("{}, State: {}, Result: {}".format(action, ok, findMsg))
            else:
                print(findMsg)
        elif action == "save":
            writeMsg, ok = writeFile()
            message = "{}, State: {}, Result: {}".format(action, ok, writeMsg)
            log(message)
        elif action == "load":
            readMsg, ok = readFile()
            if not ok:
                message = "{}, State: {}, Result: {}".format(action, ok, readMsg)
                log(message)
            else:
                global RESULT
                # 局部变量要修改全局变量的值，需要用global关键字声明。
                RESULT = readMsg
                message = "{}, State: {}".format(action, ok)
                log(message)
            print(RESULT)

        elif action == "saveCsv":
            csvMsg, ok = saveCsv()
            message = "{}, State: {}, Result: {}".format(action, ok, csvMsg)
            log(message)
        elif action == "loadCsv":
            loadcsvMsg, ok = loadCsv()
            print(RESULT)
            message = "{}, State: {}, Result: {}".format(action, ok, loadcsvMsg)
            log(message)

        elif action == "display":
            disMsg, ok = displayUser(input_user_manage_info)
            if not ok:
                print("{}, State: {}, Result: {}".format(action, ok, disMsg))
            else:
                print(disMsg)
        elif action == "doc":
            print(helpinfo)
        elif action == "exit":
            logout()
        else:
            print("\033[31m invalid action\033[0m")

def main():
    INIT_FAIL_CNT = 0
    MAX_FAIL_CNT = 6
    while INIT_FAIL_CNT < MAX_FAIL_CNT:
        username = input("Please input your username:")
        password = input("Please input your password:")
        loginMsg, ok = login(username,password)
        if not ok:
            log(loginMsg)
            INIT_FAIL_CNT += 1   #登录失败次数+1
            continue
        # print("Login succ\n\n")
        log(loginMsg)

        opLogic()
    print("\033[31m \nInput {} failed, Terminal will exit.\033[0m".format(MAX_FAIL_CNT))

if __name__ == '__main__':
    main()