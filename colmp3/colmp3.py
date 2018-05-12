#-*- coding: utf-8 -*-
import os
import codecs
import shutil


startDir = r"D:\shared\Music"
toDir = r"D:\shared\Music\Blues Collection Vol.03"

def search(dirname):
    flist = os.listdir(dirname)
    for f in flist:
        next = os.path.join(dirname, f)
        if os.path.isdir(next):
            search(next)
        else:
            doFileWork(next)

def renRev(filepath) :
    basename = os.path.basename(filepath)

    if basename == '13 I love you 1000 times.mp3' :
        return

    if basename.split('.')[-1] == 'mp3' :
        idx = len(basename) - 5
        while not basename[idx].isdigit() :
            idx -= 1
        while basename[idx].isdigit() :
            idx -= 1
        changingname = basename[idx:]

        if changingname != basename and len(changingname) > 4:
            print('%s => %s'%(basename, changingname))
            tobe = '%s\\%s'%(os.path.dirname(filepath), changingname.strip())
            os.rename(filepath, tobe)

def doFileWork(filename):

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

