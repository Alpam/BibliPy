
############################################################
#
#        Filename:
#
#     Description:
#
#         Version:  1.0
#  Python Version:  3.x
#
#          Author:  Paul Robin , paul.robin@etu.unistra.fr
#
############################################################

#!/usr/bin/python3

def create(path):
    try :
        f=open(path,'w')
        f.close
    except OSError:
        print("Impossible de créer le fichier "+path+".")

def writeAtEnd(doc, string):
    try :
        f=open(doc,'a')
        f.write(string)
        f.close
    except OSError:
        print("Impossible d'écrire dans : "+doc)

def addDb(path, name):
    create(path+"/"+name+".conf")
    writeAtEnd(path+"/"+name+".conf", name+"\n")

def addTbl(path, tbl_name, db_name):
    writeAtEnd(path+"/"+db_name+".conf", tbl_name+"::")
    writeAtEnd(path+"/"+tbl_name+"∕"+tbl_name+".conf", tbl_name+"\n")
    

