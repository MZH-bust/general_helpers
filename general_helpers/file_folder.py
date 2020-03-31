"""Dieses Modul stellt grundlegende Funktionen zum Arbeiten mit Dateien und Ordnern bereit"""

import os
from typing import Union
from pathlib import Path
from datetime import datetime


def get_file_modification_datetime(filename: Union[str, Path], folderpath: Union[str, Path] = None) -> datetime:
    """Ermittelt den letzten Änderungszeitpunkt einer Datei

    Notes
    -----
    **Zusammensetzung des zu verwendenden Dateipfads:**

    Wird ein gesamter Dateipfad als filename übergeben und kein Ordnerpfad, wird dieser Dateipfad verwendet.

    Wird nur ein Dateiname übergeben und ebenfalls kein Ordnerpfad, wird das aktuelle Arbeitsverzeichnis verwendet.

    Wird zusätzlich ein Ordnerpfad übergeben, wird der Dateipfad aus dem Ordnerpfad und dem Dateinamen zusammengesetzt

    Examples
    --------
    >>> get_file_modification_datetime(r"C:\\Users\\Martin.Zoeltsch\\Desktop\\BPMN2_0_Poster_DE.pdf")
        datetime.datetime(2019, 11, 20, 17, 7, 3, 177816)

    >>> get_file_modification_datetime("README.md")
        datetime.datetime(2020, 3, 29, 16, 37, 17, 404701)

    >>> get_file_modification_datetime("README.md", r"C:\\Users\\Martin.Zoeltsch\\Desktop\\Coding\\general_helpers")
        datetime.datetime(2020, 3, 29, 16, 37, 17, 404701)

    Parameters
    ----------
    filename :
        Dateiname oder gesamter Pfad der Datei, deren Änderungszeitpunkt bestimmt werden soll.
    folderpath :
        Ordnerpfad zu dem Ordner, in dem die Datei, deren Änderungszeitpunkt bestimmt werden soll liegt.

    Returns
    -------
    datetime.datetime
        Zeitpunkt der letzten Änderung der Datei

    Raises
    ------
    FileNotFoundError
        Falls die zu verarbeitende Datei nicht existiert.
    """

    if not folderpath:
        filepath = Path(filename)
    else:
        filepath = Path(f'{folderpath}\\{filename}')

    if not filepath.is_file():
        raise FileNotFoundError
    return datetime.fromtimestamp(os.path.getmtime(filepath))


def list_files_in_folder(folderpath: Union[str, Path] = None, file_extension: Union[str, tuple] = "") -> list:
    """Listet alle Dateien eines Ordners auf. Dabei kann eine Filterung nach Dateiendungen optional erfolgen.

    Examples
    --------
    >>> list_files_in_folder(file_extension=".py")
    >>> list_files_in_folder(r"C:\\Users\\Martin.Zoeltsch\\Desktop\\Coding\\general_helpers\\data", (".pptx", ".xlsx")

    Parameters
    ----------
    folderpath :
        Der Pfad, dessen Dateien aufgelistet werden sollen. Wird kein Pfad übergeben, wird das aktuelle
        Arbeitsverzeichnis verwendet.
    file_extension
        String oder Tupel von Strings mit der/den Dateiendung(en), auf die gefiltert werden soll.

    Returns
    -------
    list :
        Liste der passenden Dateinamen im Ordner.

    Raises
    ------
    FileNotFoundError
        Falls der Ordnerpfad nicht existiert oder der Zugriff nicht möglich ist.
    """
    folderpath = Path(folderpath or Path.cwd())
    # if not folderpath.is_dir():
    #     raise FileNotFoundError(f"Das Verzeichnis mit dem folgenden Pfad existiert nicht: {folderpath}")
    try:
        ls_filenames = [filename
                        for filename in os.listdir(folderpath)
                        if (Path(f'{folderpath}\\{filename}').is_file() and filename.lower().endswith(file_extension))]
    except (IOError, OSError):
        raise FileNotFoundError(f"Fehler beim Auflisten der Dateien im Ordner. Ggf. existiert der Ordner nicht:"
                                f" {folderpath}")

    return ls_filenames
