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

def create(db_location, db_name, tbl_name):
    dir_func.create(db_location+"/"+tbl_name)
    file_func.addTbl(db_location, tbl_name, db_name)
    return

