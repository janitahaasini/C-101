import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A7RrHAbF_GdLOtM09L-sskGXbaUi1im5M-jsblXWp2RrZRkS3kG1A8w9fCKsA-BXcNuxf9yg55UI9ZxyokfcYN4QN-OO3MDKDv_fRT80gF3S-5NeLgOc1FF40UYtvtDi5oLlAEI'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()