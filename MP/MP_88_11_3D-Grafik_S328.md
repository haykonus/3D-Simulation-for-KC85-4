# 3-D-Simulation – interaktiver Entwurf von räumlichen Modellen

**Andreas Thierbach**
Büro für Stadtplanung beim Rat der Stadt Frankfurt (Oder)

Die Leistungsfähigkeit von Computern beweist sich immer mehr auch in der Anwendung für Systemmodellierungen, Simulationen oder Prozeßoptimierungen, dort, wo eine Vielzahl von Daten und Kriterien mit hoher Geschwindigkeit verknüpft, manipuliert oder bewertet werden muß. Von wachsendem Interesse ist dabei die Simulation der räumlichen Umwelt, sei es in der Grafik, der Malerei, im Design, in der Architektur oder in der Planung allgemein. Für diese Aufgaben finden aufgrund von wachsender Verbreitung, höherer Leistungsfähigkeit sowie verbesserter Software zunehmend auch Kleinrechner ihre Anwendung. **3-D-Simulation** ist ein bildschirmorientiertes Programm für Kleincomputer (KC 85) zur Unterstützung von Entwurfsprozessen, wozu die Modellierung geometrischer, formgestalterischer oder architektonischer Körper und Objekte, die Komposition flächiger oder räumlicher Strukturen, sowie eine räumlich-perspektivische Kontrolle und Korrektur gehören.

## Arbeitsprinzip

- Baukasten – Modellbau – Modellsimulation
- Erstellen von „Modellbausteinen" beliebiger Form („monolithisch" oder seriell), die auch weiterhin verformbar bleiben
- Arrangieren, Komponieren der Bausteine zum Modell
- Betrachten, Überprüfen und Verändern des Modells aus beliebiger Position (von außen, innen, aus der Bewegung; siehe Bildserie 1, 2. Umschlagseite).

## Modellbegriff

Unter Modell wird die Abstraktion von realen oder gedachten räumlichen Objekten oder Strukturen verstanden. Hier sind das digital gespeicherte Daten von Merkmalen, die zur Visualisierung des Modells notwendig sind. Das Kanten- und Drahtmodell (im Unterschied zum Flächen- und Volumenmodell) wird aus einem oder mehreren Elementen (hier auch als Bausteine oder Körper bezeichnet) zusammengesetzt. Jedes Element wird wiederum durch seine Eckpunkte, deren Lage im kartesischen Koordinatenraum sowie durch verbindende Linien (Kanten oder Strukturen) definiert. Durch Transformation der Punktkoordinaten auf eine Bildebene nach mathematischen Regeln der perspektivischen Darstellung und Ausgabe der Verbindungslinien auf Bildschirm, Plotter oder Drucker werden die digitalen Modelldaten als Bild sichtbar. Die Darstellung der Horizontlinie oder des Koordinatenkreuzes fixiert das Modell optisch im Raum.

Das Programm bietet aufgrund seiner kompakten Struktur, der Maschinenprogrammierung und der vollen Ausnutzung des Speichers ein umfassendes Funktionsangebot, hohe Rechen- und Darstellungsgeschwindigkeit sowie eine Verarbeitung vieler Daten bei einfacher Bedienung und hohem Komfort. Das Anwendungsspektrum könnte von der Einführung in den rechnergestützten Entwurf (CAD) bis zur direkten Nutzung für CAD reichen:

- Mathematik, Geometrie: 3-D-Visualisierung von Körpern
- Bildkünstlerische Ausbildung, Zeichenunterricht, Darstellungslehre, Entwerfen allgemein: Training des Raum-Körper-Vorstellungsvermögens, Vermittlung der Regeln der perspektivischen Darstellung, Überprüfen flächiger und räumlicher Kompositionen
- Formgestaltung, Architektur, Stadtplanung: Ausbildung und Praxis.

## Nutzung und Handhabung

- Generieren linearer, flächiger oder räumlicher Grundelemente durch Punktdateneingabe oder Zeichnen auf dem Bildschirm
- Vervielfältigen, Sortieren oder Löschen von Elementen, Elementeteilen oder Elementegruppen
- Manipulieren und Arrangieren dieser Elemente, d. h. Größen-, Form- und Lageveränderung durch Verschieben, Spiegeln, Drehen, Zerren, Stauchen, Vergrößern oder Verkleinern
- Anlegen von Elementekatalogen auf Kassette, die beliebig abrufbar und in zu bearbeitende Dateien einfügbar sind
- 4 Darstellungsarten:
    - normale Perspektive: Bildausschnitt wird je nach Betrachteraugpunkt, -zielpunkt und eingestellter Brennweite auf den Bildschirm transformiert
    - Der Augpunkt kann auch im Objekt liegen!
    - totale Perspektive: Angewählter Elementebereich wird im Darstellungsfenster vollständig und in maximaler Darstellungsgröße abgebildet
    - isometrische Darstellung: analog 2., jedoch Abbildung ohne perspektivische Verkürzung, so daß alle Ansichten und Isometrien (Axiometrien) möglich sind
    - Grundrißdarstellung (Draufsicht): automatisch im Hilfsmenü je nach Wahl des Bildausschnittes
    - Bewegungssequenzen: Hinein-, Hindurch-, Vorbeigehen, Überflug, Untersichten, Schwenken usw. (siehe Bildserie 2, 2. US)
- Manipulation oder Korrektur von Einzelkoordinaten, Elementen oder der Gesamtstruktur in allen Darstellungsarten (auch in der Perspektive), damit sofortige Kontrolle der räumlichen Auswirkung der Veränderung möglich
- Manipulation von Betrachteraug- und -zielpunkt sowie deren Bewegungsdifferenzen im Raum
- Kameratechnik: stufenlose Brennweitenwahl (Froschauge bis Superteleobjektiv – Zoom)
- Menütechnik: Anwahl aller Menüfunktionen durch Betätigen der Taste mit dem ersten Zeichen des Menüwortes
- Fadenkreuztechnik: Anwahl von Koordinaten mittels Fadenkreuz direkt auf dem Bildschirm, gesteuert durch Cursortasten.

**Hardware:** Kleinrechner KC 85/2 oder KC 85/3 mit oder ohne RAM-Expander
**Peripherie:** Monitor, Datenrecorder, Drucker, Plotter, Videotechnik
**Rechenzeiten:** bis zur fertigen 3-D-Darstellung
- einfache Objekte zirka 1–5 s
- komplexe Objekte zirka 5–15 s

**Daten – Dateien:** Der Datenspeicher wird vollautomatisch verwaltet und ist volldynamisch.

**Datenmenge (Raumpunktanzahl N):**
- 450–500 Punkte ohne RAM-Expander
- 1350–1500 Punkte mit RAM-Expander (16 KByte)

**Gesamtspeicherverbrauch:** N × 16 Byte
Alle Daten sind abruf- und manipulierbar.

## Die Hauptfunktionen

- PERS: Perspektivmodus, Bewegungssequenzen
- HELP: Hilfsfunktionen, Generierungsmodus
- WAHL: Wahl eines XY-Koordinatenausschnittes
    - +,-: Vergrößern, Verkleinern des Ausschnittes
- SUCH: Suchen eines Punktebereiches und Darstellung
- V1:1: Verhältnis 1:1-Darstellung eines Ausschnittes
- AUGE, ZIEL: Einstellung mittels Fadenkreuz
- NPIX, DEFE, ELIN, MANI: siehe Unterfunktionen
- CORP: Korrektur von Punktkoordinaten mit Fadenkreuz
- FIND: Finden (Anzeige) der Elementenummern
- GENE: Generierungshilfe für Elemente: Polygon- und Bogenfunktion, Flächen- und Körperdefinition
- KOIN: Koordinateneingabe
    - Korrigieren, Kopieren, Einfügen, Löschen von Punkten

## Die Unterfunktionen

- WAHL: Wahl der Darstellungsart
- AUGE: Einstellung Augpunktkoordinaten und -differenz
- ZIEL: Einstellung Zielpunktkoordinaten und -differenz
- NPIX: Wahl des aktuellen Punkte- oder Elementebereiches
- DEFE: Elementedefinition
- ELIN: Elementeeingabe: Korrigieren, Kopieren, Löschen
- MANI: Manipulation: Verschieben, Spiegeln, Drehen, Maßverändern, Zerren

## Die Nebenfunktionen

- FPIX: Einstellung Pixelfenster-Begrenzung
- COLO: Einstellung Linien- und Hintergrundfarben
- TAFU: Anzeige der wichtigsten Tastenfunktionen
- \> L/S: Datei laden, retten, verknüpfen, hardcopy

---
*Mikroprozessortechnik, Berlin 2 (1988) 11, S. 328*
