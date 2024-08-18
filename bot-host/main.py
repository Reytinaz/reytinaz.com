import os
import shutil

print("hello world")
debug_File1 = open("debug_1", "w+")
debug_File1.write("hello world")
debug_File1.close()
shutil.move("debug_1", "_debug")