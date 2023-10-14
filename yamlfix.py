import qfile
import glob
import yaml
import hjson
import re

LIST = re.compile(r"\n((\s*)[^:\s]+:)\n((?:\2 +- .*?\n)+)")

def replm(m: re.Match):
    if m[3].count("- ") >= 7: return m[0]
    if m[3].count(": "): return m[0]
    
    s = "\n" + m[1] + " [" + ", ".join([i.strip() for i in m[3].split("- ") if i.strip()]) + "]\n"

    return s

for f in glob.glob("*/*.yaml"):
    text = qfile.read(f)
    text = LIST.sub(replm, text)
    qfile.write(f, text)
    