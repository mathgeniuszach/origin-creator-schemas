import qfile
import glob
import yaml
import hjson
import re

MLDESC = re.compile(r"^( *)desc: '((?:[^']|'')*?)'(?!')", re.MULTILINE)
HYPHEN = re.compile(r"^( *)- +", re.MULTILINE)

for f in glob.glob("*/*.hjson"):
    y = f[:-5] + "yaml"
    text = yaml.safe_dump(hjson.loads(qfile.read(f), object_hook=dict), indent=4, sort_keys=False, width=10000)
    text = text.replace("\n\n", "\n")
    text = HYPHEN.sub(r"\1  - ", text)
    text = MLDESC.sub(r"\1desc: |\n\1    \2", text).replace("''", "'")
    qfile.write(y, text)
    qfile.delete(f)