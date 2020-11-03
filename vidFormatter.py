import os

# Set the folder to be formatted
os.chdir(r'E:\SHOWS\LOVE CHUNIBYO')

# List of strings to be removed from each filename
omit = ['English', 'Dubbed',  'Watch', 'cartoons', 'online',
        'Watch', 'anime', 'online', 'English', 'dub', 'anime']

# String pattern to be used to split each filename
episodeString = 'Episode'
movieString = 'Movie'
ovaString = 'OVA'
specialString = 'Special'
ovaAndEpisodeString = 'OVA Episode'
episodeAndOVAstring = 'Episode OVA'
# List will store the filenames with the new name
collection = []
originalFileName = []
# Counter is needed to ensure each file is actually formatted. In early version, if the file was formatted, that file would be ommitted entirely. Even though in this version this will not happer (or shouldn't), the counter will ensure the same number of files going in will go out reguardless if it has a new name or not.
count = 0
formatCount = 0
missingFiles = count - formatCount

# Format each file
for f in os.listdir():
    fname, ext = os.path.splitext(f)
    ext = ext.strip()
    originalFileName.append(fname)
    for word in omit:
        fname = fname.replace(word, '')
        if episodeString in fname:
            show, num = fname.split('Episode')
            for spec in num:
                if spec == ',':
                    num = num.replace(',', '')
            show, num = show.strip(), num.strip().zfill(2)
            newName = f'{show} Episode {num}{ext}'
        if ovaString in fname:
            show, num = fname.split('OVA')
            for spec in num:
                if spec == ',':
                    num = num.replace(',', '')
            show, num = show.strip(), num.strip().zfill(2)
            if num == '00':
                newName = f'{show} OVA{ext}'
            else:
                newName = f'{show} OVA {num}{ext}'
        if movieString in fname:
            show, num = fname.split('Movie')
            show, num = show.strip(), num.strip().zfill(2)
            if num == '00':
                newName = f'{show} Movie{ext}'
            else:
                newName = f'{show} Movie {num}{ext}'
        if specialString in fname:
            show, num = fname.split('Special')
            show, num = show.strip(), num.strip().zfill(2)
            newName = f'{show} Special {num}{ext}'
        if ovaAndEpisodeString in fname:
            show, num = fname.split('Episode')
            show, num = show.strip(), num.strip().zfill(2)
            newName = f'{show} Episode {num}{ext}'
        if episodeAndOVAstring in fname:
            show, num, ova = fname.split('Episode')
            for spec in num:
                if spec == ',':
                    num = num.replace(',', '')
            show, num, ova = show.strip(), num.strip().zfill(2), ova.strip()
            newName = f'{show} Episode {num}{ext}'
    collection.append(newName)
    count += 1
    print(newName)
# This will go into os.rename definition
print('')
print('Number of show tiltes: %s' % count)
print('-------------------------')
for tiles, og in zip(collection, originalFileName):
    print(og + ' Renamed to:  %s' % tiles)
    formatCount += 1
print('')
print('Total files formatted: %s' % formatCount)
print('-------------------------')
if count == formatCount:
    print('All files in folder are accounted for')
else:
    print('Number of files missing after format: %s' % missingFiles)
