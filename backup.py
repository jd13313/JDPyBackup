import os
import datetime
import tarfile


'''
    List of directories to be backed up and their names
'''

backup_list = [
    {
        'path': 'C:\\Users\Jeremy\Documents',
        'name': 'Local Documents'
    },
    {
        'path': 'C:\\Users\Jeremy\Desktop',
        'name': 'Desktop'
    },
    {
        'path': 'C:\\Users\Jeremy\Pictures',
        'name': 'Local Pictures'
    },
    {
        'path': 'C:\World of Warcraft\Screenshots',
        'name': 'WoW Screenshots'
    },
    {
        'path': 'C:\World of Warcraft\Interface',
        'name': 'WoW Plugins'
    },
    {
        'path': 'D:\Projects',
        'name': 'Projects'
    },
    {
        'path': 'Z:\Docs',
        'name': 'Server Documents'
    },
    {
        'path': 'Z:\Photos',
        'name': 'Server Photos'
    },
    {
        'path': 'Z:\Sites',
        'name': 'Server Sites'
    }
]

'''
    Generate target directory if it doesn't exist
'''

current_date = datetime.datetime.now()
destination_dir = 'Z:\Backups\\' + current_date.strftime('%Y/%m/%d')

if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

'''
    Iterate through backup list, compressing directories and then moving them to Z drive for future sync to Google Drive.
'''
for dir in backup_list:
    print('Backing up ' + dir['path'] + '...')

    try:
        tar = tarfile.open(destination_dir + '/' + dir['name'] + '.tar.bz2', 'w:bz2', compresslevel=9)
        tar.add(dir['path'], arcname=dir['name'])
        tar.close()
    except IOError:
        print('Window sucks, skipping this non-existent file...')
    finally:
        print(dir['path'] + ' backed up successfully!')
