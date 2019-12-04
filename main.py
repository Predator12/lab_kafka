from read_data import Data
from settings import settings


def main():
    data = Data(settings.CONFIG['IMPORT_URL'])
    data.read()


if __name__ == '__main__':
    main()
