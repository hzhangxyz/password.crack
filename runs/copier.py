import os
def copy(filename,startid,beginner,ender,num):
    length = (ender - beginner)
    for i in range(num):
        n = "t:%d:%d:%d"%((i+startid),(beginner + length*i/num),(beginner + length*(i+1)/num))
        os.system("ln -s %s %s"%(filename,n))

