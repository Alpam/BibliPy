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

from . import mkdir
from . import rmtree

def create(location, name):
    try :
        mkdir(location+name)
    except OSError:
        print("Chemin :"+location+" invalide.")

def delete_all(location):
    rmtree(location)
