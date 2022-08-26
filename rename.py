import os
opath = "F:\\shixi\\CS\\vits3\\wav"
for root, dirs, files in os.walk(opath):
    # print('root:',root)
    # print('dirs:',dirs)
    # print('files:',files)
    for file in files:
        if(file[-4:] == ".wav"):
            #print(file)
            fp = os.path.join(root, file)
            fp_rename = os.path.join(root, "shioriko_" + file)
            os.rename(fp, fp_rename)