# genutil
Dieses Repository beinhaltet übergreifende Hilfsfunktionen, die so allgemein sind, dass sie in mehreren Projekten 
Anwendung finden. Ziel dabei ist es, doppelten Code in diversen Projekten zu vermeiden.  
Link: <https://github.com/MZH-bust/genutil>

## Installation: 
    pip3 install git+https://github.com/MZH-bust/genutil.git#egg=genutil

## Dokumentation:
[Link zur PDF Dokumentation](docs/build/pdf/genutildoc.pdf)  
[Link zur HTML Dokumentation](https://htmlpreview.github.io/?https://github.com/MZH-bust/genutil/blob/master/docs/build/html/index.html)

## Vorteile:
* Zentrale Wartung und Weiterentwicklung an einer Stelle.
* Zentrale Fehlerbehebung statt in jedem einzelnen Projekt. 

## Testing
Das Testing erfolgt mit pytest. Alle Testcases liegen im Ordner "tests". 
Für manche Testcases sind zusätzliche Testdaten erforderlich. Diese liegen im Ordner "tests/data".  
Für das Testing des E-Mail Moduls ist eine Verbindung zum SMTP Server erforderlich. 


## Dokumentationserstellung
**Aktualisierung der HTML- und PDF Dokumentation**  
`sphinx-apidoc -f -o source/ ../genutil/ & make html & sphinx-build -b pdf source build/pdf`

**Erläuterung:**
* SPHINX sources erzeugen mit: 
    `sphinx-apidoc -f -o source/ ../genutil/`
* HTML Dokumentation erzeugen mit  
    `make html`
* PDF Dokumentation erzeugen mit: 
    `sphinx-build -b pdf source build/pdf`
