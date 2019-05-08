#coding=utf-8
#Version: V 1.0
#author:  'WangSheng'
#date:  '2019/3/30 22:03'

from src.Dao.OpcClientDao import OpcClient
import xlrd
from src.Config.AppConfig import Point_Config_File
import  numpy as np

def HandlePointExcel2Dic():
    """
    将Excel文件 转为字典数据
    :return:   kks编码：【区域，点描述】
    """
    wb = xlrd.open_workbook(filename=Point_Config_File,encoding_override='utf-8')
    ws = wb.sheet_by_name('Sheet1')
    dataset = []
    groups = []

    # groups_kks = {}
    groups_kks_desc = {}

    for r in range(ws.nrows): # 将excel数据转为二位数组
        col =[]
        for c in range(ws.ncols):
            col.append(ws.cell(r,c).value)
        dataset.append(col)
    dataset.pop(0)  # 将第一行数据删除

    for item in dataset:  # 将获分组标签
        # kksList.append(item[3]) #获取ID
        group = item[2]
        if group not in groups:
            groups.append(group)

    for item in  groups: #生成K-V数据类型
        groups_kks_desc[item] = []

    for item in dataset: #将kks与组对应
        group = item[2]
        kksId = item[3]
        idDesc = item[1]
        groups_kks_desc[group].append([kksId,idDesc])
    return  groups_kks_desc



def  GetOpcData(opcClient,tagList):
    """
    根据输入的标签名，获取对于的数据
    :param tagList: 标签列表
    :return: 对应的数据
    """

    tagList = np.array(tagList)
    tagDesc =tagList[:,1]
    tagList = tagList[:,0].tolist() #获取第一列标签KKS码

    opcDataList = opcClient.read(tagList)  # 根据KKS编码 获取opc 对应数据
    opcDataList = np.array(opcDataList)
    opcDataList = opcDataList[:,0:2] #取出钱两列数据
    concaList = np.c_[opcDataList,tagDesc] #将俩个列表合并
    return concaList.tolist()


