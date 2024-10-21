import qfile
import glob
import yaml
import re

LIST = re.compile(r"(?<=\n)((?:\s*)[^:\s]+:)\n((\s+)- .*?\n(?:\3- .*?\n|[ \t]*\n)*)")

def replm(m: re.Match):
    if m[2].count("- ") >= 7 or m[2].count(":") or m[2].count("#"): return m[0]
    
    s = m[1] + " [" + ", ".join([i.strip() for i in m[2].split("- ") if i.strip()]) + "]\n"

    return s

for f in glob.glob("**/*.yaml", recursive=True):
    text = "\n" + qfile.read(f).strip() + "\n"
    text = LIST.sub(replm, text)
    qfile.write(f, text[1:])
    