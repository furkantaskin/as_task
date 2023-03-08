from decouple import config
import requests
import os
import time

def use_proxy(address: str) -> str:
    proxy = config("PROXY")
    proxies = {"http": proxy, "https": proxy}
    response = requests.get(address, proxies=proxies, verify=False)
    return response.text


def download_assets():
    """

    It will download the assets from the list of urls provided. It will create a folder for each domain name extracted
    from the url. For example if url is like http://www.example.com/assets/assetname.js then it will create a folder
    named assets inside the res folder and save the file as assetname.js in it.

    @todo Fix structure for assets which has another subfolder. Example http://www.example.com/assets/js/assetname.js

    :return: True if all urls were downloaded successfully

    """

    with open("../temp_data/asset_list.txt", "r", encoding="utf-8") as f:
        url_list = [*set(f.readlines())]
        f.close()

    print("\033[0;35m Downloading assets... \033[0m")
    # For each url in the list, download the file and save it in the res folder.
    # Show progress to detect how many files are downloaded.
    for i, url in enumerate(url_list, start=1):
        try:
            if "classcentral.com" in url:
                # Generate progress bar with length of files to download

                print("\r", end=f"\033[0;93m ({i}/{len(url_list)}) Downloading: \033[0m {url}")

                # Generate file name and folder name from the url
                file_name = url.split("/")[-1].replace("\n", "")
                temp_folder = url.split("/")
                file_dir = "/".join(temp_folder[3:-1])
                print("Create folder: ", file_dir)

                for f_name in temp_folder[3:-1]:
                    folder_dir = "/".join(temp_folder[3:temp_folder.index(f_name) + 1])
                    print("Creating folder: ", folder_dir)
                    os.makedirs(f"../docs/{folder_dir}", exist_ok=True)
                # Download the file and save it in the specified folder

                with open(f"../docs/{file_dir}/{file_name.split('?')[0] if '?' in file_name else file_name}", "w",
                          encoding="utf-8") as f:
                    if file_name.split('.')[-1] != "woff2":
                        result = use_proxy(url.replace("\n", ""))
                        f.write(result)
                    else:
                        print("\033[0;93m Skipping woff2 file \033[0m")
                    f.close()

                time.sleep(5)
            else:
                print("\r", end=f"\033[0;93m ({i}/{len(url_list)}) Skipping: \033[0m {url}")

        except IndexError as e:
            print(f"IndexError for {url}: Reason: {e}")
            return False

    return True


download_assets()
