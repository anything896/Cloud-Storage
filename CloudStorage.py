import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token

    def upload_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f= open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.ArDMcNNNV2pA3GD5ZhidPLTVygeMtN8l15BJW43-no-uKMgk_ymYnNOECVRqYw_l8Z5SbfO-VCxSDtkPXetOAhtqH7lqi8Y80kgky718RiQLLCe-3HkMKI6ihGMOarkGm3YysCs'
    transferData = TransferData(access_token)

    file_from = input("Enter your file name ")
    file_to = input("Enter the location where you would like to upload ")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved")

main()