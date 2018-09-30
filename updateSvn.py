# -*- coding：utf-8 -*-
import os
import time

def svnUpdate():
    os.chdir('F:/03 卡门网SVN/Fulu.Document/2.TestCase/05 测试资料')
    cmd='svn update . '
    os.system(cmd)

def timer(n):
  ''''' 
  每n秒执行一次 
  '''
  while True:
    print(time.strftime('%Y-%m-%d %X',time.localtime()))
    svnUpdate() # 此处为要执行的任务
    time.sleep(n)
    print('第'+str(n)+'次更新完成')

if __name__ == '__main__':
    timer(10)