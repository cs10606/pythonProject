#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql


def searchCode():
     conn = pymysql.connect(host='10.0.0.95', port=3306, user='root', passwd='password', db='ads')
     cur = conn.cursor()
     sql1="select code  from captcha where account= '%s'"%str
     cur.execute(sql1)
     data = cur.fetchone()
     conn.commit()
     conn.close()
     return data



if __name__ == '__main__':
    str = input("请输入您要删除的手机号:")
    print("你手机号"+str+"的验证码是: ", searchCode())

