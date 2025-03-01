from urllib.parse import urlparse
from app.settings import get_settings

settings = get_settings()

def formated_file (filename: str, folder: str, size: int = 56):
    files_obj_in = {
        'name': filename,
        'folder': folder,
        'ext': filename.split('.')[-1],
        'size': size,
        'path': f"https://s3.amazonaws.com/{settings.BUCKET_NAME}/{folder}/{filename}"
    }

    return files_obj_in

def formated_url_file (url: str): 
    parsed_url = urlparse(url=url)
    path = parsed_url.path
    path_components = path.split('/')
    folder = path_components[-2]
    filename = path_components[-1]
    files_obj_in = formated_file(filename=filename, folder=folder)
    return files_obj_in