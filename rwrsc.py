import xml.etree.ElementTree as ET
import os

def getXmls(path):
    fLine = os.listdir(path)
    oFileNameLine = []
    for i in fLine:
        if os.path.splitext(i)[1] == '.xml':
            oFileNameLine.append(os.path.splitext(i)[0])
    return oFileNameLine



print("code by square around 2021/9/1")
print("1:scale the skeleton 缩放骨架")
print("2:draw out skeleton to a .skl 提取骨架并生成skl文件")
com = input("输入你的操作：")
if(com == "1"):
    sN = (float)(input("输入缩放倍数："))
    fileLine = getXmls('./')
    for i in fileLine:
        print(i+".xml")
        infTree = ET.parse(i+'.xml')
        infRoot = infTree.getroot()
        for j in infRoot:
            if( j.tag == "skeleton"):
                for k in j:
                    if(k.tag == "particle"):
                        k.set("x",'{:.9f}'.format((float)(k.get("x"))*sN))
                        k.set("y",'{:.9f}'.format((float)(k.get("y"))*sN))
                        k.set("z",'{:.9f}'.format((float)(k.get("z"))*sN))
        infTree.write(i+'.xml')
if(com == "2"):
    fileLine = getXmls('./')
    for i in fileLine:
        print(i+".xml")
        infTree = ET.parse(i+'.xml')
        infRoot = infTree.getroot()
        for j in infRoot:
            if( j.tag == "skeleton"):
                j = ET.ElementTree(j)
                j.write(i+".skl")
                print (i+'.skl')
                break
os.system('pause')



