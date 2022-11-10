from zipfile import ZipFile
from pathlib import Path


def process_zip(zipFilename):
    # with statement ensure proper aquisition and release of resources
    with ZipFile(zipFilename, allowZip64=True) as z_files:
        for file_info in z_files.infolist():
            print(file_info)
            '''if file_info.filename.split(".")[1] == "zip":
                print(file_info.filename.split(".")[1])
                with ZipFile(file_info.filename, allowZip64=True) as z_files_sub:
                    for sub_file_info in z_files_sub.infolist():
                        print(sub_file_info)'''



# Path should be path where zip file is located
input_dir = Path.home().joinpath("Desktop", "zip_files")
print(input_dir)
print(input_dir)
# print(Path.home().joinpath("Desktop"))
# glob = specific folder
# rglob = including subfolder
files = list(input_dir.rglob("*.zip"))
# Path = "/Users/purnaraghavaraokalva/Desktop/sampledata.zip"
for each_file in files:
    process_zip(each_file)
