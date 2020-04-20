import colorama
import time
import os
#
#             c
#            ooo
#           ccccc
#          ooooooo
#         ccccccccc
#        ooooooooooo
#       ccccccccccccc
#      ooooooooooooooo
#     ccccccccccccccccc
#    ooooooooooooooooooo
#   ccccccccccccccccccccc
#  ooooooooooooooooooooooo
#          cccccc
#          oooooo
#          cccccc

b = 1
os.system("clear")
print("""
             c
            ooo
           ccccc
          ooooooo
         ccccccccc
        ooooooooooo
       ccccccccccccc
      ooooooooooooooo
     ccccccccccccccccc
    ooooooooooooooooooo
   ccccccccccccccccccccc
  ooooooooooooooooooooooo
          cccccc
          oooooo
          cccccc""")

for a in range(101):
	time.sleep(0.5)
	os.system("clear")
	if b == 1:
		print(colorama.Cursor.UP(1)+"""
             o
            ccc
           ooooo
          ccccccc
         ooooooooo
        ccccccccccc
       ooooooooooooo
      ccccccccccccccc
     ooooooooooooooooo
    ccccccccccccccccccc
   ooooooooooooooooooooo
  ccccccccccccccccccccccc
          oooooo
          cccccc
          oooooo
		""")
		time.sleep(0.05)
		b = 2
		print("por desmon")
	elif b == 2:
		print(colorama.Cursor.UP(1)+"""
             c
            ooo
           ccccc
          ooooooo
         ccccccccc
        ooooooooooo
       ccccccccccccc
      ooooooooooooooo
     ccccccccccccccccc
    ooooooooooooooooooo
   ccccccccccccccccccccc
  ooooooooooooooooooooooo
          cccccc
          oooooo
          cccccc
		""")
		time.sleep(0.05)
		b =1
		print("por desmon")
