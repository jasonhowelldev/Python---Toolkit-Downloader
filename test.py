# TODO
# daisy chaing downloads, right now only the first one downloads

import subprocess
import os
import asyncio

# this is the folder all downloaded files are saved to
saved_file_folder_path = "c:\\Sources2\\"


# def runcmd(cmd, verbose = False, *args, **kwargs):

#     process = subprocess.Popen(
#         cmd,
#         cwd=os.path.dirname(__file__),
#         stdout = subprocess.PIPE,
#         stderr = subprocess.PIPE,
#         text = True,
#         shell = True
#     )
#     std_out, std_err = process.communicate()
#     if verbose:
#         print(std_out.strip(), std_err)
#     pass
# runcmd('echo "Hello, World!"', verbose = True)


# urlCrystalDisk = "https://osdn.net/dl/crystaldiskinfo/CrystalDiskInfo8_17_14.zip"
# urlFirefox = "https://download-installer.cdn.mozilla.net/pub/firefox/releases/112.0.1/win32/en-US/Firefox%20Installer.exe"

# download all files simulataneously from a list of urls

urls = ["https://osdn.net/dl/crystaldiskinfo/CrystalDiskInfo8_17_14.zip", "https://download-installer.cdn.mozilla.net/pub/firefox/releases/112.0.1/win32/en-US/Firefox%20Installer.exe"]

# wget needs each url on a new line in a text file

# create file to list each url on a new line
file_with_list_of_urls = os.path.dirname(__file__) + '\\urls.txt'
print('====== FILE PATH OF EXECUTABLE ====', os.path.dirname(__file__)) # location of this python file that is being ran
print('====== FILE PATH TO URLS ====', file_with_list_of_urls) # create urls.txt in the same folder as this python file

# write each urls to a new line in the file we just created
with open(file_with_list_of_urls,'w') as file_path:
    for url in urls:
        file_path.write("%s\n" % url)
    print('done writing urls to text file')

print( os.path.dirname(__file__) + "\\wget\\wget" ) # wget is distributed in a subfoler called wget

# create subprocess which call wget in a  command prompt
downloading_of_files = subprocess.Popen( [ os.path.dirname(__file__) + "\\wget\\wget", '-N', '-i', file_with_list_of_urls, '-P', saved_file_folder_path, "--show-progress" ], stdout=subprocess.PIPE, universal_newlines=True, shell=True )

# while subprocess is running, get output to print it, which allows us to see the progress of the file downloads
# todo, display this to the user
while True:
    output = downloading_of_files.stdout.readline()
    print(output.strip())

    return_code = downloading_of_files.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
        # process finished, read rest of output
        for output in downloading_of_files.stdout.readlines():
            print(output.strip())
        break