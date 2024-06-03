import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def upload_google_drive():

    gauth = GoogleAuth()
    path = os.getcwd() + r"\clientside"
    # Load saved client credentials
    gauth.LoadCredentialsFile(path + r'\mycreds.txt')
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
    gauth.SaveCredentialsFile(path + r'\mycreds.txt')

    drive = GoogleDrive(gauth)

    fileList = drive.ListFile({'q': "'1IOCHHbrbhTffv3MjcAxm-AE2t9i4Vsxh' in parents and mimeType='text/plain'"}).GetList()

    for e in fileList:
        drive.CreateFile({'id': e['id']}).Trash()

    file1 = drive.CreateFile({'parents': [{'id': '1IOCHHbrbhTffv3MjcAxm-AE2t9i4Vsxh'}]})
    file1.SetContentFile(path + r'\client_script_file.txt')
    file1['title'] = 'client_script_file.txt'
    file1.Upload()
