
# "3D-Simulation" für den KC85/4
In einer Zeit, in der professionelle CAD-Systeme meist auf teuren Workstations liefen, demonstrierte dieses Programm, dass auch auf 8-Bit-Heimcomputern der [KC 85 3/4-Serie](https://www.mpm-kc85.de/), basierend auf dem U880-Prozessor (Z80 Klon), komplexe 3D-Visualisierungen möglich waren. Das Projekt wurde im DDR-Fachmagazin **Mikroprozessortechnik** (Ausgabe 2, 1988) ([PDF](/MP/MP_88_11_3D-Grafik.pdf), [MD](/MP/MP_88_11_3D-Grafik_S328.md)) veröffentlicht. Restaurierung und Aufbereitung erfolgten im Zeitraum 04/2025 - 05/2026.

<br>

![](/Bilder/3D-start.gif)

# Historischer Kontext
Diese Software ist ein sehr interessantes Dokument der DDR-Computergeschichte im Bereich der Softwareentwicklung. Sie beinhaltet ein komplettes Programmpaket, inkl. [Handbuch](/Dokumentation/Handbuch_03-1990.txt), mit umfangreichen Funktionen zur Modellierung und Animation von komplexen 3D-Strukturen. Die Software wurde im Zeitraum 1986-90 von Andreas Thierbach programmiert. 

Als Student in der Fachrichtung Städtebau an der Hochschule für Architektur und Bauwesen (HAB) Weimar war er von den Möglichkeiten der Computergrafik fasziniert. Den Einstieg fand er mit den ersten KCs im Computerclub der Hochschule in der Programmiersprache Basic. Nebenan im Rechenzentrum wurden noch Programme der Studenten in Lochkarten gestanzt. Nachdem er dann als Assistent an der HAB einen eigenen KC 85 erwerben konnte, waren dem nächtlichen "Experimentieren" keine Grenzen mehr gesetzt. Mit den ersten selbst gesteuerten "schnellen" Linien auf dem kleinen Schwarz-Weiß-Fernseher war sein Ehrgeiz entfacht. 

Die Kleincomputer [KC 85 3/4](https://www.mpm-kc85.de/) waren, verglichen mit den Heimcomputern Mitte der 80'er Jahre, mit einer guten Grafikauflösung ausgestattet, hatten jedoch keine spezielle Hardware zur Grafikbeschleunigung und waren vollständig auf die Leistung der CPU mit nur 1,77 MHz Taktfrequenz angewiesen. Die notwendige Verarbeitungsgeschwindigkeit für die Berechnung der 3D-Modelle und für deren Visualisierung war somit nur durch Programmierung in Maschinensprache zu erreichen. Herr Thierbach erlernte als Autodidakt im Selbststudium in U880-Assembler zu programmieren und erstellte das Programm auf dem Entwicklungssystem EDAS.

Das Programm wurde auf der [5. Computerfachtagung in Frankfurt (Oder)](https://www.kc85emu.de/scans/fa0189/Tagung.htm) vorgestellt und für einige städtebauliche Visualisierungen u.a. im Büro für Stadtplanung beim Rat der Stadt Frankfurt (Oder) verwendet.

# Überblick
Das Programm dient der Modellierung geometrischer, formgestalterischer und architektonischer Körper. Die Anwendungsschwerpunkte liegen in der Vermittlung des Raum-Körper-Vorstellungsvermögens, der perspektivischen Darstellung sowie der konkreten Planung in Architektur und Stadtplanung.

# Arbeitsprinzip und Modellbegriff
Das Programm folgt dem Prinzip eines digitalen Baukastens. Nutzer erstellen „Modellbausteine“ beliebiger Form, die zu komplexen Strukturen arrangiert werden können.

*   **Drahtmodell-Ansatz:** Im Gegensatz zu modernen Volumenmodellen nutzt das Programm ein Kanten- und Drahtmodell. Jedes Objekt wird über seine Eckpunkte im kartesischen Koordinatenraum definiert.
*   **Transformation:** Die digitalen Modelldaten werden nach mathematischen Regeln der perspektivischen Darstellung auf die Bildebene transformiert und als Linienmodell ausgegeben.

# Technische Spezifikationen
## Hardware-Anforderungen
              
| Komponente | Spezifikation |
| :--- | :--- |
| Hardware | KC 85/4, M022 (16k), V24-Schnittstelle, M011 (64k) für Ebenentechnik u. hochauflösende Grafik |
| Peripherie | Tastatur, Monitor, Datenrecorder und/oder D004 KC-Floppy-System |
| Erweiterung | Plotter, Grafikdrucker, Videotechnik |

## Datenmengen
                
| Max. Raumpunkte (N) | RAM-Bedarf |
| :--- | :--- |
| ~2000 – 2100  | 16 KByte-Expander |
| ~4200 – 16.300  |für Ebenentechnik: | 
| 3 Ebenen:  |16 und 64 KByte-Expander | 
| 9 Ebenen:  |16 und 256 KByte-Expander | 

N = Anzahl der gespeicherten Raumpunkte, Gesamtspeicherverbrauch: ca. N * 16 Byte 

## Rechenzeiten

| Komplexität der 3D-Darstellung | Rechenzeit
| :--- | :--- |
| einfach | 1 – 5 Sekunden | 
| komplex | 5 – 15 Sekunden |

Der Datenspeicher wird vollautomatisch verwaltet und ist volldynamisch. Die Datenblöcke beanspruchen immer den minimal notwendigen Speicherraum.

## Funktionskatalog

- [Handbuch (TEXOR)](/Dokumentation/Handbuch_03-1990.txt)
- Handbuch (MD)

## Bedienkonzept

*   **Menütechnik:** Funktionen werden direkt über den Anfangsbuchstaben des jeweiligen Befehls aufgerufen (z. B. "P" für PERS).
*   **Fadenkreuztechnik:** Anwahl von Koordinaten mittels Fadenkreuz direkt auf dem Bildschirm, gesteuert durch Cursortasten.

# Entwicklungssystem
Das Original Entwicklungssystem von Andreas Thierbach.

![](/Bilder/KC-50.jpg)

# Emulator
## Einstellungen
Das Programm kann im [JKCEMU](http://www.jens-mueller.org/jkcemu/) mit folgenden Einstellungen emuliert werden:

![](/Bilder/JKCEMU-1.PNG)
![](/Bilder/JKCEMU-2.PNG)
![](/Bilder/JKCEMU-3-75.PNG)
![](/Bilder/DISK.png)

Als Diskette das Verzeichnis [/Disketten/Work](/Disketten/Work) einbinden.

## Programm starten
```
Im Betriebssystem CAOS:

JUMP FC <Enter>
FL <Enter>
GRAFIK <Enter>
```
## Grafik laden und anzeigen
```
Im Programm 3D-Grafik:

Taste ">"
Taste "L"
Eingeben: "STREET.DWG" <Enter>
Taste "P"
```

# Lizenz

Der Autor hat das Programm zur Veröffentlichung für Demonstrationen im Kontext historischer Computertechnik auf GitHub freigegeben. Alle Rechte liegen beim Autor Andreas Thierbach. Kommerzielle Nutzung ist hiermit ausdrücklich untersagt. 

# Danksagung

Besonderer Dank geht an Andreas Thierbach für die Hilfe bei der Sichtung und Restaurierung der alten Datenbestände sowie an Peter Salomon, der durch seine Erinnerungen an die [5. Computerfachtagung in Frankfurt (Oder)](https://www.kc85emu.de/scans/fa0189/Tagung.htm) den Anstoß zur Restaurierung dieses interessanten Projekts gab.

# Quellen

Dieses Projekt nutzt Infos und Software aus den u.g. Quellen.

https://www.mpm-kc85.de/html/D001BasisDevise.htm

https://www.mpm-kc85.de/html/D004FD.htm

https://www.mpm-kc85.de/html/m012_texor.htm

https://kc85.info/

http://www.jens-mueller.org/jkcemu/






