import os
import random

l_train=[]
l_val=[]
l_test=[]

# 读取文件中的内容，并将其打乱写入列表FileNameList
def ReadFileDatas(original_filename):
    file=open(original_filename,'r+',encoding='utf-8')
    FileNameList=file.readlines()
    random.shuffle(FileNameList)
    file.close()
    print("数据集总量：", len(FileNameList))
    return FileNameList
#将数据集随机划分
def TrainValTestFile(FileNameList):
    i=0
    j=len(FileNameList)
    for line in FileNameList:
        if i<(j*0.7):
            i+=1
            l_train.append(line)
        elif i<(j*0.9):
            i+=1
            l_val.append(line)
        else:
            i+=1
            l_test.append(line)
    print("总数量:%d,此时创建train,val,test数据集"%i)
    return l_train,l_test,l_val
#将获取到的各个数据集的包含的文件名写入txt中
def WriteDatasToFile(listInfo, new_filename):
    file_handle = open(new_filename,'w',encoding='utf-8')
    for str_Result in listInfo:
        file_handle.write(str_Result)
    file_handle.close()
    print('写入 %s 文件成功.' % new_filename)
if __name__ == "__main__":
      listFileInfo = ReadFileDatas('典义+典源/典义+典源.txt') # 读取文件
      l_train,l_val,l_test=TrainValTestFile(listFileInfo)
      WriteDatasToFile(l_train, '典义+典源/train.txt')
      WriteDatasToFile(l_test, '典义+典源/test.txt')
      WriteDatasToFile(l_val, '典义+典源/dev.txt')