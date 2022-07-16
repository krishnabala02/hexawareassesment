from pathlib import Path

input_dir = Path.home().joinpath("Desktop", "zip_files")
print(input_dir)
#print(Path.home().joinpath("Desktop"))
# glob = specific folder
# rglob = including subfolder
files = list(input_dir.rglob("*.zip"))
print(files)
