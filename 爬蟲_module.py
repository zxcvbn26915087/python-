# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 12:41:15 2021

@author: admin
"""
import os
import csv
import requests
file_name1=["資料夾名稱","資料夾名稱"]

file_name2=["資料夾名稱","資料夾名稱","資料夾名稱"]

file_name3=["資料夾名稱","資料夾名稱"]

file_name4=["資料夾名稱","資料夾名稱","資料夾名稱","資料夾名稱","資料夾名稱","資料夾名稱","資料夾名稱","資料夾名稱"] 

file_name5=["資料夾名稱","資料夾名稱","資料夾名稱","資料夾名稱","資料夾名稱","資料夾名稱","資料夾名稱","資料夾名稱","資料夾名稱","資料夾名稱","資料夾名稱","資料夾名稱"] 

base_path=os.getcwd()
print(base_path)

path_list1=[None]*200   #295
path_list2=[None]*200

range_start = 80 
range_end = 110

def create_csv(list1):
    csvfile = "log.csv"
    with open(csvfile, 'w+',newline='',errors='ignore') as fp:
        writer = csv.writer(fp)
        writer.writerow(["檔案名稱", "檔案內容", "檔案類型"])
        for row in list1:
            writer.writerow(row)
        fp.close()

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print("資料夾不存在, 建立資料夾: "+folder_name)
    else:
        print("找到資料夾: "+folder_name)
        
def folder_path(file_name,path):
    new_path=path + "\\" +file_name
    new_path=new_path.replace("\\","/")
    return new_path
    
def create_KM_file():   
    for i in range(len(file_name1)):
        create_folder(file_name1[i])  #第一層建好資料夾
    count=0
    
    #KM專區的資料夾建立
    path=base_path #路徑切到最外層
    path=folder_path(file_name1[0],path)  #紀錄"KM專區"的資料夾建立資料夾路徑
    print(path+"\n")
    
    for j in range(len(file_name2)):
        #print(file_name2[i])
        os.chdir(path)#已切換執行位置到"KM專區"資料夾路徑
        if not os.path.exists(file_name2[j]):
            os.mkdir(file_name2[j])
            print("資料夾不存在, 建立資料夾: "+file_name2[j])
        else:
            print("找到資料夾: "+file_name2[j])
        os.chdir(path+"/"+file_name2[j])#已切換到第二層資料夾路徑
        
        for k in range(range_start,range_end):
            if not os.path.exists("%d"%k):
                os.mkdir("%d"%k)
                print("資料夾不存在, 建立資料夾: "+"%d"%k)
               # a=path+"/"+file_name2[j]+"/"+"%d"%k
                path_list1[count]=path+"/"+file_name2[j]+"/"+"%d"%k  #"%s"%a
                count=count+1
            else:
                print("找到資料夾: "+"%d"%k)
                path_list1[count]=path+"/"+file_name2[j]+"/"+"%d"%k  #"%s"%a
                count=count+1
    os.chdir(base_path)
    
    #知識文件專區
    path=base_path #路徑切到最外層
    path=folder_path(file_name1[1],path)  #紀錄"知識文件專區"資料夾路徑
    print(path+"\n")
    
    
    #創建報告類與教材類
    for j in range(len(file_name3)):
        os.chdir(path)#已切換執行位置至"知識文件專區"資料夾路徑
        if not os.path.exists(file_name3[j]):
            os.mkdir(file_name3[j])
            print("資料夾不存在, 建立資料夾: "+file_name3[j])
        else:
            print("找到資料夾: "+file_name3[j])
        os.chdir(path+"/"+file_name3[j])#已切換到第二層資料夾路徑
        
        #創建報告類裡的資料夾
        if j==0:
            for k in range(len(file_name4)): 
                if not os.path.exists(file_name4[k]):
                    os.mkdir(file_name4[k])
                    print("資料夾不存在, 建立資料夾: "+file_name4[k])
                    path_list2[count]=path+"/"+file_name3[0]+"/"+file_name4[k]
                    count=count+1
                else:
                    print("找到資料夾: "+file_name4[k])
                    path_list2[count]=path+"/"+file_name3[0]+"/"+file_name4[k]
                    count=count+1
            
        #創建教材類裡的資料夾
        if j==1:
            for k in range(len(file_name5)): 
                if not os.path.exists(file_name5[k]):
                    os.mkdir(file_name5[k])
                    print("資料夾不存在, 建立資料夾: "+file_name5[k])
                    path_list2[count]=path+"/"+file_name3[1]+"/"+file_name5[k]
                    count=count+1
                else:
                    print("找到資料夾: "+file_name5[k])
                    path_list2[count]=path+"/"+file_name3[1]+"/"+file_name5[k]
                    count=count+1
                
        """
        if not os.path.exists("%d"%k):
            os.mkdir("%d"%k)
            print("資料夾不存在, 建立資料夾: "+"%d"%k)
           # a=path+"/"+file_name2[j]+"/"+"%d"%k
            path_list[count]=path+"/"+file_name2[j]+"/"+"%d"%k  #"%s"%a
            count=count+1
        else:
            print("找到資料夾: "+"%d"%k)
            path_list[count]=path+"/"+file_name2[j]+"/"+"%d"%k  #"%s"%a
            count=count+1
            """
        os.chdir(path)#已切換到第一層資料夾路徑
    os.chdir(base_path)



def get_url(path):
    with open(path ,'r', newline='') as f:
        lines = f.readlines()
        url_text = []
        for line in lines:
            line = line.replace("\r\n","")
            url_text.append(line)
        f.close()
    return url_text
    
def save_to_folder(file, path):
    page = requests.get(file)
    list3 = file.split('/')
    if page.status_code == requests.codes.ok:
        os.chdir(path)  #切換至儲存檔案位置
        folder_file_name =  list3[len(list3)-1]
        with open(folder_file_name, 'wb+') as fp:
            fp.write(page.content)
            fp.close()
        os.chdir(base_path)#路徑切到最外層
        return None
    else:
        log_file_name = list3[len(list3)-1].replace(file[file.rfind('.'):],"")
        file_type = file[file.rfind('.'):].replace(".","")
        if file_type.startswith('59'):
            return [log_file_name,page.status_code,'None']
        else:
            return [log_file_name,page.status_code,file[file.rfind('.'):].replace(".","")]
        
def get_pathlist():
        return path_list1,path_list2


def del_KM_emp_dir():
    
    
    path=base_path #路徑切到最外層
    path=folder_path(file_name1[0],path)  #紀錄"KM專區"的資料夾建立資料夾路徑
    print(path+"\n")
    
    
    #刪除KM專區裡空的資料夾
    for j in range(len(file_name2)):
        #print(file_name2[i])
        os.chdir(path)#已切換執行位置到"KM專區"資料夾路徑
        os.chdir(path+"/"+file_name2[j])#已切換到第二層資料夾路徑
        
        for k in range(range_start,range_end):
            try:
                os.rmdir(path+"/"+file_name2[j]+"/"+"%d"%k) #os.rmdir() 方法用於刪除指定路徑的目錄。僅當這資料夾是空的才可以,否則,丟擲OSError。
                print(path)
            except Exception as e:
                print('Exception',e)
    os.chdir(base_path)
    
    #知識文件專區
    path=base_path #路徑切到最外層
    path=folder_path(file_name1[1],path)  #紀錄"知識文件專區"資料夾路徑
    print(path+"\n")
    
    
    #創建報告類與教材類
    for j in range(len(file_name3)):
        os.chdir(path)#已切換執行位置至"知識文件專區"資料夾路徑
        
        #刪除報告類裡空的資料夾
        if j==0:
            for k in range(len(file_name4)): 
                try:
                    os.rmdir(path+"/"+file_name3[0]+"/"+file_name4[k]) #os.rmdir() 方法用於刪除指定路徑的目錄。僅當這資料夾是空的才可以,否則,丟擲OSError。
                    print(path)
                except Exception as e:
                    print('Exception',e)
                    
                    
        #刪除教材類裡空的資料夾
        if j==1:
            for k in range(len(file_name5)): 
                try:
                    os.rmdir(path+"/"+file_name3[1]+"/"+file_name5[k]) #os.rmdir() 方法用於刪除指定路徑的目錄。僅當這資料夾是空的才可以,否則,丟擲OSError。
                    print(path)
                except Exception as e:
                    print('Exception',e)
                    
    os.chdir(base_path)
    