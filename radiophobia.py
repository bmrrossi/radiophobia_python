import os
import csv
import time
import functools

STATIONS_FILE = 'stations.csv'
MPLAYER = '/usr/bin/mplayer'


def timer(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        begin = time.time()
        func(self)
        total = time.time() - begin
        print(f'Time: {total}')
    return wrapper


class Radiophobia:

    # only for tests, it works even without it and it will create the class in the same way
    def __new__(cls):
        return super().__new__(cls)

    def __init__(self, version='2.0.0'):
        self.version = version

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name} - version:{self.version!r}'

    @property
    def version(self):
        return self._version_radio
    
    @version.setter
    def version(self, version):
        self._version_radio = version

    @timer
    def play(self):
        print('-' * 100)
        self.read_all_stations()
        print('-' * 100)

        print("Choose your station by number: ", end='')
        self.station = input()
        self.url = self.get_url(self.station)

        self.start_player(self.url)

    def read_all_stations(self):
        with open(STATIONS_FILE, newline='', encoding='utf8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')

            for row in reader:
                print(' - '.join(row))

    def get_url(self, choosen_station, /):
        with open(STATIONS_FILE, newline='', encoding='utf8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')

            for row in reader:
                if row[0] == choosen_station:
                    return row[2]

    def start_player(self, url):
        cmd = "{player} '{url}'".format(player=MPLAYER, url=url)
        os.system(cmd)


if __name__ == "__main__":
    radiophobia = Radiophobia()
    radiophobia.version = '1.0.0'
    print(f'Radiophobia - Version: {radiophobia.version}')
    radiophobia.play()
