import os
import re
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


def sorted_alphanumeric(data):
    """
    Sortiert eine Liste alphanumerisch sinnvoll.
    sorted_aphanumeric(["1", "10", "2", "foo_10", "foo_8"]) ) -> ['1', '2', '10', 'foo_8', 'foo_10']
    :param data: Liste
    :return: sortierte Liste
    """
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)


def get_list_of_pptx_files_from_folder(folder=None):
    """
    Liest alle PPTX/pptx Dateien von einem Ordner ein.
    :param folderpath: Pfad zum Ordner
    :return: Liste der Dateien mit folgenden Informationen als Dict: Dateiname, MA Kürzel, Änderungsdatum,
            Datumsdifferenz seit Änderungsdatum
    """
    folder = folder or os.getcwd()
    try:
        ls_filenames = [{"filename": filename,
                         "ModificationDate": get_file_modification_datetime(filename, folder),
                         }
                        for filename in os.listdir(folder)
                        if (os.path.isfile(f'{folder}\\{filename}') and filename.lower().endswith(".pptx"))]
    except (IOError, OSError) as e:
        print(e)
        return e

    return ls_filenames
