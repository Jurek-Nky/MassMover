#!/usr/bin/python3.8
import argparse
import os
import shutil

parser = argparse.ArgumentParser(description="Copies all Files from all subdirectories into the destination directory.")
parser.add_argument("-s", "--start_dir", type=str, metavar="", help="directory from where to start")
parser.add_argument("-d","--destination", type=str,metavar="",required=True, help="destination dircetory")
parser.add_argument("-p", "--pictures", action="store_true", help="will copy pictures")
parser.add_argument("-v", "--videos", action="store_true", help="will copy videos")
parser.add_argument("-a","--all",action="store_true",help="copies every file")
parser.add_argument("-l","--list",action="store_true",help="list files to copie")
args = parser.parse_args()




def copy_All_from_dir_to_dir(start_dir,destination,pictures,videos,all,list):
    working_dir = os.getcwd()
    all_bool = False
    pictures_bool = False
    audio_bool = False
    vid_bool = False
    list_bool = False
    if start_dir:
        working_dir = start_dir
    if pictures:
        pictures_bool = True
    if videos:
        vid_bool = True
    if all:
        all_bool = True
    if list:
        list_bool =True
    if os.path.isdir(working_dir)== False:
        os.mkdir(working_dir)
    for roots , dirs , files in os.walk(working_dir):
        for file in files:
            if list_bool == False:
                if all_bool:
                    shutil.copy2(roots + "/" + file, destination)
                    print(file + " copied")
                elif pictures_bool and file.endswith(".png") or file.endswith(".jpg") or file.endswith(".gif"):
                    shutil.copy2(roots+"/"+file, destination)
                    print(file + " copied")
                elif audio_bool and file.endswith(".mp3") or file.endswith(".wav"):
                    shutil.copy2(roots + "/" + file, destination)
                    print(file + " copied")
                elif vid_bool and file.endswith(".mp4") or file.endswith(".avi"):
                    shutil.copy2(roots + "/" + file, destination)
                    print(file + " copied")
                else:
                    print(roots + file)
                    print("wrong format")
            else:
                if all_bool:
                    print(roots + "/" + file)
                elif pictures_bool and file.endswith(".png") or file.endswith(".jpg") or file.endswith(".gif"):
                    print(roots + "/" + file)
                elif audio_bool and file.endswith(".mp3") or file.endswith(".wav"):
                    print(roots + "/" + file)
                elif vid_bool and file.endswith(".mp4") or file.endswith(".avi"):
                    print(roots + "/" + file)
                else:
                    print(roots + "/" + file)
                    print("wrong format")




if __name__ == '__main__':
    copy_All_from_dir_to_dir(args.start_dir,args.destination,args.pictures,args.videos,args.all,args.list)
