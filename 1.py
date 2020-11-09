# -*- coding: utf-8 -*-
import sys
import random

stu_score = dict()
stu = ['jay', 'tom', 'lucy', 'jimmy']

for i in stu:
    stu_score[i] = random.choice(range(100))


def displayscore():
    print(stu_score)
    print("最高分为:{}".format(max(list(stu_score.values()))))


def modifyscore():
    name_tomodify = input("请输入需要修改成绩的名字('jay', 'tom', 'lucy', 'jimmy')：")
    score_tomodify = input("请输入需要修改{}的分数为(1-100)：".format(name_tomodify))
    stu_score[name_tomodify] = int(score_tomodify)
    print(stu_score)


while True:
    print("1.查看学生成绩")
    print("2.修改学生成绩")
    choice = input('请输入(1-2)：')
    if choice == '1':
        displayscore()
    elif choice == '2':
        modifyscore()
    else:
        print('输入错误，请重试')