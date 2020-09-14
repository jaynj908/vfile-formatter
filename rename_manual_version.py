import os, re, sys 

def path_test():
    try:
        path = input('Enter folder path: ')
        os.chdir = os.chdir('{}'.format(path))
    except FileNotFoundError:
        print('Either file could not be found or wrong drive was selected.')
        print('Make sure path is spelled correctly.')
    except OSError:
        print('Drive Letter missing')
    except SyntaxError:
        print(" You may need to use '\\' in your path.")
    else:
        print(path)
        return path

def parsing():
    a = int(input('Enter the lenght to shorten file name to: '))
    b = a + 1
    c = b + 2
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        if re.match('Watch', f_name):
            show = f_name[6:a].strip()
        else:
            show = f_name[:a].strip()
        ep_num = f_name[b:c].strip().zfill(2)
        new_name = ('{} {}{}'.format(show, ep_num, f_ext))
        print(new_name)

def f_final():
    a = int(input('Enter the lenght to shorten file name to: '))
    b = a + 1
    c = b + 2
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        if re.match('Watch', f_name):
            show = f_name[6:a].strip()
        else:
            show = f_name[:a].strip()
        ep_num = f_name[b:c].strip().zfill(2)
        new_name = ('{} {}{}'.format(show, ep_num, f_ext))
        print(new_name)
        os.rename(f, new_name)
        
def verify():
    test = input('Is filename OK?...>')
    if test == 'y':
        f_final()
    elif test == 'n':
        parsing()
        verify()
    elif test == 'q':
        print('Program stopped...')

path_test()

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    print(f_name + ' ' + f_ext)

print(len(f_name))

parsing()

verify()

print('Finished...')


        



