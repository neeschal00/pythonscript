# import pandas as pd
import os
import csv
import time

dir_file = os.getcwd()
'''

for files in os.listdir(dir_file):
    # print(files)
    if(files.endswith(".csv")):
        df = pd.read_csv(files)
        output_file = files.split(".csv")
        output_file = output_file[0]+"1"+".csv"
        df.to_csv(output_file,index=False)
        os.remove(files)
        os.rename(output_file,files)

'''

for files in os.listdir(dir_file):
    # print(files)
    if(files.endswith(".csv")):
        with open(files, newline='') as in_file:
            out_fileN = files.split(".csv")
            out_fileN = out_fileN[0]+"1"+".csv"
            with open(out_fileN, 'w', newline='') as out_file:
                writer = csv.writer(out_file)
                for row in csv.reader(in_file):
                    if row:
                        writer.writerow(row)
        time.sleep(3)
        os.remove(files)
        os.rename(out_fileN,files)
        files = ''
        out_fileN = ''