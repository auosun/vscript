from client import Client, VMessInbound
import mysql

# from errors import *


class userController():
    """
    #1 用户控制类
        1. 根据邮箱创建用户
        2. 根据邮箱删除用户
        3. 创建所有用户
        4. 删除所有用户
    """
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 10085
        self.client = Client(self.ip, self.port)

    def create_one_user(self,email):
        """
        1. 根据邮箱创建
        :param email: 用户邮箱
        :return:
            111:创建成功
            112:数据库错误
            # 113:若email已存在，抛出EmailExistsError异常
            # 114:若inbound_tag不存在，抛出InboundNotFoundError异常
            115:根据邮箱创建一个用户未知原因异常
        """
        sql = "SELECT * FROM `user` WHERE `email` = '%s'" % (email)
        result = mysql.mysql(sql)
        if (result == 33063 or result==33061 or result==33062):
            return 112
        try:
            self.client.add_user('vmess-in', result[0][4], email, 0, 2)
        # except EmailExistsError:
        #     return 13
        # except InboundNotFoundError:
        #     return 14
        except Exception:
            # print("15 ".result[0])
            return 115
        else:
            return 111

    def remove_one_user(self,email):
        """
        2. 根据邮箱删除
        :param email: 用户邮箱
        :return:
            121:删除成功
            122:未知原因删除失败
        """
        try:
            self.client.remove_user('vmess-in', email)
        except Exception:
            return 122
        else:
            return 121

    def create_all_user(self):
        """
        3. 创建所有用户
        :return:
            131:创建所有的用户成功
            132:出现错误
        """
        right = 0
        sql = "SELECT * FROM `user` LIMIT 50"
        result = mysql.mysql(sql)
        for res in result:
            re = self.create_one_user(res[1])
            if not re==111:
                right = 1
        if(right==1):
            return 132
        else:return 131

    def remove_all_user(self):
        """
        4. 删除所有用户
        :return:
            141:删除所有的用户成功
            142:出现错误
        """
        right = 0
        sql = "SELECT * FROM `user` LIMIT 50"
        result = mysql.mysql(sql)
        for res in result:
            re = self.remove_one_user(res[1])
            if not re == 121:
                right = 1
        if (right == 1):
            return 142
        else:
            return 141

    def test1(self):
        """
        test1 测试数据库运行
        :return:
        """
        sql = "SELECT * FROM `user` LIMIT 50"
        result = mysql.mysql(sql)
        for res in result:
            print(res)


if __name__ == '__main__':
    c= userController()
    print(mysql.readconfig().get('error', str(c.remove_all_user())))




