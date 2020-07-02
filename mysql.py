import pymysql
import configparser




def readconfig():
    """
    1. 配置文件读取
    :return: cf:config文件读取结果
    """
    cf = configparser.ConfigParser()
    cf.read('config.ini')
    return cf

def mysql(sql):
    """
    2. 使用数据库
    :param sql:sql语句
    :return:
        33061:数据库连接失败
        33062:数据库连接成功，语句执行失败
        33063:查询结果为空，或者无查询结果
        results:正常返回结果
    """
    try:
        db = pymysql.connect(host=readconfig().get('mysql', 'host'), port=3306, user=readconfig().get('mysql', 'user'),
                             password=readconfig().get('mysql', 'password'), db=readconfig().get('mysql', 'db'),
                             charset='utf8')
        db.connect()
    except:
        return 33061
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        results = cursor.fetchall()
    except:
        db.rollback()
        db.close()
        return 33062
    if not results:
        return 33063
    db.close()

    return results

