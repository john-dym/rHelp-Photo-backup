import datetime
import os

now = datetime.datetime.now()
date = now.strftime('%d.%m.%Y')

  #Test destination directory
main = 'C:\Python\Auto.python'
  #Test source directory
dirs = 'C:\Python\DCIM'

os.chdir (main)
os.makedirs(date,exist_ok=True)
  #I used the os.path.join() because of an issue with concatenation of the directory path strings causing multiple // to appear
newMain = os.path.join(main,date)
  #Directory change was used for the for loop below
os.chdir (dirs)

for file in os.listdir('.'):
    oldFile = os.path.join(dirs,file)
    fileName, ext = os.path.splitext(file)
    newFile = os.path.join(newMain,fileName) + ' ' + date + ext
    if os.path.isfile(oldFile):
        os.replace(oldFile,newFile)
