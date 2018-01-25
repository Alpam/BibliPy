#
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

from dbfactory import mkdir

def create_db(location,name):
    try :
        mkdir(location+name)
    except OSError:
        print("Chemin invalide.")
