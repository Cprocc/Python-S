# crate a new files
# get all files from old files
# copy all files from old files to new files
from multiprocessing import Pool,Manager
import os

def copyFileTask(name,oldFolderNmae,newFolderName,queue):
    'copy a file '
    fr = open(oldFolderNmae+'/'+name)
    fw = open(newFolderName +"/"+name,'w')

    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()

    queue.put(newFolderName)

def main():
    oldFolderName = input("Enter the old folder Name")
    newFolderName = oldFolderName + "-copyright"
    os.mkdir(newFolderName)
    fileNames = os.listdir(oldFolderName)

    pool = Pool(5)
    queue = Manager().Queue()
    for name in fileNames:
        pool.apply_async(copyFileTask,args=(name,oldFolderName,newFolderName,queue))

    num = 0
    allNum = len(fileNames)
    print(allNum)
    while num < allNum:
        queue.get()
        num += 1
        copyRate = num / allNum
        print("\r进度是：%.2f%% " %(copyRate*100),end = '')

if __name__ == "__main__":
    main()