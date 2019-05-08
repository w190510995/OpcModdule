#coding=utf-8
#Version: V 1.0
#author:  'WangSheng'
#date:  '2019/3/31 14:01'
"""
将OPC数据 ，转存到redis
"""
import socket
from src.Config.AppConfig import Bind_ip,Bind_port
from src.Dao.OpcClientDao import OpcClient
from src.Dao.PointConfigDao import HandlePointExcel2Dic,GetOpcData
import json

groups_kks_desc = HandlePointExcel2Dic() #获取按组区分出的标签  组名： 【KKS编码ID,标签描述】

def HandleOpcData():
    """
    获取OPC数据 并根据要求，转存到redis
    """
    opcGroupsData = {}
    opcClient = OpcClient()

    for group in groups_kks_desc: #按照分组获取opc数据
        opcGroupsData[group] = GetOpcData(opcClient,groups_kks_desc[group])
    return opcGroupsData



def handle_request(client):
    """
    处理客户端请求
    :param client:
    """
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    opcData = json.dumps(HandleOpcData())
    client.send(opcData) #返回数据



def webserver_main():
    """
    webserver主程序
    """
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind((Bind_ip,Bind_port))
    sock.listen(1)
    while True:
         connection,address = sock.accept()
         handle_request(connection)
         connection.close()

# if __name__ == '__main__':
#     # opcData=   GetOpcData2Redis()
#     # print opcData
#     webserver_main()