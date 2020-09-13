import os

def remake(x):
    print('Will be renamed==>', x)

#Open the foler and get a list of files. Split the file and file extension
def nameCheck():
    for f in os.listdir():
        fileName, fileExt = os.path.splitext(f)
        fileName = fileName.strip()
        for word in omitWordList:
            fileName = fileName.replace(word, '')

        #Split the fileName and Episode number. 
        show, episodeNum = fileName.split('Episode')
        #Strip away empty space and fill episodeNum with a zero so shows will play correctly in a playlist
        show, episodeNum, fileExt = show.strip(), episodeNum.strip().zfill(2),fileExt.strip()
        #Set the format you want the shows to appear
        newName = f'{show} Episode {episodeNum}{fileExt}'
        #Preview the format before committing to changes
        remake(newName)
        

def editName():
    for f in os.listdir():
        fileName, fileExt = os.path.splitext(f)
        fileName = fileName.strip()
        for word in omitWordList:
            fileName = fileName.replace(word, '')

        #Split the fileName and Episode number. 
        show, episodeNum = fileName.split('Episode')
        #Strip away empty space and fill episodeNum with a zero so shows will play correctly in a playlist
        show, episodeNum, fileExt = show.strip(), episodeNum.strip().zfill(2),fileExt.strip()
        #Set the format you want the shows to appear
        newName = f'{show} Episode {episodeNum}{fileExt}'
        #Preview the format before committing to changes
        os.rename(f, newName)

#Change to cwd to the file we need to edit
def workPath():
    pattern = input('==>Enter Folder: ')
    os.chdir(r'{}'.format(pattern))

#Create a list of words and characters to be removed while parsing
omitWordList = ['English','Dubbed','Watch','cartoons','online','anime','dub','anime',',','Online','-','  ','–']

workPath()

nameCheck()

#After user checks the filenames and make sure editing is good. 
userInput = input('==>Verify names are good: ')

if userInput == 'y':
    editName()
else:
    print('Review files in folder. If you felt rename should have been good, you may have to edit more words or characters to omit list')

