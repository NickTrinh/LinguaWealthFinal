import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def retrieve_google_drive():
    
    gauth = GoogleAuth()

    path = os.getcwd() + r"\serverside"

    # Load saved client credentials
    gauth.LoadCredentialsFile(path + r"\mycreds.txt")
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile(path + r"\mycreds.txt")

    drive = GoogleDrive(gauth)

    file1 = drive.CreateFile({'parents': [{'id': '1IOCHHbrbhTffv3MjcAxm-AE2t9i4Vsxh'}]})

    file_list = drive.ListFile({'q': "'1IOCHHbrbhTffv3MjcAxm-AE2t9i4Vsxh' in parents and mimeType='text/plain'"}).GetList()

    for file in file_list:
        if file['title'] == 'client_script_file.txt':
            file.GetContentFile(path + r'\client_script_file.txt') 
            break

    filenames = ['client_script_file.txt', 'manager_script_file.txt']

    with open(path + r'\full_script_file.txt', 'w') as outfile:
        for names in filenames:
            with open(path + r"\\" + names) as infile:
                outfile.write(infile.read())
            outfile.write("\n")

    clean = ''.join(l[:-1] for l in open(path + r'\full_script_file.txt'))

    full_script =  open(path + r"\full_script_file.txt")
    lines = sorted(full_script.readlines())
    full_script = open(path + r"\full_script_file.txt", "w")
    full_script.writelines(lines)
    full_script.close()

