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

from factory import db_factory

print("creation")
db_factory.create("./","t1")
print("suppression")
db_factory.delete("./t1")
