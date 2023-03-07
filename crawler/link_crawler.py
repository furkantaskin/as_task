import cloudscraper

scraper = cloudscraper.create_scraper()


def download_assets(url_list: list) -> bool:
    """

    :param url_list: List of urls to download
    :return: True if all urls were downloaded successfully

    """

    print("\033[0;35m Downloading assets... \033[0m")
    for url in url_list:
        try:
            if "classcentral.com" in url:
                print("\033[0;93m Downloading: \033[0m", url)
                file_name = url.split("/")[-1]
                file_folder: str = url.split("/")[3]
                with open(f"../res/{file_folder}/{file_name}", "wb") as f:
                    f.write(scraper.get(url).content)
                    f.close()
        except IndexError as e:
            print(f"Error for {url}: Reason: {e}")
            return False
    return True