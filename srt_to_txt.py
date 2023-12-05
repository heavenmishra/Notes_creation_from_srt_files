'''
***Some points to remember before using the code.***
1.All srt file of a prticular course must present in a single folder.
2.Nameing of those srt files should start with number,followed by the seperator.
3.If both the condations are already done then you can just clone the code and edit the constants section like give the proper srt folder path,seperator and notes name.

Enjoy the note

**Further improvement will be done soon
'''

'''
Importing os,tkinterand shutil module for verious purposes.
    os module - is used for readinf files from a particular path.
    tkinter module - is used to sort the files in numerical order.
    shhutil module - is used to get the size of a terminal.

'''
import os
from tkinter import Tcl
import shutil

# Below parameters are constant parameters you can modifie the srt file path , seperator and notes name only and you will get the same result.
srt_path=r'D:\[TutsNode.net] - AWS Certified Developer Associate Exam Training DVA-C02\srt'
seperator=r'.'
notes_name=r'AWS developer certification'
#------------------------constants section ends here--------------------

final_content=""
files = os.listdir(srt_path)
sorted_files=Tcl().call('lsort', '-dict', files)
# print(sorted_files)

def filecontent(file,filename):
    '''
    filecontent function takes two arggumets that is file and filename. and used those two parameter to retirve actual content from srt files and return the actual content.
    ----------------------------------------
    file: string
        File will contein the all content including time-stamps.
    
    filename: string
        As name suggest it contains the name of the file.
    
    return
    -----------------------------------------
    actual_content: string
        As name suggest it contains the actuall content from the srt files.
    '''
    contentaslist = file.split("\n\n")
    actual_content= filename[:-7]+"\n\n"
    for i in contentaslist:
        lst = i.split("\n")
        actual_content = actual_content+lst[-1]+"\n"
    return actual_content

for filename in sorted_files:
    with open(srt_path+r"/"+filename,"r") as content:
        content = filecontent(content.read(),filename)
    
    final_content = final_content+content

try:
  with open(notes_name+".txt","w") as finaltext:
    finaltext.write(final_content)
    # This will print the statemt/string in the middle of the terminal with a emoji.
    print("Cake status: Baked, aromatic, and ready for enjoyment! \N{smiling face with sunglasses}".center(shutil.get_terminal_size().columns))
except Exception as e:
  print(e)