import re
import os
import sys

os.chdir(r'')

count = 0
formatCount = 0

for f in os.listdir():
    title, ext = os.path.splitext(f)
    format = re.compile(
        r'^(?P<show>...+)\s(?P<type>OVA|Episode|.+)\s(?P<epNum>\s|\d*)')

    # Remove, fix, replace words and phrases
    title = title.replace('Watch', '')
    title = title.replace('cartoons online,', '')
    title = title.replace('anime online,', '')
    title = title.replace('English dub anime', '')
    title = title.replace('Bungou', 'Bungo')
    title = title.replace('English', '')
    title = title.replace('Dubbed', '')
    ext = ext.replace('.crdownload', '.mp4')

    # Parse regex groups
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

            # Remove Ova = 00
            if epNum == "00":
                newName = f'{show} {type}{ext}'
            else:
                newName = f'{show} {type} {epNum}{ext}'

            formatCount = formatCount + 1

            # Check the output first before renaming filename
            print(newName)
            # os.rename(f, newName)
print(f'File Count = {count}')
print(f'Formatted Count = {formatCount}')
