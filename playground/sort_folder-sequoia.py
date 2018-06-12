# !/usr/bin/env python

import os
import shutil

path = "/Users/starsky/Desktop/DATA/GREEN-RED-RED_EDGE-IR"

savePath = "/SORT/"
fileExtensionTIFFolder = "TIF/"
fileExtensionJPGFolder = "JPG/"

directory = os.listdir(path)

pictures = []

for i in directory:

    i_path = path + "/" + i

    if os.path.isdir(i_path):

        i_dir = os.listdir(i_path)

        for j in i_dir:

            j_path = i_path + "/" + j

            if not os.path.isdir(j_path):

                fileName = j_path.split("_")

                for p in fileName:

                    if p == "GRE.TIF":
                        pictures.append(j_path)
                        folderName = i_path.split("/")[-1]

                        GRE_path = path + savePath + fileExtensionTIFFolder

                        GRE_path = GRE_path + j
                        print GRE_path

                        shutil.copy2(j_path, GRE_path)

                    elif p == "NIR.TIF":
                        pictures.append(j_path)
                        folderName = i_path.split("/")[-1]

                        NIR_path = path + savePath + fileExtensionTIFFolder
                        NIR_path = NIR_path + j
                        print NIR_path

                        shutil.copy2(j_path, NIR_path)

                    elif p == "RED.TIF":
                        pictures.append(j_path)
                        folderName = i_path.split("/")[-1]

                        RED_path = path + savePath + fileExtensionTIFFolder
                        RED_path = RED_path + j
                        print RED_path

                        shutil.copy2(j_path, RED_path)

                    elif p == "RGB.JPG":
                        pictures.append(j_path)
                        folderName = i_path.split("/")[-1]

                        RGB_path = path + savePath + fileExtensionJPGFolder
                        RGB_path = RGB_path + j
                        print RGB_path

                        shutil.copy2(j_path, RGB_path)
