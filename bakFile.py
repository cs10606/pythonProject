import os

Root = 'a'
Dest = 'b'

def DtestF():
    for (root, dirs, files) in os.walk(Root):
        print(dirs)
        #print(dirs)
        #print(files)
        new_root = root.replace(Root, Dest, 1)
        #print('new_root:'+new_root)


if __name__ == '__main__':
    DtestF()