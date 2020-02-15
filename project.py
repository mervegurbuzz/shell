import os
def ls():
    for fn in os.listdir('.'):
        print (fn)



if __name__=='__main__':
    ls()
    