import os.path
from pyunpack import Archive

def extract():
    """Extract data files from colombia-data.7z, in order 
    to save space in repo.

    requirements: pyunpack and patool
        `pip install pyunpack patool`
    """
    path = os.path.join('data', 'colombia-data.7z')
    Archive(path).extractall('data')


# def __name__ = "__main__i":
#     extract()
