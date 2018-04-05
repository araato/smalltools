#-*- coding: utf-8 -*-
import os
import codecs
import shutil


startDir = r"D:\torrent\complete\Joan Jett Full Discography with Lives"
toDir = r"D:\Share\모바일용Music\car16G\Joan Jett"

def search(dirname):
    flist = os.listdir(dirname)
    for f in flist:
        next = os.path.join(dirname, f)
        if os.path.isdir(next):
            search(next)
        else:
            doFileWork(next)



def doFileWork(filename):

    global startDir
    global toDir
    ext = os.path.splitext(filename)[-1]

    if ext == '.mp3': 

        toFile = filename.replace(startDir, "")[1:]
        
        dstFile = toDir + "\\" + toFile.replace("\\", "_")
    
        try :
            shutil.copy(filename, dstFile)
        except shutil.SameFileError:
            pass
        

        try :
            print(toFile)
        except UnicodeEncodeError :
            bfilename = codecs.encode(toFile, 'utf-8')
            ufilename = codecs.encode(bfilename, 'cp949', 'replace')
            print(ufilename)


search(startDir)

