import os
from datetime import datetime


def get_file_modification_datetime(filename, folder=None):
    """
    Ermittelt das letzte Änderungsdatum einer Datei
    :param filename: Dateiname
    :param folder: Pfad. Wenn kein Pfad übergeben wird, wird das aktuelle Arbeitsverzeichnis verwendet.
    :return:
    """
    folder = folder or os.getcwd()
    return datetime.fromtimestamp(os.path.getmtime(f'{folder}\\{filename}'))


def check_if_file_exists(filename, folder=None):
    """
    Überprüft, ob eine Datei existiert.
    :param filename: Dateiname
    :param folder: Pfad. Wenn kein Pfad übergeben wird, wird das aktuelle Arbeitsverzeichnis verwendet.
    :return:
    """
    folder = folder or os.getcwd()
    return os.path.isfile(f'{folder}\\{filename}')