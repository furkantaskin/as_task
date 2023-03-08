import os


async def save_page(content: str, file_name: str, length: int) -> bool:
    print("\n\033[0;96m Saving page... \033[0m")
    try:
        if length == 2:
            os.makedirs(f"docs/{file_name.split('/')[0]}", exist_ok=True)
            with open(f"docs/{file_name}.html", "w", encoding="utf-8") as f:
                f.write(content)
                f.close()
        elif length == 3:
            os.makedirs(f"docs/{file_name.split('/')[0]}/{file_name.split('/')[1]}", exist_ok=True)
            with open(f"docs/{file_name}.html", "w", encoding="utf-8") as f:
                f.write(content)
                f.close()
        else:
            with open(f"docs/{file_name}.html", "w", encoding="utf-8") as f:
                f.write(content)
                f.close()
    except Exception as e:
        print(f"\033[0;91m An error occured while saving {file_name}. Reason:  ", e, "\033[0m")
        return False
    print(f"\033[0;92m {file_name} saved successfully \033[0m")
    return True
