# TODO
# daisy chaing downloads, right now only the first one downloads

import subprocess
import os

# this is the folder all downloaded files are saved to
saved_file_folder_path = "c:\\Sources2\\"


# def runcmd(cmd, verbose = False, *args, **kwargs):

#     process = subprocess.Popen(
#         cmd,
#         cwd="./Python---Toolkit-Downloader/wget",
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


def wgetDownload(url, out_dir = saved_file_folder_path, verbose=False):
    process = subprocess.Popen(
        f"wget -P {out_dir} {url}",
        cwd = "./Python---Toolkit-Downloader/wget",
        shell = True,
        text= True,
        stdout=subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass
# wgetDownload("https://download-installer.cdn.mozilla.net/pub/firefox/releases/112.0.1/win32/en-US/Firefox%20Installer.exe", verbose = True)


urlCrystalDisk = "https://osdn.net/dl/crystaldiskinfo/CrystalDiskInfo8_17_14.zip"
urlFirefox = "https://download-installer.cdn.mozilla.net/pub/firefox/releases/112.0.1/win32/en-US/Firefox%20Installer.exe"


wgetDownload(urlCrystalDisk, verbose = True)
wgetDownload(urlFirefox, verbose = True)
