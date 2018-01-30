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
    db_location = location+"/"+name
    dir_func.create(db_location)
    file_func.addDb(db_location, name)
    return

def delete(location):
    dir_func.deleteAll(location)
