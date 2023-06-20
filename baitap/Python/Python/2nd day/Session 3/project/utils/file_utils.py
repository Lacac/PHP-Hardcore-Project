import re
def fhand(file_name):
    try:
        with open(file_name, "r") as file:
            array = re.split("[^a-zA-Z']+", file.read())
            return array
    except Exception:
        print(f"Can't open file name: {file_name}\n")
    finally:
        file.close()
        