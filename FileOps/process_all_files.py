import insert_feature
import sys
import os

directory = sys.argv[1]
extension = sys.argv[2]

#inputfile = sys.argv[1]

#return the list of files with certain extension in certain directory
def get_fileList(dirpath,extension):
    fileList = []
    for file in os.listdir(dirpath) :
        if file.endswith(extension):
            fileList +=[file]
    return fileList

            
files_to_process = get_fileList(directory,extension)
for inputfile in files_to_process:
    print inputfile
    insert_feature.insert_ethlnk_param(inputfile,inputfile+'_1','317','319','sample_files/ethlnk_Param_319.txt')
    insert_feature.insert_ethlnk_param(inputfile+'_1',inputfile+'_2','319','320','sample_files/ethlnk_Param_320.txt')
    insert_feature.insert_global_feature(inputfile+'_2',inputfile+'_3','31205','sample_files/param_31206_31213.txt',True)
    insert_feature.insert_global_feature(inputfile+'_3',inputfile+'_4','31012','sample_files/assem_31013_31014.txt',False)

#insert_feature.insert_ethlnk_assem(inputfile,'006','007','ethlnk_Assem_007.txt')
