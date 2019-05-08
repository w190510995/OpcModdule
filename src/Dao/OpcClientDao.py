#coding=utf-8
#Version: V 1.0
#author:  'WangSheng'
#date:  '2019/3/31 13:54'
from src.Config.AppConfig import Opc_Server_Name,Opc_Server_Ip
import  OpenOPC

def OpcClient():
    opc = OpenOPC.client()
    opc.connect(Opc_Server_Name, Opc_Server_Ip)
    return  opc
