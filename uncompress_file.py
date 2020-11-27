import os.path
from pyunpack import Archive

def extract():
    """Extract data files from colombia-data.7z
    Why?: save space in repository.
    """
    path = os.path.join('data', 'colombia-data.7z')
    Archive(path).extractall('data')
