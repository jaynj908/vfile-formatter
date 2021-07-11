import re
import os
import sys

os.chdir('')

count = 0
formatCount = 0

for f in os.listdir():
    title, ext = os.path.splitext(f)
    format = re.compile(
        r'^(?P<show>...+)\s(?P<type>OVA|Episode)\s(?P<epNum>\s|\d*)')

    title = title.replace('Watch', '')
    count = count + 1
    for line in title.splitlines():
        line = line.strip()
        m = format.match(line)
        if m:
            show = m.groupdict()['show']
            show = show.strip()
            type = m.groupdict()['type']
            type = type.strip()
            epNum = m.groupdict()['epNum']
            epNum = epNum.strip().zfill(2)
            ext = ext.strip()
            newName = f'{show} {type} {epNum}{ext}'
            formatCount = formatCount + 1
            print(newName)
print(f'File Count = {count}')
print(f'Formatted Count = {formatCount}')
