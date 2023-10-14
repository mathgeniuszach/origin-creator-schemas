import yaml
import glob
import qfile

for f in glob.glob("*/*.yaml"):
    yaml.safe_load(qfile.read(f))