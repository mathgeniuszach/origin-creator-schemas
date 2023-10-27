import yaml
import glob
import qfile
import traceback

files = glob.glob("*/*.yaml")
files.sort()

for f in files:
    print(f'Testing "{f}"                ', end='\r')
    try:
        yaml.safe_load(qfile.read(f))
    except Exception as e:
        print(f'Error loading file "{f}":')
        print("  " + str(e) + "          ")

print("All files passed                   ")