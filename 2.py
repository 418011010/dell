# -*- coding: utf-8 -*-
import json

#input_path real_filename rec_filename rec_row rec_count


def displayrec():
    if insertdic:
        print(insertdic)
    else:
        print("无记录")

def insertrec():
    # with open('rec.txt', 'rb') as f:
    #     info = json.load(f)
    #     print(info)

    input_path = input("请输入文件名或路径：")
    #input_path = "C:\\Users\\Administrator\\PycharmProjects\\dell\\12345678910111213141516.py"
    real_filename = input_path.split('\\')[-1]
    print(real_filename)
    rec_filename = real_filename[-16:]
    print(rec_filename)
    rec_row = input("请输入有错误的行号：")
    inserttuple = (real_filename, rec_row)
    rectuple = (rec_filename, rec_row)
    insertdic[inserttuple] = 1


    print(insertdic)


if __name__ == "__main__":
    insertdic = dict()
    while True:

        print("1.查看错误记录")
        print("2.新增错误记录(系统最多记录8条信息)")
        choice = input('请输入(1-2)：')
        if choice == '1':
            displayrec()
        elif choice == '2':
            insertrec()
        else:
            print('输入错误，请重试')

