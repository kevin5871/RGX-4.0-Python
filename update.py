import zipfile
import os
from distutils.dir_util import copy_tree
from shutil import copyfile
try :
    with zipfile.ZipFile("update/updatefile.zip","r") as zip_ref:
        zip_ref.extractall("update/updatefile")
except :
    print("ERROR : Failed to extract zip.")
try :
    copy_tree("update/updatefile/RGX-4.0-Python-master/Songs", "Songs")
    print("SUCESS : Successfully updated Songs")
    copy_tree("update/updatefile/RGX-4.0-Python-master/img", "img")
    print("SUCESS : Successfully updated img")
    copy_tree("update/updatefile/RGX-4.0-Python-master/music", "music")
    print("SUCESS : Successfully updated music")
    copy_tree("update/updatefile/RGX-4.0-Python-master/ttf", "ttf")
    print("SUCESS : Successfully updated ttf")
    copy_tree("update/updatefile/RGX-4.0-Python-master/etc", "etc")
    print("SUCESS : Successfully updated etc")
    copyfile("update/updatefile/RGX-4.0-Python-master/main.py", "main.py")
    print("SUCESS : Successfully updated main.py")
    copyfile("update/updatefile/RGX-4.0-Python-master/version.txt", "version.txt")
    print("SUCESS : Successfully updated version.txt")
    copyfile("update/updatefile/RGX-4.0-Python-master/SongData.zip", "SongData.zip")
    print("SUCESS : Successfully updated SongData.zip")
except :
    print("ERROR : Failed to Copy Updated File")
print("FILE UPDATED SUCCESSFULLY!")
os.system('main.py')
