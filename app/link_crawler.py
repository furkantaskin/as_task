import cloudscraper
import os

scraper = cloudscraper.create_scraper()


def download_assets(url_list: list) -> bool:
    """

    It will download the assets from the list of urls provided. It will create a folder for each domain name extracted
    from the url. For example if url is like http://www.example.com/assets/assetname.js then it will create a folder
    named assets inside the res folder and save the file as assetname.js in it.

    :param url_list: List of urls to download
    :return: True if all urls were downloaded successfully

    """

    print("\033[0;35m Downloading assets... \033[0m")
    # For each url in the list, download the file and save it in the res folder.
    # Show progress for to detect how many files are downloaded.
    for i, url in enumerate(url_list, start=1):
        try:
            if "classcentral.com" in url:
                square = "#" * i
                underscore = "_" * (len(url_list) - i)
                print("\r", end=f"\033[0;93m {square+underscore} Downloading: \033[0m {url}")
                file_name = url.split("/")[-1]
                file_folder: str = url.split("/")[3]
                os.makedirs(f"res/{file_folder}", exist_ok=True)
                with open(f"res/{file_folder}/{file_name}", "wb") as f:
                    f.write(scraper.get(url).content)
                    f.close()
        except IndexError as e:
            print(f"Error for {url}: Reason: {e}")
            return False
    return True