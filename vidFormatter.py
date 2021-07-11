import os

os.chdir(r'')

omit = ['Watch', 'cartoons', 'online', 'English', 'Dubbed','anime','dub',','] #List may need to be modified. Links are often in pieces.

for f in os.listdir():
    fname, ext = os.path.splitext(f)
    ext = ext.strip()
    for o in omit:
        fname = fname.replace(o, '')
    if 'Ova' in fname:
        show, no = fname.split('Ova')
        show, no = show.strip(),no.strip().zfill(2)
        newName = f'{show} Ova {no}{ext}'
    if 'Episode' in fname:
        show, no = fname.split('Episode')
        show, no = show.strip(),no.strip().zfill(2)
        newName = f'{show} Episode {no}{ext}'
    else:
        fname = fname.strip()
        newName = f'{fname}{ext}'
        
    print(newName)
    # !!!Do not execute the next line til sure formatting is good!!!    
    # os.rename(f, newname)
