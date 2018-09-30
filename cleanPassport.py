import redis
import pymysql
r=redis.Redis(host='10.0.0.147',port=6379,db=1)

#def delRedis():
#     r.delete(r.delete('CELLPHONE:'+str))

def delcas():
     conn = pymysql.connect(host='10.0.0.147', port=3306, user='root', passwd='123456', db='passport')
     cur = conn.cursor()
     sql1="delete from passport.sys_user where cellphone= '%s'"%str
     cur.execute(sql1)
     conn.commit()
     conn.close()

def delDB():
     conn = pymysql.connect(host='10.0.0.95', port = 3308, user ='ichdev', passwd ='ichdev2018',db ='steamtest')
     cur = conn.cursor()
     sql2 = "delete from steamtest.sys_user where tel= '%s'"%str
     cur.execute(sql2)
     conn.commit()
     conn.close()

if __name__ == '__main__':
    str = input("请输入您要删除的手机号:");
    print("你输入的内容是: ", str)
    delRedis()
    delcas()
    delDB()
