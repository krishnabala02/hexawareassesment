'''Program to count number of files inside zip file,size of each file inside and count of records in each file'''
from zipfile import ZipFile
import pandas as pd
import os
import datetime

file_names = []
file_sizes = []
file_record_count = []
Nested_zipfiles = []


# extracting file metadata
def process_file(file_info, z_files):
    file_names.append(file_info.filename.split("/")[1])
    file_sizes.append(file_info.file_size)
    # print(type(z_files.read(file_info.filename)))
    # read with split \n will give no. of rows. length will  give count of total rows in a file
    file_record_count.append(len(z_files.read(file_info.filename).split(b'\n')))


# iterating through zip files without extracting
def process_zip(zipFilename):
    try:
        # with statement ensure proper aquisition and release of resources
        with ZipFile(zipFilename, allowZip64=True) as z_files:

            for file_info in z_files.infolist():
                print(file_info)
                # ignoring OS related files in below condition
                if file_info.filename[len(file_info.filename) - 1] == "/" \
                        or file_info.filename.startswith("__MACOSX") \
                        or file_info.filename.__contains__(".DS_Store"):
                    continue
                if file_info.filename.split(".")[1] == "zip":
                    Nested_zipfiles.append(file_info.filename)
                    file_names.append(file_info.filename.split("/")[1])
                    file_sizes.append(" ")
                    file_record_count.append(" ")
                    # print(z_files.extract(file_info.filename))
                    process_zip(z_files.extract(file_info.filename))
                else:
                    process_file(file_info, z_files)

    except zipfile.BadZipFile as error:
        print(error)


# writing zip file info to csv file
def write_to_file():
    output_df = pd.DataFrame(
        {
            "FileName": file_names,
            "Size(bytes)": file_sizes,
            "RecordCount": file_record_count
        }
    )
    print(output_df.to_string(index=False))
    # output_df.to_csv("output_" + str(datetime.datetime.now()) + ".csv", index=False)
    with open('output_' + str(datetime.datetime.now()) + '.txt', mode='w') as file_object:
        print(output_df.to_string(index=False), file=file_object)


# Path should be path where zip file is located
Path = "/Users/purnaraghavaraokalva/Desktop/sampledata.zip"
process_zip(Path)
write_to_file()

# removing extracted nested zips
for zipfile in Nested_zipfiles:
    # print(zipfile)
    os.remove(zipfile)
