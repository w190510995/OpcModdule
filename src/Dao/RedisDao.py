#coding=utf-8
#Version: V 1.0
#author:  'WangSheng'
#date:  '2019/3/30 21:39'

from src.Config.AppConfig import Redis_db,Redis_ip,Redis_password,Redis_port
import  redis




def RedisClient():
    """
    连接redis
    :return:
    """
    pool = redis.ConnectionPool(host=Redis_ip, port=Redis_port, db=Redis_db,password=Redis_password)
    client = redis.StrictRedis(connection_pool=pool)
    return client

def SaveUpdateData2Redis(tempData):
    """
    将传入的数据存入redis
    :param tempData:
    """




if __name__ == '__main__':
    redis = RedisClient()
    print(redis.keys())
    print type(redis.keys())
