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

from factory import dir_func, file_func

def create(location,name):
    dir_func.create(location, name)
    f = file_func.create(location, name)
    f.write(name)
    f.close
    return

def delete(location):
    dir_func.delete_all(location)
