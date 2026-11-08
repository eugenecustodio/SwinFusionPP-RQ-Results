"""List every decimal number in the Chapter 4 prose and say where it is backed: a table CSV cell,
KEY_NUMBERS.md, or nowhere (to be checked by hand). Usage: python check_numbers.py"""
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ch4_content as C  # noqa: E402

src = Path(C.__file__).read_text()
start, end = src.index('def chapter4('), src.index('# Chapter 3 amendment')
prose = ''.join(re.findall(r"'((?:[^'\\]|\\.)*)'", src[start:end]))
num = re.compile(r'[+−-]?\d+\.\d+%?')
cells = set()
for f in C.TAB.glob('*.csv'):
    for row in csv.reader(open(f, newline='')):
        for c in row:
            cells.update(m.lstrip('+−-').rstrip('%') for m in num.findall(c))
            cells.add(c.strip())
key = (C.TAB / 'KEY_NUMBERS.md').read_text() if (C.TAB / 'KEY_NUMBERS.md').exists() else ''
keynums = set(m.lstrip('+−-').rstrip('%') for m in num.findall(key))
missing = []
for m in sorted(set(num.findall(prose))):
    bare = m.lstrip('+−-').rstrip('%')
    where = 'table' if bare in cells else ('KEY_NUMBERS' if bare in keynums else None)
    if where is None:
        missing.append(m)
print(f'{len(set(num.findall(prose)))} distinct decimal numbers in the prose; {len(missing)} not found in any table or KEY_NUMBERS:')
for m in missing:
    i = prose.find(m)
    print(f'  {m:>10}  …{prose[max(0, i - 70):i + 20]}…')
