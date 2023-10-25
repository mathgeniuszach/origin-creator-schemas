import yaml
import glob
import qfile
import traceback

for f in glob.glob("*/*.yaml"):
    try:
        yaml.safe_load(qfile.read(f))
    except Exception as e:
        print(f'Error loading file "{f}":')
        print("  " + str(e))