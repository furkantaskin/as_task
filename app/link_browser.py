from playwright.sync_api import sync_playwright, Playwright


def edit_link():

    """

    This function edits the links in the links.txt file and saves them to links_new.txt.
    Steps are
    1. Read the links from the file
    2. Check if the link starts with /, if yes then add https://www.classcentral.com to it
    3. Remove the spaces from the link
    4. Remove the duplicates from the list
    5. Save the links to links_new.text

    """

    print("\033[0;96m Editing links \033[0m")

    # Read the links from the file
    with open("temp_data/links.txt", "r") as f:
        links = f.readlines()
        f.close()

    # Check if the link starts with /, if yes then add https://www.classcentral.com to it and remove spaces
    for index, link in enumerate(links):
        if link[0] == "/":
            link = "https://www.classcentral.com" + link
            links[index] = link.replace(" ", "")

    # Write new links to file
    with open("temp_data/links_new.txt", "w") as f:
        print("\033[0;96m Saving links to file \033[0m")
        for link in [*set(links)]:
            f.write(link)
        f.close()
