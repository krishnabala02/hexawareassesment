# importing the module
import re
import pandas as pd
import datetime

# initializing the list objects
valid = []
unique_valid = []
invalid = []
# declaring the regex pattern for IP addresses numbers
pattern = re.compile("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}"
                     "(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$")

# opening and reading the file
try:
    with open('/Users/purnaraghavaraokalva/Desktop/sampleip.txt') as fh:
        string = fh.readlines()
except FileNotFoundError:
    print("Sorry,the file does not exist")


def ipextraction():
    # extracting the IP addresses
    for line in string:
        for word in line.split():
            result = pattern.search(word)
            # valid IP addresses
            if result:
                valid.append(word)

            # invalid IP addresses
            else:
                invalid.append(word)


# function to get unique IP values
def unique(valid):
    # traverse for all elements
    for x in valid:
        # check if exists in unique_list or not
        if x not in unique_valid:
            unique_valid.append(x)


# Function to write to file
def write_to_file():
    Df = pd.DataFrame(
        {
            "IP": unique_valid
        }
    )
    print(Df)
    Df.to_csv("outputIPfile_" + str(datetime.datetime.now()) + ".csv", index=False)


ipextraction()
unique(valid)
write_to_file()
