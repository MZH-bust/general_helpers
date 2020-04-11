"""Dieses Modul stellt Hilfsfunktionen zur Arbeit mit Daten aus Sharepoint zur Verfügung"""

import re


class SpFieldText:
    """
    Die Klasse stellt Möglichkeiten zur Verarbeitung von Informationen in Sharepoint Feldern bereit.
    z.B. Entfernen der Identifier aus dem Text oder Extraktion einer Liste der Identifier oder Werte aus einem Feld.
    Hintergrund: Werden Sharepointfelder als String aus Sharepoint ausgelesen, enthalten diese neben dem Wert des
    Felds häufig auch zusätzlich einen Identifier. Dies kann bei der weiteren Datenverarbeitung hilfreich oder störend
    sein.

    Attributes
    ----------
    field_text : str
    identifier_value_list : list
        Liste von Tupeln in der folgenden Form:
        [
        ("Identifier1", "Feldwert1),
        ("Identifier2", "Feldwert2),
        ...
        ]
    identifier_value_list_transponed : list
        Liste von Tupeln in der folgenden Form:
        [
        ("Identifier1", "Identifier2, ...),
        ("Feldwert1", "Feldwert2, ...)
        ]

    """
    def __init__(self, field_text: str):
        """

        Parameters
        ----------
        field_text : str
            Feldtext des Sharepoint-Felds
        """
        self.field_text = field_text
        self.identifier_value_list = self._get_identifier_and_values_from_string()
        self.identifier_value_list_transponed = self._transpone_identifier_value_list()

    def _get_identifier_and_values_from_string(self):
        """ Teilt den String "self.field_text" anhand der Sharepoint Identifier auf.

        Returns
        -------
        list :
            Gibt eine Liste von Tupeln in folgendem Format zurück:
            [
            ("Identifier1", "Feldwert1),
            ("Identifier2", "Feldwert2),
            ...
            ]
        """
        # Erklärung zum regulären Ausdruck:
        # (?:\d+;#|^) : Entweder (Eine oder mehrere Ziffern gefolgt von ";#") oder (Anfang des Strings)
        # (.*?) : Beliebiger Text in der Mitte <-- Rückgabewert
        # (?:;#|$) : Ende mit ";#" oder Zeilenende
        return re.findall(r"(?:(\d+);#|^)(.*?)(?:;#|$)", self.field_text)

    def _transpone_identifier_value_list(self):
        """ Transponiert die Liste self.identifier_value_list

        Returns
        -------
        list:
            Gibt eine Liste von Tupeln in folgendem Format zurück:
            [
            ("Identifier1", "Identifier2, ...),
            ("Feldwert1", "Feldwert2, ...)
            ]
        """
        return [*zip(*self.identifier_value_list)]

    def cleanse_text(self, delimiter: str = "; ") -> str:
        """Gibt einen um die Sharepoint Identifier bereinigten Text zurück.

        Parameters
        ----------
        delimiter : str
            Trennzeichen, das zwischen den einzelnen Werten gesetzt werden soll.

        Returns
        -------
        str:
            Bereinigter Feldtext ohne die Sharepoint Identifier.

        """
        return delimiter.join(self.identifier_value_list_transponed[1])

    def get_identifier_list(self) -> list:
        """ Gibt eine Liste aller Sharepoint Identifier des Felds zurück"""
        return list(self.identifier_value_list_transponed[0])

    def get_value_list(self) -> list:
        """ Gibt eine Liste aller Sharepoint Werte des Felds zurück"""
        return list(self.identifier_value_list_transponed[1])
