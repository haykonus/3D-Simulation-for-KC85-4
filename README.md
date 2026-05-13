[Deutsch](https://github.com/haykonus/3D-Simulation-for-KC85-4) | [English](https://github-com.translate.goog/haykonus/3D-Simulation-for-KC85-4?_x_tr_sl=de&_x_tr_tl=en&_x_tr_hl=de&_x_tr_pto=wapp)

<details>
<summary> <b>Inhalt</b> <br> </summary>
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<br>

- ["3D-Simulation" für den KC85/4](#3d-simulation-f%C3%BCr-den-kc854)
- [Historischer Kontext](#historischer-kontext)
- [Überblick](#%C3%9Cberblick)
- [Arbeitsprinzip und Modellbegriff](#arbeitsprinzip-und-modellbegriff)
- [Technische Spezifikationen](#technische-spezifikationen)
  - [Hardware-Anforderungen](#hardware-anforderungen)
  - [Datenmengen](#datenmengen)
  - [Rechenzeiten](#rechenzeiten)
  - [Funktionskatalog](#funktionskatalog)
  - [Handbuch](#handbuch)
  - [Bedienkonzept](#bedienkonzept)
- [Entwicklungssystem](#entwicklungssystem)
- [Emulator](#emulator)
  - [Einstellungen](#einstellungen)
  - [Programm starten](#programm-starten)
  - [Grafik laden und anzeigen](#grafik-laden-und-anzeigen)
- [Lizenz](#lizenz)
- [Danksagung](#danksagung)
- [Quellen](#quellen)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
</details>

# "3D-Simulation" für den KC85/4
In einer Zeit, in der professionelle CAD-Systeme meist auf teuren Workstations liefen, demonstrierte dieses Programm, dass auch auf 8-Bit-Heimcomputern der [KC 85 3/4-Serie](https://www.mpm-kc85.de/html/D001BasisDevise.htm), basierend auf dem U880-Prozessor (Z80 Klon), komplexe 3D-Visualisierungen möglich waren. Das Projekt wurde im DDR-Fachmagazin **Mikroprozessortechnik** (Ausgabe 2, 1988) ([PDF](/MP/MP_88_11_3D-Grafik.pdf), [MD](/MP/MP_88_11_3D-Grafik_S328.md)) veröffentlicht. 

Restaurierung und Aufbereitung erfolgten im Zeitraum 04/2025 - 05/2026.

<br>

![](/Bilder/3D-start.gif)

# Historischer Kontext
Diese Software ist ein sehr interessantes Dokument der DDR-Computergeschichte im Bereich Softwareentwicklung. Sie beinhaltet ein komplettes Programmpaket, inkl. [Handbuch (deutsch)](/Dokumentation/Handbuch_03-1990.md), mit umfangreichen Funktionen zur Modellierung und Animation von komplexen 3D-Strukturen. Die Software wurde im Zeitraum 1986-90 von Andreas Thierbach programmiert. 

Die Kleincomputer [KC 85 3/4](https://www.mpm-kc85.de/html/D001BasisDevise.htm) waren, verglichen mit den Heimcomputern Mitte der 80'er Jahre, mit einer guten Grafikauflösung ausgestattet, hatten jedoch keine spezielle Hardware zur Grafikbeschleunigung und waren vollständig auf die Leistung der CPU mit nur 1,77 MHz Taktfrequenz angewiesen. Die notwendige Verarbeitungsgeschwindigkeit für die Berechnung der 3D-Modelle und für deren Visualisierung war somit nur durch Programmierung in Maschinensprache zu erreichen. Herr Thierbach erlernte als Autodidakt im Selbststudium in U880-Assembler zu programmieren und erstellte das Programm auf dem KC-Entwicklungssystem [EDAS](https://www.mpm-kc85.de/html/m027_entwicklung.htm).

Das Programm wurde auf der [5. Computerfachtagung in Frankfurt (Oder)](https://www.kc85emu.de/scans/fa0189/Tagung.htm) vorgestellt und für städtebauliche Visualisierungen u.a. im Büro für Stadtplanung beim Rat der Stadt Frankfurt (Oder) verwendet.

Aus der Erinnerung von Andreas Thierbach:

*"Als Student der Fachrichtung Städtebau an der Hochschule für Architektur und Bauwesen (HAB) Weimar war ich von den Möglichkeiten der Computergrafik fasziniert. Den Einstieg fand ich mit den ersten KCs im Computerclub der Hochschule in der Programmiersprache Basic. Nebenan im Rechenzentrum wurden noch Programme der Studenten in Lochkarten gestanzt. Nachdem ich dann als Assistent an der HAB einen eigenen KC 85 erwerben konnte, war dem nächtlichen "Experimentieren" keine Grenzen mehr gesetzt. Mit den ersten selbst gesteuerten "schnellen" Linien auf dem kleinen Schwarz-Weiß-Fernseher war mein Ehrgeiz entfacht."*

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

# Funktionskatalog

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;">

<b><ins>Hauptmenü:</ins>

PERS   SEQU   HELP   KOIN   RDAT   FPIX   COLO   &gt;L/S
WAHL   AUGE   BILD   NPIX   DEFE   ELIN   MANI   GRAF
-&gt;

<b><ins>Die Nebenfunktionen:</ins></b></b>

<b>-&gt; RDAT:</b> Initialisieren oder Schalten der 32k-Speicherebenen
         zur 3D-Bearbeitung oder zur Darstellung;
<b>-&gt; FPIX:</b> Einstellung Pixelfenster-Begrenzung für 3D- und 2D-
         Darstellungen: links, rechts, oben, unten, Rand ?
<b>-&gt; COLO:</b> Einstellung Linien- und Hintergrundfarben für Darstel-
         lungen und Menüs: normal-, hochauflösend; ink, paper ?
<b>-&gt; &gt;L/S:</b> Datei laden / retten:

   <b>-&gt; DISK:</b> Diskettenbetriebsart
   <b>-&gt; TAPE:</b> Kassettenbetriebsart
   <b>-&gt; GDIR:</b> Anzeige des aktuellen Directories
   <b>-&gt; LOAD:</b> Datei von Kassette/Diskette laden
   <b>-&gt; ADDL:</b> Verknüpfen von Dateien
   <b>-&gt; EXLD:</b> Laden von Nutzer-MC-Unterprogrammen und Integration
   <b>-&gt; SAVE:</b> Datei auf Kassette/Diskette retten
   <b>-&gt; CAVE:</b> individuelles 3D-Grafik-System retten
   <b>-&gt; USER:</b> Start des USER-MC-Unterprogrammes
   <b>-&gt; FREE:</b> Anzeige verfügbarer Punkte   

<b><b><ins>Die Unterfunktionen:</ins></b></b>

<b>-&gt; WAHL:</b> Wahl der Darstellungsart:

   <b>-&gt; NORM:</b> normale Perspektive (auch im Objekt):  Focus ?
   <b>-&gt; TOTA:</b> totale Perspektive
   <b>-&gt; PARA:</b> Parallelprojektion

<b>-&gt; AUGE:</b> Einstellung Augpunktkoordinaten:
         XYZ-Augpunkt, XYZ-Differenz
<b>-&gt; BILD:</b> Einstellung Bildpunktkoordinaten:
         XYZ-Bildpunkt, XYZ-Differenz
<b>-&gt; NPIX:</b> Wahl des aktuellen Punkte- oder Elementebereiches:

   <b>-&gt; ALL :</b> Alle Elemente
   <b>-&gt; PIXL:</b> Punktebereich: Ab-Nr., Anzahl ?
   <b>-&gt; ELMT:</b> Elementebereich:  Ab-Nr., Anzahl ?
   <b>-&gt; BRK :</b> bleibt

<b>-&gt; DEFE:</b> Elementedefinition eines Punktebereiches (analog NPIX)

   <b>-&gt; E-&gt;P:</b> Elemente -&gt; Punktanzeige

<b>-&gt; ELIN:</b> Enementeeingabe:

   <b>-&gt; COR:</b>  Korrektur (Manipulation)
   <b>-&gt; ADD:</b>  Addition einer Kopie
   <b>-&gt; INS:</b>  Einfügen einer Kopie: KOPIE-AB-NR.:?
   <b>-&gt; DEL:</b>  Löschen von Punkten oder Elementen

<b>-&gt; MANI:</b> Manipulation:

   <b>-&gt; TRAN:</b> Verschiebung: XYZ ? (analog Bewegungsmanipunation)
   <b>-&gt; POSI:</b> Positionieren mittels Fadenkreuz
   <b>-&gt; MIRR:</b> Spiegelung: Richtung XYZ -&gt;
   <b>-&gt; ROTA:</b> Drehung: Achsenrichtung XYZ -&gt;, Grad ?
   <b>-&gt; SCAL:</b> Maßvergrößerung, -verkleinerung, Maß ? ...
   <b>-&gt; EXPA:</b> Strecken, Stauchen: Richtung XYZ ?, +- -&gt;, Maß ? ...

<b>-&gt; GRAF:</b> Grafikeditor:

   <b>-&gt; LINE:</b> Zeichnen Polygonlinie (Gummifuktion), Stift- oder
            Radierfunktion zuschaltbar;
   <b>-&gt; QUAD:</b> Zeichnen beliebiges Rechteck (Gummifunktion);
   <b>-&gt; CIRC:</b> Zeichnen Kreis (Gummifunktion);
   <b>-&gt; PERS:</b> 3D-Darstellung ohne Bildschirmlöschen;
   <b>-&gt; FILL:</b> Flächenfüllen in 45 Grad Schraffur;
   <b>-&gt; DELT:</b> Löschen zusammenhängender Pixelstrukturen;
   <b>-&gt; RESS:</b> Umschalten der Grafikauflösung, Überblicksdarstel-
            lung der Großgrafik, Schirm- oder Grafiklöschen;
   <b>-&gt; WIND:</b> Zeichnen des Bildschirm- oder Fensterrandes;
   <b>-&gt; INVR:</b> Inverse Grafikdarstellung;
   <b>-&gt; TEXT:</b> Texteingabe;
   <b>-&gt; HCOP:</b> Hardcopyinitialisierung (Normal, Farb- oder Hochauf-
            lösung) und -aufruf;
   <b>-&gt; &gt;L/S:</b> Kass./Disk.-Speicherung von Pixelgrafiken;
   <b>-&gt; BIND:</b> Logische Verknüpfung von Bild- oder Farbebenen;
   <b>-&gt; MOVE:</b> Bewegen von Bildschirm- oder Ausschnittsanzeige von
            Großgrafiken je nach RESS-Einstellung;


<b><b><ins>Die Hauptfunktionen:</ins></b></b>

<b>-&gt; PERS:</b> Perspektivmodus: perspektivische Darstellung,
         geradlinige Bewegungssequenzen,
<b>-&gt; SEQU:</b> Programmieren von Sequenzen, Weg mit LGEN
<b>-&gt; HELP:</b> Hilfsfunktionen, Generierungsmodus:
         HELP-Menü:

   <b>WAHL   AUGE   BILD   NPIX   DEFE   ELIN   MANI   GRAF
   XYZ3   Plan   Such   R1:1   Corp   Find   BGen   Keys  -&gt;</b>

   <b>-&gt; WAHL:</b> Wahl eines XY-Koordinatenausschnittes
            Bildeingabe mittels Fadenkreuz und Gummifenster
   <b>-&gt; 0,+,-:</b> Auschnittmanipulationen
   <b>-&gt; =   :</b> Gleichsetzen der Ausschnittgrenzen der 3 Ebenen
   <b>-&gt; XYZ3:</b> Ebenenwahl oder alle 3 Ebenen darstellen
   <b>-&gt; PLAN:</b> erneute Darstellung der Ebene und des Ausschnittes;
   <b>-&gt; SUCH:</b> Suchen eines Punktebereiches und Darstellung:
            (Definition mit NPIX);
   <b>-&gt; R1:1:</b> Darstellung im Verhältnis 1:1 (Fadenkreuz)
   <b>-&gt; AUGE, BILD:</b> Aug- u. Bildpunkteinstellung mittels Faden-
            kreuz;
   <b>-&gt; NPIX, DEFE, ELIN, MANI:</b> siehe &quot;Die Unterfunktionen&quot;!
   <b>-&gt; CORP:</b> Korrektur von Punktkoordinaten mit Fadenkreuz, 
            (Bereichsdefinition mit NPIX);
   <b>-&gt; FIND:</b> Finden (Anzeige) der Elementenummern;

   <b>-&gt; LGEN:</b> grafische Elementegenerierung

      <b>-&gt; GON:</b>  Polygon fortsetzen
      <b>-&gt; ARC:</b>  Bogenzug: Mittelpunkt, Gradschritte
      <b>-&gt; BRK:</b>  Abbruch mit Schließen des Polygons
      <b>-&gt; OPN:</b>  Abbruch ohne Schließen,

      <b>-&gt; PYRA:</b>  pyramidenförmiger Körper;
      <b>-&gt; QUAD:</b>  prismatischer Körper;       sonst Fläche;
      
<b>-&gt; KOIN:</b> Koordinateneingabe, direkte Werteingabe für Punkte
         und Linienverbindungen;

   <b>-&gt; COR:</b>  Korrektur: Eingabe analog NPIX;

      <b>-&gt; KOOR:</b> Koordinatenkorrektur: XYZ ant, neu ?
      <b>-&gt; VERB:</b> Verbindungslinienkorrektur: Anzahl, Pkt.-Nr.,
               alt, neu ?

   <b>-&gt; ADD:</b>  Addition von Punktekopien: Anzahl ?
   <b>-&gt; INS:</b>  Einfügen von Punktekopien: analog NPIX;
   <b>-&gt; DEL:</b>  Löschen von Punkten und Elementen;

</ins></b></b></pre>

# Handbuch

- [Handbuch (MD, deutsch)](/Dokumentation/Handbuch_03-1990.md)
- [Handbuch (Wordstar, deutsch)](/Dokumentation/Handbuch_03-1990.txt)

# Bedienkonzept

*   **Menütechnik:** Funktionen werden direkt über den Anfangsbuchstaben des jeweiligen Befehls aufgerufen (z. B. "P" für PERS).
*   **Fadenkreuztechnik:** Anwahl von Koordinaten mittels Fadenkreuz direkt auf dem Bildschirm, gesteuert durch Cursortasten.

# Entwicklungssystem
Das Original-Entwicklungssystem von Andreas Thierbach.

![](/Bilder/KC-50.jpg)

# Emulator
## Einstellungen
Das Programm kann im [JKCEMU](http://www.jens-mueller.org/jkcemu/) mit folgenden Einstellungen emuliert werden:

![](/Bilder/JKCEMU-1.PNG)

![](/Bilder/JKCEMU-2.PNG)

![](/Bilder/JKCEMU-3-75.PNG)

![](/Bilder/DISK2.png)

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

Nachdem die Daten fertig geladen wurden:

Taste "P"
```

# Lizenz

Der Autor hat das Programm zur Veröffentlichung für Demonstrationen im Kontext historischer Computertechnik auf GitHub freigegeben. Alle Rechte liegen beim Autor Andreas Thierbach. Kommerzielle Nutzung ist hiermit ausdrücklich untersagt. 

# Danksagung

Besonderer Dank geht an Andreas Thierbach für die Hilfe bei der Sichtung und Restaurierung der alten Datenbestände sowie an Peter Salomon, der durch seine Erinnerungen an die [5. Computerfachtagung in Frankfurt (Oder)](https://www.kc85emu.de/scans/fa0189/Tagung.htm) den Anstoß zu diesem Projekt gab.

# Quellen

Dieses Projekt nutzt Informationen und Software aus den u.g. Quellen:

https://www.mpm-kc85.de/html/D001BasisDevise.htm

https://www.mpm-kc85.de/html/D004FD.htm

https://www.mpm-kc85.de/html/m027_entwicklung.htm

http://www.jens-mueller.org/jkcemu/

http://kc85.info/






