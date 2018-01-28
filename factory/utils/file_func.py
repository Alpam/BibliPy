
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

def create(location, name):
    try :
        f=open(location+name+"/"+name+".conf",'w')
    except OSError:
        print("Impossible de créer le fichier de configuration de la db.")
    return f

