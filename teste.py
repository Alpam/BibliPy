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

from factory import db_factory, tbl_factory

db_factory.create("./test","t1")
tbl_factory.create("./test/t1","t1","tbl1")
tbl_factory.create("./test/t1","t1","tbl2")

