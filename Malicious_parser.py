import os
import io
from bs4 import BeautifulSoup

path = "C:\\Users\\17862\\OneDrive\\Desktop\\Datasets\\malicious_data"

os.chdir(path)

def read_File(file_path, file):

    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            #print(lines)
    except Exception as e:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                #print(lines)
        except Exception as e2:
            try:
                with open(file_path, "r", encoding="latin1") as f:
                    lines = f.readlines()
                    # print(lines)
            except Exception as e3:
                return False

    javascript = []
    start = False

    for line in lines:
        if "<script" in line:
            script_Start = line.find("<script")
            line = line[script_Start:]
            #javascript.append(line)
            start = True
        if "</script>" in line:
            script_End = line.find("</script>")
            line = line[:script_End + 9]
            javascript.append(line)
            start = False
        if start == True:
            javascript.append(line)
    try:
        with open("C:\\Users\\17862\\OneDrive\\Desktop\\Datasets\\malicious_js\\" + file + ".js", "w") as f:
            f.writelines(javascript)

    except Exception as e:
        try:
            with open("C:\\Users\\17862\\OneDrive\\Desktop\\Datasets\\malicious_js\\" + file + ".js", "w", encoding="utf-8") as f:
                f.writelines(javascript)
        except Exception as e2:
            try:
                with open("C:\\Users\\17862\\OneDrive\\Desktop\\Datasets\\malicious_js\\" + file + ".js", "w", encoding="latin1") as f:
                    f.writelines(javascript)
            except Exception as e3:
                return False
    return True

for file in os.listdir():

    file_path = f"{path}\{file}"
    #print(file_path)
    read_File(file_path, file)
