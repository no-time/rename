def main():
    while True:
        question1=input('''
Do you want to rename:

1. A single file
2. Multiple files?

(1, or 2):''')
        if question1 == '1':
        
            single("1")

        if question1 == '2':

            multi()

        ex=input("Would you like to exit? (y, or n): ")
        if ex == "y":
            break
def single(multi):
    
    import os
    import subprocess
    from subprocess import call
    proc = subprocess.Popen(["ls", "-a"], \
    stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    ls=str(out)
    ls_split=ls.split("\\n")
    y=ls_split[0]
    y=str(y[2:]+"'")
    y=str(y[:-1])
    ls_split[0]=y
    ls_split.pop()
    print(ls_split)
    number=0
    for filenumber in ls_split:
        print(number, ls_split[number])
        number+=1
    if multi== "1":
        single2(ls_split)
def single2(ls_split):
    import os
    import subprocess
    from subprocess import call
    user_input=int(input\
    ("Which file number would you like to rename?: "))
    rename= input("What would you like to call the file?: ")
    
    call(["mv","-i",str(ls_split[user_input]),str(rename)])

def multi():
    import os
    import subprocess
    from subprocess import call
    import glob
    proc = subprocess.Popen(["pwd"], \
    stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    directory=str(out[1:-1])
    directory="/"+directory[2:-1]+"/"
    print(directory)
    integer=0
    extension=input("\nEnter the file extension: ")
    fileList=multi1(extension)
    print(fileList)
    user_inputM=input("\nEnter the beginning part of the filename\
. It will be numbered with this beginning \
(i.e. name0, name1, name2): ")
    for file in fileList:
        call(["mv","-i",str(fileList[(integer)]),str(user_inputM)+\
              str(integer)+str(extension)])
        integer+=1
    fList=(glob.glob('*'+extension))
    number=1
    print("Files changed:\n")
    for file in fList:
        print(str(number)+". "+file)
        number+=1
        
def multi1(extension):
    import glob
    lis=glob.glob("*"+extension)
    return (lis)

main()
