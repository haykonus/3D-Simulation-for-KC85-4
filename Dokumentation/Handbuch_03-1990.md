# Handbuch 03/1990 — 3D-Grafik und Simulation (KC85/4)

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;">

<b>_______________________________________________________________
I                                                             I
I                                                             I
I     3 D  -  G R A F I K   U N D   S I M U L A T I O N       I
I                                                             I
I_____________________________________________________________I
I                                                             I
I         A N W E N D E R D O K U M E N T A T I O N           I
I_____________________________________________________________I
I                                                             I
I                                                             I
I  RECHNERTYP:         KC-85/4                                I
I                                                             I
I  BETRIEBSART:        CAOS                                   I
I                                                             I
I  DATENTRÄGER:        Kassette/Diskette                      I
I                                                             I
I  BEARBEITUNGSSTAND:  März 1990                              I
I                                                             I
I_____________________________________________________________I
I                                                             I
I                                                             I
I  AUTOR: Dipl.-ing. Andreas Thierbach                        I
I         Stakerweg 2d, Frankfurt/Oder, 1200                  I
I         Diensttelefon: 365 306                              I
I                                                             I
I_____________________________________________________________I
I                                                             I 
I                                                             I 
I  <b><ins>Inhaltsverzeichnis:</ins></b>                               Seite    I
I                                                             I
I  0.         Einleitung                                 2    I
I  1.         Anwendungsgebiete                          3    I
I  2.         Nutzungsmerkmale                           3    I
I  3.         Handhabungsmerkmale                        4    I
I  4.         Technische Merkmale                        5    I
I  5.         Daten - Dateien                            5    I
I  6.         Laden - Programmstart                      5    I
I  7.         Programmbeschreibung                       6    I
I  7.1.       Das Hauptmenü                              6    I
I  7.2.       Die Nebenfunktionen                        6    I
I  7.3.       Die Unterfunktionen                        9    I
I  7.4.       Die Hauptfunktionen                       13    I
I  7.4.1.     Perspektivmodus                           13    I
I  7.4.2.     Generierungsmodus - Das HELP-Menü         14    I
I  7.4.3.     Koordinateneingabe                        18    I
I  7.4.4.     Grafikeditor                              19    I
I  8.         Zusammenfassung der Kommandos             22    I
I  9.         Symbole, Abkürzungen, Begriffe            24    I
I  10.        Fehlermeldungen                           24    I
I  11.        Literatur                                 25    I
I                                                             I
I_____________________________________________________________I</b>

                                      — 1 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;"><b><b><ins>0.  Einleitung:</ins></b></b>

Die Leistungsfähigkeit von Computern beweist sich immer mehr 
auch in der Anwendung für Systemmodellierungen, Simulationen oder
Prozeßoptimierungen, dort wo sehr viele Informationen mit hoher
Geschwindigkeit verknüpft, manipuliert oder bewertet werden müssen.

Von wachsendem Interesse ist dabei die Simulation der räumlichen
Umwelt, sei es in der Grafik, Malerei, im Design, der Architektur
oder in der Planung allgemein. Für diese Aufgaben finden aufgrund
von wachsender Verbreitung, höherer Speicherkapazität sowie ver-
besserter Software zunehmend auch Kleinrechner ihre Anwendung.

<b>&quot;3D-Grafik&quot;</b> ist ein bildschirmorientiertes Programm für KC-
Kleincomputer zur Unterstützung von Gestaltungs- und Entwurfs-
prozessen, wozu die

- Modellierung geometrischer, formgestalterischer oder architekto-
  nischer Körper und Objekte (rechnerinterne Modelle), die
- Komposition flächiger oder räumlicher Strukturen, eine
- zwei- oder dreidimensionale Darstellung,
- Bewegungssimulation sowie
- eine grafische Aufbereitung gehören.

Das vorliegende Programmsystem ist eine weiterentwickelte Ver-
sion von &quot;3D-Grafik u. Simulation&quot; (85/3) für KC85/4.

<b>Arbeitsprinzip:</b> Baukasten - Modellbau - Modellsimulation

- Erstellen und Vervielfältigen beliebiger &quot;Modellbausteine&quot;
  (Makros), die auch weiterhin verformbar bleiben,
- Arrangieren, Komponieren der Bausteine zum Modell,
- Betrachten, Überprüfen und Verändern des Modells aus beliebiger
  Position (von außen, innen, aus der Bewegung).

<b>Modellbegriff:</b>

Unter Modell wird die digitale Abstraktion von realen oder
gedachten räumlichen Objekten oder Strukturen verstanden.

Grundlage ist das Karthesische Koordinatensystem, welches
den Modellraum definiert.
   
<b>Das Kanten- oder Drahtmodell</b> (im Unterschied zum Flächen und
Volumenmodell) kann aus einem Element oder mehreren Elementen
(hier auch als Bausteine, Objekte oder Körper bezeichnet) be-
stehen.

Jedes <b>Element</b> wird wiederum durch seine <b>Eckpunkte</b>, deren
Lage im Koordinatenraum (XYZ-Koordinaten) sowie durch diese Punkte
<b>verbindende Linien</b> (Kanten) definiert.

Durch Transformation der Punktkoordinaten auf eine Bildebene
nach mathematischen Regeln der perspektivischen Darstellung
und Ausgabe der Verbindungslinien auf Bildschirm, Plotter oder
Drucker werden die digitalen Modelldaten sichtbar gemacht.

Die Darstellung der <b>Horizontlinie</b> oder des Koordinatenkreuzes
fixiert das Modell optisch im Raum.

                                   — 2 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;"><b><b><ins>1.  Anwendungsgebiete:</ins></b></b>

- Erstellen von 2D/3D-Illustrationen, Text- und Repräsentations-
  grafiken (bis Format A4);
- Mathematik, Geometrie: 3D-Visualisierung von Körpern;
- Bildkünstlerische Ausbildung: Training des Raum-Körper-
  Vorstellungsvermögens; Überprüfen und Manipulieren flächiger
  und räumlicher Kompositionen aller Art;
- Formgestaltung: Entwurf, Modellsimulation;
- CAD-Einführung, -Ausbildung und Nutzung fÜr CAD.


<b><b><ins>2.  Nutzungsmerkmale:</ins></b></b>

- Einfaches Generieren linearer, flächiger oder räumlicher Grund-
  elemente durch Zeichnen auf dem Schirm oder Punktdateneingabe;

- Einfaches Vervielfältigen, Sortieren oder Löschen von
  Elementen, Elementeteilen oder Elementegruppen;

- Einfaches Manipulieren und Arrangieren dieser Elemente:
  Größen-, Form- und Lageveränderung durch:  
             -Verschieben
             -Positionieren
             -Spiegeln
             -Drehen
             -Strecken, Stauchen
             -Vergrößern, Verkleinern;

- Speichern von Elementen auf Kassette/Diskette, die beliebig
  abrufbar und in zu bearbeitende Modelle einfügbar sind
  (Bibliotheken);

- Wahl von Grundriß-, Ansichten-, isometrischer oder perspekti-
  vischer Darstellung sowie Programmierung von Sequenzen;

- Wahlweise Abbildung von Elementegruppen, Einzelelementen oder
  Details (freie Ausschnittwahl);

- Korrektur oder Manipulation von Einzelkoordinaten, Elementen
  oder der Gesamtstruktur in allen Darstellungsarten (auch
  in der Perspektive); 

- Einfache Wahl und Manipulation von Betrachteraug- und -bild-
  punkt sowie von Bewegungen im Raum;

- Betrachterbewegungssequenzen wie Hinein-, Hindurch-, Vorbei-
  gehen, Überflug, Untersichten, Schwenke sowie freie Wege
  programmierbar;

- <b>Kameratechnik:</b>  freie Brennweitenwahl (Froschauge  bis
  Superteleobjektiv);

- Umfangreicher Grafikeditor und differenzierte Bildspeicher-
  und Hardcopyfunktionen;

- Verdeckte Kanten werden dargestellt. Eine Programmversion mit
  Algorithmus zur Unterdrückung der verdeckten Kanten ist in
  Arbeit.

                              — 3 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;"><b><b><ins>3.  Handhabungsmerkmale:</ins></b></b>

- <b>Menütechnik:</b> Anwahl aller Menüfunktionen (meist als Kür-
  zel angezeigt) durch Betätigen der Taste mit dem 1. Zeichen
  des Menüwortes oder Kürzels. Gekennzeichnet sind solche
  Menüs durch &quot;-&gt;&quot;;

- Direkte Werteingabe bei Menüwörtern, die durch ein Frage-
  zeichen abgeschlossen sind;
  - &gt;ENTER&lt; der Wert bleibt erhalten,
  - Neueingabe durch Überschreiben des angezeigten Wertes,
  - Eingabe von &gt;B&lt; und &gt;ENTER&lt; - Abbruch der Eingabefunktion

  Generell ganzzahlige dezimale Eingabe und Ausgabe (Anzeige),
  Wertebereich <b>von -32768 bis  32767;</b> (Auflösung, Raumkoor-
  dinaten, maximale Größen und Ausdehnungen liegen ebenfalls
  in diesem Bereich !)

- <b>Fadenkreuztechnik:</b> Anwahl von Koordinaten mittels Fadenkreuz
  direkt auf dem Bildschirm;

- <b>Gummibandfunktionen</b> für Linie, Rechteck und Kreis;

- beliebiges Bildschirmdarstellungsfenster (Windowing) sowie
  alle verfügbaren Vorder- und Hintergrundfarben einstellbar;

- einfache, nutzerorientierte Dateiarbeit und Ebenentechnik.

- <b>4 Darstellungsarten:</b>

  <b>1.  normale  Perspektive:</b>  Bildausschnitt  wird  je  nach
  Betrachteraugpunkt, -zielpunkt und eingestellter Brennweite 
  auf den Bildschirm transformiert (Horizontdarstellung);
  Der Augpunkt kann hier auch im Objekt liegen ! 

  <b>2.  totale  Perspektive:</b>  angewählter Elementebereich wird
  im Darstellungsfenster vollständig und in maximaler Darstel-
  lungsgröße abgebildet (Horizontdarstellung);
  <b>Achtung:</b> hier darf der Augpunkt nicht im oder in unmittel-
  barer Nähe des Objektes liegen, d.h. die Bildebene darf das
  Objekt nicht schneiden, sonst fehlerhafte Darstellung !

  <b>3.  Parallelprojektion:</b> analog 2. jedoch Abbildung
  ohne perspektivische Verkürzung, sodaß alle Ansichten und
  Isometrien (Axiometrien) möglich sind;

  <b>4.  Drauf- und Ansichten:</b> automatisch im Hilfsmenü je
  nach Wahl der Koordinatenebene und des Bildausschnittes;
  Achsenanzeige sowie Grobbemaßung des Ausschnittes möglich.

  Alle 2D-/3D-Transformationen sind vektororientiert. Das gene-
  rierte Bild kann jederzeit gelöscht und neu aufgebaut werden.
  Die gespeicherte Modellgeometrie bleibt dabei erhalten.

  Alle erzeugten 2D- und 3D-Darstellungen lassen sich mit dem
  pixelorientierten Grafikeditor aufbereiten oder verfeinern.

                                  — 4 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;"><b><b><ins>4.  Technische Merkmale:</ins></b></b>

<b>Hardware:</b>     KC 85/4, M022 (16k), V24-Schnittstelle,
              M011 (64k) für Ebenentechnik u. hochauflösende Grafik

<b>Peripherie:</b>   Tastatur, Monitor, (Grafikdrucker),
              Datenrecorder und/oder D004 KC-Floppy-System;

<b>Erweiterung:</b>  Plotter, Videotechnik

<b>Rechenzeiten:</b> bis zur fertigen 3-D-Darstellung
              einfache Objekte ca. <b>1 - 5 sec.</b>
              komplexe Objekte ca. <b>5 -25 sec.</b>


<b><b><ins>5.  Daten - Dateien:</ins></b></b>

N = Anzahl der gespeicherten Raumpunkte

<b>Gesamtspeicherverbrauch:</b> ca. N * 16 Byte 

Der Datenspeicher wird vollautomatisch verwaltet und ist
volldynamisch. Die Datenblöcke beanspruchen immer den minimal
notwendigen Speicherraum.

Warnungen bei Speicherüberlauf werden angezeigt (je nach
Speichererweiterungsmodul).

<b>Datenmenge (Raumpunktanzahl):</b>

  450 -   500  Punkte ohne RAM-Expander          (nur KC 85/3)
1 400 - 1 500  Punkte mit 16 KByte-Expander      (nur KC 85/3)
2 000 - 2 100  Punkte ROM-Version, 64 KByte-Expander (KC 85/3)
                                   16 KByte-Expander (KC 85/4)
4 200 -16 300  Punkte und hochauflösende Grafikbearbeitung,
               parallele Programmierung, bzw. Textverarbeitung;
               Ebenentechnik:
               3 Ebenen bei 16 und 64 KByte-Expander    
               9 Ebenen bei 16 und 256 KByte-Exp.    (KC 85/4)  

Alle Daten sind abruf- und manipulierbar.


<b><b><ins>6.  Laden - Programmstart:</ins></b></b>

Das Programm &quot;3D-Grafik&quot; wird im der Kassettenversion mit %LOAD,
in der Diskettenversion in der CAOS-Betriebsart mit %FLOAD in
den Rechner geladen.
Ein 16k-RAM-Expander M011 muß im Schacht 8 des Grundgerätes
stecken ! In der Kassettenversion ist dieser vor dem Laden mit
%SWITCH  8  C3  zu schalten.
Nach Abschluß des Ladevorganges <b>startet</b> das Programm <b>selbst</b> .

Nach dem Selbststart wird das Titelbild des Programms aufge-
baut. Die 3D-Datei des Titelbildes ist voll im Speicher abgelegt
und kann (eventuell nur während der Einarbeitungsphase) weiter
genutzt oder gelöscht werden (siehe DELete in ELIN).

Das Bild bleibt ca. 3 sec. stehen, dann erscheint die
Hauptmenüleiste. 

                                   — 5 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;"><b><b><ins>7.   Programmbeschreibung:</ins></b></b>
 
<b><b><ins>7.1.  Das Hauptmenü:</ins></b>

PERS   SEQU   HELP   KOIN   RDAT   FPIX   COLO   &gt;L/S
WAHL   AUGE   BILD   NPIX   DEFE   ELIN   MANI   GRAF
-&gt;</b>

Die Menüfunktionen werden durch Eingabe des 1. Buchstabens
oder Zeichens des Menükürzels angewählt. Das Zeichen <b>&quot; -&gt; &quot;</b>
erwartet nur <b>einen</b> Tastendruck. In dieser Funktionsbeschrei-
bung wird der Buchstabe der zu betätigenden Taste immer dem
Menüwort vorangestellt. Beispiel: <b>-&gt; P PERS:</b> 
In allen übergeordneten Menüs führt die Betätigung der Taste
&gt;ENTER&lt; zur Anzeige des Vollbildes, das Menü verschwindet dann
bis zu einem erneuten Tastendruck (PULLDOWNMENU).

Das Hauptmenü ist gegliedert in die

<b>- Hauptfunktionen:</b>  PERS   SEQU   HELP   KOIN

<b>- Nebenfunktionen:</b>  RDAT   FPIX   COLO   &gt;L/S

<b>- Unterfunktionen:</b>  WAHL   AUGE   BILD   NPIX
                    DEFE   ELIN   MANI   GRAF


<b><b><ins>7.2.  Die Nebenfunktionen:</ins></b></b>

   beeinflussen Dateiaktivierung, Bildschirmlayout, Kassetten-
   speicherarbeit. Nach dem Programmstart sind diese Funktionen
   standartinitialisiert und benötigen keine Veränderung. Der
   Neueinsteiger sollte sie deshalb vorerst nur informatorisch
   abhandeln.

<b>-&gt; R RDAT:</b> Aktivieren und Schalten der RAM-DATEIEN (-EBENEN)
   Nur bei Einsatz von 64k- oder 256k-RAM-Expandern möglich !
   Die Erweiterungen sind <b>vor dem Einschalten</b> des KC zu stecken!

   Nach Drücken des Taste &gt;R&lt; erfolgt im Menüfenster die An-
   zeige der verwendbaren RAM-Ebenen und des neuen Menüs:

   <b>RAM-FILES:  3               (bei Einsatz 1 * M011)
   WORK  DRAW  -&gt;</b>

   <b>-&gt; W WORK:</b> Initialisierung oder Schaltung der Arbeitsebene

   Nach Eingabe &gt;W&lt; erfolgt die Anzeige der Nummer der aktuellen
   (bearbeitbaren) Ebene:

   <b>WORKFILE:? 1</b>

   <b>Achtung:</b> nach Laden und Start des Programmes 3D-Grafik ist
   immer die Ebene 1 initialisiert und aktiviert. Stehen keine
   64- oder 256k-RAM-Erweiterungen zur Verfügung, wird generell
   nur in Ebene 1 gearbeitet und es bedarf keiner Ebenenschaltung!

   &quot;?&quot; erfordert eine numerisch Eingabe und &gt;ENTER&lt;, soll die
   angezeiget Zahl erhalten werden, dann nur &gt;ENTER&lt;.

                                     — 6 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;">   Jetzt erfolgt die Anzeige der momentanen Nutzungsart der ange-
   wählten Ebene: <b>P</b> für 3D-Koordinatendatei
                  <b>G</b> für Grafikdatei (hochauflösend)
                  <b>kein Buchstabe</b> für unbenutzte Ebene.

   <b>SWIT  INIT  -&gt;</b>

   <b>-&gt; S SWIT:</b> Schalten/Aktualisieren einer schon initiali-
   sierten Ebene. Falls die zu schaltende Ebene noch nicht
   initialisiert ist, erfolgt die Anzeige: <b>FALSE BASE! -&gt;</b>
   (falsche oder keine Gundinitialisierung) und nach Tastendruck
   wird erneut die Eingabe <b>WORKFILE:?</b> gefordert.

   <b>-&gt; I INIT:</b> Initialisieren einer 32k-Speicherebene für
   die 3D-Arbeit, Menü:

   <b>BASE  SYST  -&gt;</b>

   <b>-&gt; B BASE:</b> Grundinitialisierung (P) der Ebene für 3D-Arbeit,
   dabei wird der Speicher gelöscht und es müssen 3D-Elemente neu
   generiert oder von Kassette geladen werden. Ist keine 3D-Infor-
   mation im Speicher (Anzahl der Raumpunkte = 0), erfolgt auch keine
   3D-Darstellung im Hauptmenü bei Aufruf der Perspektive mit &gt;P&lt;!

   <b>-&gt; S SYST:</b> Initialisierung der angewählten Arbeitsebene mit
   den Systemdaten der vorher aktuellen Ebene, wie Aug- und Bild-
   punktkoordinaten, Darstellungsart, Brennweite, Farben, Fenster,
   Koordinatenebenen usw. Die vorhandenen 3D-Raumpunktdaten der
   angewählten Ebene bleiben dabei erhalten! Ist die Ebene jedoch
   nicht grundinitialisiert, erfolgt wiederum die Ausschrift
   <b>FALSE BASE! -&gt;</b> .

   <b>-&gt; D DRAW:</b> Eingabe der Anzahl der im Perspektivmodus gleich-
           zeitig darzustellenden Ebenen:

   <b>DRAWFILES:? 1</b>

   die Arbeitsebene wird dann immer zuerst dargestellt, bleibt aber
   für die Bearbeitung (Generierung, Manipulationen usw.) aktuell.

<b>-&gt; F FPIX:</b> Einstellung PIXELFENSTER-BEGRENZUNG:

   Das Bildschirmdarstellungsfenster wird durch Linien begrenzt. 
   Alle Darstellungen werden in dieses Fenster transfor-
   miert und sind durch dieses Fenster (+- eingestellter 
   Rand) begrenzt.
   Plazierung und Größe des Fensters sind frei einstellbar. Menü:

   <b>DIN   NEW   HM3  -&gt;</b>

   <b>-&gt; D DIN:</b> Standartfenster wird automatisch eingestellt
   Im Perspektivmodus erfolgt dann eine Aug- u. Bildpunktkoordi-
   natenanzeige.

   <b>-&gt; N NEW:</b> Neueingabe der Fenstergrenzen

   LINKS? 0            RECHTS? 319
   UNTEN? 0              OBEN? 255         RAND? 10

                                  — 7 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;">   &quot;RAND&quot; ist der Abstand von der maximalen Objektdarstellung
   zur Fenstergrenze (nur für totale und isometrische Dar-
   stellung relevant).

   Der Cursor steht auf der &quot;0&quot; hinter &quot;LINKS?&quot;. Sollen die
   Werte beibehalten werden, jeweils nur &gt;ENTER&lt; eingeben, sonst
   numerische Eingabe und mit &gt;ENTER&lt; abzuschließen.

   <b>-&gt; H HM3:</b> Einstellung der Fenstergrenzen für die Darstel-
   lung aller drei Koordinatenebenen in der HELP-Menüfunktion
   &gt;3&lt;. Hier sollten die Standartwerte beibehalten werden, für
   speziele grafische Darstellungen sind sie jedoch variierbar.


<b>-&gt; C COLO:</b> Einstellung der Vordergrund-(Linien-, Zeichen-)
   und Hintergrundfarben. Menü:

   <b>HIGH  NORM  -&gt;</b>

   <b>-&gt; N NORM:</b> normale KC-Farbauflösung (16 Vorder-, 8 Hinter-
   grundfarben)
   Es können die Farben für die Zeichnungen (DRAWINGS),
                            das Haupsmenü   (MAINMENU) und
                            das Hilfsmenü   (HELPMENU)
   nacheinander eingestellt werden.

   <b>-&gt; H HIGH:</b> hochauflösende Farbdarstellung (3 Vorder-, 1
   Hintergrundfarbe)
   Die Einstellung erfolgt analog NORM. Es empfehlen sich hier
   aber die Vordergrund/Hintergrund-Kombinationen der Codes 31 / 7
   und 0 / 0 !

   Eintragen der Dezimalcodes für Farben siehe Beschreibung
   für KC 85/4, BASIC- oder Systemhandbuch!

<b>-&gt; &gt; &gt;L/S:</b> Laden, Retten, Verknüpfen von Dateien, Menü in der

   Kassettenversion:  <b>LOAD  ADDL  EXLD
                      SAVE  CAVE  USER  FREE  -&gt;</b>

   Diskettenversion:  <b>LOAD  ADDL  EXLD  DISK  GDIR
                      SAVE  CAVE  USER  TAPE  FREE  -&gt;</b>

   <b>-&gt; D DISK:</b> Alle Speicherfunktionen werden auf Disketten-
   arbeit umgeschaltet.

   <b>-&gt; T TAPE:</b> Umschalten auf Kassettenbetrieb.

   In der Diskettenbetiebsart erfolgt generell vor dem Saven
   oder Laden eine Aufforderung zur Namenseingabe. Hier sind
   immer Dateiname und -typ (durch Punkt getrennt) einzugeben !
   3D-Zeichnungsdateien sollten üblicherweise den Typ .DWG
   erhalten, um sie von Programm- oder Grafikdateien zu unter-
   scheiden (.KCC, .LGR oder .HGR).

   <b>-&gt; G GDIR:</b> Anzeige des aktuellen Directories der einge-
   legten Diskette,

                                     — 8 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;">   <b>-&gt; L LOAD:</b> 3D-Datei von Kassette/Diskette laden, alte
   Datei (falls vorhanden) wird dabei im Speicher gelöscht,

   <b>-&gt; A ADDL:</b> &quot;Additionsladen&quot;, die zu ladende 3D-Datei wird
   zur vorhandenen addiert und die Raumpunktdaten einsortiert,
   Nach Eingabe von &gt;A&lt; Bandwiedergabe starten !

   Achtung: Bei diesen Ladefunktionen werden BASIC- oder ASM-
   dateien ausgeschieden, fremde MC-Programme nicht ! Tasten-
   druck während des Ladens führt zu Fehlern !

   <b>-&gt; S SAVE:</b> 3D-Datei auf Kassette/Diskette retten,

   <b>NAME :</b> Name und Typ der Datei eintragen und &gt;ENTER&lt; drücken,
   (in der Kassettenversion vorher Bandaufnahme starten !)

   <b>-&gt; E EXLD:</b> Laden eines Nutzer MC-Programmes. Dieses muß
   ab Adresse DC00h beginnen und darf maximal 400h lang sein.
   Diese Nutzerroutine (z.B. Plottertreiber) wird dann automatisch
   in das 3D-System implementiert.

   <b>-&gt; U USER:</b> Ansprung des Nutzer-MC-Programmes

   <b>-&gt; C CAVE:</b> Abspeichern einer individuellen Nutzerkopie von
              &quot;3D-Grafik&quot;
   Die Urheberrechte des Autors sind zu wahren! Von der Nutzerkopie
   sind keine weiteren Kopien zu fertigen!
   
   <b>-&gt; F FREE:</b> die Anzahl der noch in der jeweilig aktuellen
   Speicherebene generierbaren Raumpunkte wird angezeigt.


<b><b><ins>7.3.  Die Unterfunktionen:</ins></b></b>

   bedienen direkt die 3D-Simulation sowie die Objekt-
   generierung und -manipulation (den Modellbau).

<b>-&gt; W WAHL:</b> Wahl der Darstellungsart

   <b>NORM   TOTA   PARA   -&gt;</b>

   <b>-&gt; N NORM:</b> normale Perspektive, der Augpunkt kann auch im
   Objekt liegen (Hindurchgehen möglich)

   <b>FOCUS ? ...</b>    Eingabe der Brennweite (analog Kamera):
                  &lt; 50      Weitwinkelobjektiv
                  50 bis 80 Normalobjektiv
                  &gt; 80      Teleobjektiv
                     
   <b>-&gt; T TOTA:</b> totale Perspektive, der Augpunkt darf nicht im
   Objekt liegen bzw. die Bildebene darf das Objekt nicht
   schneiden, sonst Fehldarstellung. 
   Unabhängig vom Abstand Betrachter - Objekt wird die Darstellung
   in maximaler Größe in das Fenster transformiert.

   <b>-&gt; P PARA:</b> Parallelprojektion, alle parallelen Modell-
   kanten werden auch parallel dargestellt, sonst analog TOTA;

   Aufruf der gewählten Darstellungsart aus dem Hauptmenü mit PERS.

                                     — 9 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;"><b>-&gt; A AUGE:</b>   AUGE:    X? ...   Y? ...   Z? ...
             DIFF:    X? ...   Y? ...   Z? ...

   Eingabe der Augpunktkoordinaten sowie der Schrittweiten
   (Differenzen), um die der Augpunkt bei geradliniger Bewegungs-
   simulation in X, Y oder Z-Richtung verändern werden soll.

<b>-&gt; B BILD:</b>  BILD:    X? ...   Y? ...   Z? ...
            DIFF:    X? ...   Y? ...   Z? ...

   analog AUGE;

<b>-&gt; N NPIX:</b>  PIXL   ELMT   ALL  -&gt;

   Funktion zur Wahl der Punkte- oder Elementeanzahl, die zur
   Bearbeitung aktiviert (aktuell auf dem Bildschirm dargestellt,
   korrigiert, angezeigt usw.) werden soll:

   <b>-&gt; BRK   :</b> alte Einstellung bleibt; Rücksprung in&#x27;s Menü
   <b>-&gt; P PIXL:</b> Anwahl der Raumpunkteingabe
   <b>-&gt; E ELMT:</b> Anwahl der Elementeingabe
   <b>-&gt; A ALL :</b> alle Elemente werden automatisch aktiviert

   Die Gesamtzahl der bereits abgespeicherten Raumpunkte oder
   Elemente wird jeweils angezeigt: 

   <b>EXIST: ...  PUNKTE (oder ELEMENTE) !
   AB-NR. ? 0
   ANZAHL ? 0</b>

   Eingeben, <b>ab</b> welcher Punkte- bzw. Elementenummer <b>wieviel</b>
   Punkte oder Elemente aktiviert werden sollen.


<b>-&gt; D DEFE:</b>   DEFE   E-&gt;P   -&gt;

   <b>-&gt; D DEFE:</b> DEF ELEMENT
   Elementedefinition:  eine Anzahl Punkte oder Elemente kann als
   neues Element zusammengefaßt (definiert) oder ein Element kann
   in Teilelemente zerlegt werden,
   Anzeige und Eingabe analog NPIX ! 
   Achtung: wichtig nach KOIN - ADD oder INS !

   <b>-&gt; E E-&gt;P:</b> DEF ELEMENT
   Elemente-Punktanzeige: für die angewählte Anzahl Elemente
   werden die erste Punktnummer sowie die Anzahl der enthaltenen
   Punkte angezeigt (wichtig für Korrekturen oder Manipulationen),
   Eingabe analog NPIX !    Anzeige: <b>AB-PIX: ...
                                     ANZAHL: ...  -&gt;</b>
 
  zurück in&#x27;s Menü mit &gt;BRK&lt; oder &gt;ENTER&lt;

<b>-&gt; E ELIN:</b> Elementeeingabe (Korrigieren, Kopieren, Ein-
   sortieren, Löschen von Elementen), 

   <b>DEF ELEMENT</b> Anzeige und Definition des zu bearbeitenden
   Punkte- oder Elementebereiches analog NPIX ! Dann Menü:

   <b>COR   ADD   INS   DEL   -&gt;</b>

                                  — 10 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;">   <b>-&gt; C COR:</b> Korrektur: Sprung in&#x27;s Manipulationsprogramm
   (siehe MANI)

   <b>-&gt; A ADD:</b> Addition: Kopieren des definierten Bereiches
   und Addition zum vorhandenen Speicher,
   Nach der Eingabe von &gt;A&lt; liegt die Kopie am Ende der Datei
   und ist deckungsgleich zum Original. Sie kann jetzt noch
   in ihrer Größe, Form oder Raumlage manipuliert werden.

   <b>-&gt; I INS:</b> Insert/Einfügen: Kopieren des definierten Be-
   reiches und Einsortieren in die Datei an gewünschter Stelle.

   KOPIE-AB-NR.: ?

   Eingabe der Elementenummer <b>an deren Stelle</b> in der Ele-
   mentereihenfolge die Kopie eingefügt werden soll.
   <b>Achtung:</b> damit erhöhen sich die Nummern der nachfolgen-
   den Elemente um die Anzahl der gedoppelten und eingefüg-
   ten Elemente !

   Nach dem Einfügen erfolgt wie nach ADD der Sprung in das
   Manipulationsmenü.

   <b>-&gt; D DEL:</b> delete/Löschen: Der definierte Punkte- oder Ele-
   mentebereich wird aus der Datei gestrichen, die verbleiben-
   den Daten werden zusammengerückt.
   <b>Achtung:</b> damit verringern sich die Nummern der nachfolgenden
   Elemente um die Anzahl der gelöschten Elemente !
   Die gelöschten Elemente fehlen erst bei erneuter Darstellung.

<b>-&gt; M MANI:</b> Manipulation eines Elemente- oder Punktebereiches:

   <b>DEF ELEMENT</b> Anzeige und Definition des Bereiches analog NPIX !

   Manipulationsmenü:
   <b>TRAN   POSI   MIRR   ROTA   SCAL   EXPA   -&gt;</b>

   <b>-&gt; T TRAN:</b> Translation, Verschieben

   <b>DIFF</b>    X? ...      Y? ...      Z? ...
   
   Nach Eingabe der Differenzen wird die definierten Elemente im
   Koordinatenraum verschoben und in ihrer neuen Position auf dem
   Bildschirm dargestellt.

   <b>BRK   ENTER  -&gt;</b>

   Bei Eingabe von &gt;ENTER&lt; wird der Bereich erneut um die ein-
   gegebenen Werte verschoben, die alte Position auf dem Bild-
   schirm wird gelöscht, die neue Position dargestellt.
   &gt;BRK&lt; : zurück in&#x27;s Manipulationsmenü.

   <b>-&gt; P POSI:</b> Positionierung:

   Das Fadenkreuz (siehe: Das tastaturgesteuerte Fadenkreuz !)
   wird in die Mitte des Elements gesetzt und kann nun neu
   positioniert werden. Nach Eingabe &gt;ENTER&lt; wird das Element
   an die gewünschte Stelle plaziert.

                                 — 11 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;">   <b>-&gt; M MIRR:</b> Mirror, Spiegeln

   <b>SPIEGELRICHTUNG  X Y Z  -&gt;</b>
   Wahl der Koordinatenrichtung, in die gespiegelt werden soll:

   Wahl der Position der Spiegelungsachse mittels Fadenkreuz, das
   auch hier in die Mitte des Elements gesetzt wird.

   Bei Eingabe von &gt;ENTER&lt; wird der Punkte- oder Elementebe-
   reich in der festgelegten  Richtung  gespiegelt. Wird das
   Kreuz nicht bewegt, erfolgt die Spiegelung auf der Stelle.
      
   &gt;BRK&lt; : zurück in&#x27;s Manipulationsmenü.

   <b>-&gt; R ROTA:</b> Rotation, Drehen

   <b>ACHSRICHTUNG  X Y Z  -&gt;</b>
   Wahl der Koordinatenrichtung der Drehachse, um die gedreht
   werden soll,

   Wahl der Position der Drehachse mittels Fadenkreuz analog
   Spiegelung.

   <b>GRAD ?</b>
   Eingabe der Drehgradzahl: positiv - Drehung im Uhrzeiger-
                                       sinn   
                             negativ - Drehung im negativen
                                       Uhrzeigersinn
 
   <b>Achtung:</b> bei häufigem fortlaufenden Drehen entsteht ein
   Genauigkeitsverlust (Berechnungsverlust durch ganzzahliges
   Abspeichern der Koordinatenwerte) ! Empfehlenswert ist, vor-
   her eine Elementekopie anzulegen !   

   <b>-&gt; S SCAL:</b> Scalation, Vergrößern, Verkleinern

   <b>MASS? ...</b>
   Die alte Ausdehnung in Z-Richtung wird angezeigt,
   das gewünschte neue Maß kann eingegeben werden.
   Das Objekt wird in allen Maßen proportional vergrößert
   oder verkleinert. (Nicht bei Linien oder Flächen anwenden!)

   <b>-&gt; E EXPA:</b> Expansion, Strecken, Stauchen

   <b>STRECKRICHTUNG  X Y Z  -&gt;</b>
   Wahl der Koordinatenrichtung, in die das Objekt gestreckt,
   bzw. gestaucht werden soll,

   <b>+  -  -&gt;</b>
   Eingabe von &gt;+&lt;: Sreckung in positive Achsenrichtung
               &gt;-&lt;: Sreckung in negative Achsenrichtung

   <b>MASS? ...</b>
   Die alte Ausdehnung in der jeweils vorher gewählten 
   Koordinatenrichtung wird angezeigt, der neue Wert kann
   eingegeben werden, das Objekt wird in die angegebene
   Richtung gezerrt.
   Ist der neue Wert größer als der alte, wird gestreckt;
   ist er kleiner, wird gestaucht.

                              — 12 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;">Aus den Manipulationsfunktionen wird jeweils in das Manipu-
lationsmenü zurückgesprungen, sodaß auch Kombinationen von
Manipulationen zum jeweiligen Objekt möglich sind.

Alle Manipulationen werden auf dem Bildschirm in der jeweils
gewählten Darstellungsart (NORM, TOTA, PARA, HELP) angezeigt.
Es ist also auch möglich, im Perspektivmodus zu manipulieren,
damit sofort die räumliche Auswirkung der Veränderung zu
prüfen und gegebenenfalls erneut zu korrigieren.


<b><b><ins>7.4.   Die Hauptfunktionen:</ins></b>

<b><ins>7.4.1. Perspektivmodus:</ins></b>

      -&gt; P PERS:</b>

Nach Eingabe von &gt;P&lt; wird der angewählte Punkte- oder Ele-
mentebereich (je nach Einstellung der Neben- und Unterfunk-
tionen) auf dem Bildschirm dreidimensional dargestellt.

Am oberen Bildrand werden (bei OBEN &lt; 243) die aktuellen XYZ-
Koordinaten des Aug- und Bildpunktes angezeigt (z.B.: DIN-Fenster):

<b>A:  ...  ...  ...    B:  ...  ...  ...</b>

Das Programm befindet sich jetzt im Bewegungsmodus, dessen
Menü aber aus Layoutgründen nicht vollständig angezeigt wird.

<b>Tastenfunktionen im Bewegungsmodus:</b>

<b>-&gt; ENTER:</b>  nächstes Bild (je nach Einstelnung der Aug- und
           Bildpunktdifferenzen ändert sich die Perspektive);
<b>-&gt; BRK:</b>    zurück in&#x27;s Hauptmenü;
<b>-&gt; S:</b>      geradlinige Sequenz je nach Aug- und Bildpunkt-
           differenzeinstellung (nur mit &gt;BRK&lt; zu unterbrechen)

Differenzmanipulation im Bewegungsmodus: 

<b>-&gt; A,B:</b>    Anwahl Aug- oder Bildpunkt, dann Anzeige:
<b>DIFF   X? ...    Y? ...    X? ...</b>  und Eingabe möglich

<b>-&gt; M MOVE:</b> Bildverschiebung für aktuelle Darstellung,
           (nur in NORM !)
<b>MOVE   X? ...    Y? ...</b> 

Das angezeigte Bild wird einmalig um die eingegebenen Pixelwerte
verschoben.

      <b>-&gt; S SEQU:</b> Initialisieren und Starten <b>programmierter</b> Sequenzen

<b>AWAY   BWAY   LINE  -&gt;</b>
Festlegen, ob Augpunkt, Bildpunkt oder beide dem vorher mit LGEN
(siehe 7.4.2.) programmierten Polygonzug (Weg) folgen.
Das letzte Element wird in SEQU immer automatisch als Weg benutzt
und kann für die Darstellung ausgeblendet werden: vorher mit NPIX
den richtigen Elementebereich aktivieren. 

                                       — 13 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;">Ist der Augpunkt als Weg programmiert (AWAY), sollte der Bildpunkt 
vor Anwahl von SEQU richtig eingestellt werden, ansonsten bleibt
die letzte Einstellung dafür aktuell ! (Analog  für BWAY)

Nach Abbruch von SEQU (nur mit &gt;BRK&lt; während des Bildaufbaus) 
sind AUGE und BILD gegebenenfalls neu einzustellen. 


<b><b><ins>7.4.2. Generierungsmodus - Das HELP-Menü:</ins></b></b>

      <b>-&gt; H HELP:</b> Hilfsfunktionen für Elementegenerierung,
                            Manipulationen,
                            Korrekturen,
                            Aug- und Zielpunkteinstellung,
                            Nummernanzeige usw.

Nach Aufruf von HELP wird die Menüleiste des HELP-Menüs angezeigt.

<b>WAHL   AUGE   BILD   NPIX   DEFE   ELIN   MANI   GRAF
XYZ3 . Plan . Such . R1:1 . Corp . Find . LGen . Keys 

0 = + -  -&gt;</b>
        
<b><b><ins>Das tastaturgesteuerte Fadenkreuz:</ins></b></b>

Die Fadenkreuzfunktionen sind für fast alle HELP-Menüfunktionen
relevant. Dqs Operieren mit dem Fadenkreuz wird durch folgende
Anzeigen und Kommandos möglich:

<b>-&gt; CURSORkeys:</b> Steuerung der XY-Bewegung des Fadenkreuzes auf
               dem Bildschirm, (auch Shiftfunktion);
<b>-&gt; BRK:</b>        alte Werte bleiben erhalten,
<b>-&gt; ENTER:</b>      neuangepeilte Werte werden eingetragen;
<b>-&gt; +,-:</b>        Verändern die 3. Koord. des angepeilten Punktes;
<b>-&gt; A:</b>          Anzeige der Raumkoordinaten in den HELP-Funktionen
               oder der Bidschirmkoordinaten im GRAFik-Modus
<b>-&gt; S:</b>          Speedschalter, das Kreuz kann schneller bewegt
               werden (&quot;flackert&quot;), Koordinaten werden nicht
               angezeigt, nach &gt;ENTER&lt; aber richtig abgespei-
               chert;
<b>-&gt; G:</b>          Großes Fadenkreuz über gesamten Ausschnitt
<b>-&gt; K:</b>          Kleines Fadenkreuz
<b>-&gt; F:</b>          an der aktuellen Position des steuerbaren Faden-
               kreuzes wird ein Fadenkreuz über das gesamte
               Bildschirmfenster gezogen, (Orientierungshilfe);
<b>-&gt; M:</b>          Fadenkreuz wird in die Bilschirmmitte und 3.
               Koordinatenwert wird Null gesetzt (Ursprungslage).
<b>-&gt; 1:</b>          Schrittweite  1
<b>-&gt; 5:</b>          Schrittweite  5 (Achtung: SPEED zu schnell!)
<b>-&gt; 0:</b>          Schrittweite 10 (Achtung: SPEED zu schnell!)
<b>Grafische Funktionen des Fadenkreuzes:</b>
<b>-&gt; W:</b>           Walk - Bewegen ohne Veränderung des Bildes 
<b>-&gt; P:</b>          Pen  - Zeichenstift     
<b>-&gt; R:</b>          Radierfunktion   

Die Stift- und Radierfunktion sollten nur bei kleinem Fadenkreuz
und Schrittweite 1 angewendet werden!
Alle Fadenkreuzfunktionen lassen sich nur während der Anzeige des
Kreuzes schalten!

                                  — 14 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;"><b>Die HELP-Menüfunktionen:</b> 

<b>-&gt; X Y Z :</b> Wahl der Blickrichtung:
           aus positiv X auf die YZ-Koordinatenebene (Ansicht), 
           aus negativ Y auf die XZ-Koordinatenebene (Ansicht),
           aus positiv Z auf die XY-Koordinatenebene (Draufsicht).

<b>-&gt; 3     :</b> alle drei Ansichten werden gleichzeitig dargestellt.

<b>-&gt; P PLAN:</b> Darstellung der mit X,Y oder Z angewählten Koordi-
   natenebene, der angewählte Ausschnitt bleibt erhalten, die
   Ausschnittgrenzen werden bemaßt, die jeweiligen Koordinaten-
   achsen werden angezeigt und benannt.

<b>Ausschnittwahlfunktionen zur Wahl des darzustellenden Koor-
dinatensektors der Ebenen: WAHL, SUCH, R1:1, KEYS, 0, =, +, -</b>

<b>-&gt; W WAHL:</b> Bildschirmeingabe der diagonalen Eckpunkte des 
   gesuchten Ausschnittfensters mittels tastaturgesteuertem Faden-
   kreuz in der vorhandenen Darstellung. Nach der Eingabe des 1.
   Eckpunktes wird das Fenster angezeigt (&quot;Gummifenster&quot;).

<b>-&gt; S SUCH:</b> automatisches &quot;Suchen&quot; des mit NPIX definierten
   Punkte- oder Elementebereiches und Darstellung in voller
   Größe im Bildschirmfenster;

<b>-&gt; R R1:1:</b> Relation 1:1, Darstellung eines angewählten
   Sektors in der Auflösung: 1 Bildpunkt = 1 Koordinatenwert.
   Hier ist nur das Anvisieren eines Grundrißpunktes mittels
   Fadenkreuz notwendig. Dieser Punkt definiert die Bildmitte
   des gewünschten Sektors.

<b>-&gt; K KEYS:</b> Anwahl eines Bildpunktes, der die Bildmitte des
   neuen Ausschnittes definiert, mittels Fadenkreuz (Verschieben
   des Koordinatenausschnittes bei konstanter Größe).

<b>-&gt; 0     :</b> der Koordinatenursprung wird in die Bildmitte
   gesetzt, die Ausschnittgröße bleibt konstant

<b>-&gt; =     :</b> Gleichschalten der Ausschnittgrenzen der drei
   Koordinatenebenen, die XY- und die YZ-Ebenengrenzen haben dabei
   Priorität !

<b>-&gt; +, -  :</b> Vergrößern, bzw. Verkleinern des angezeigten
   Koordinatenausschnittes in fest eingestellten Schritten.

   In allen Ausschnitten ist Manipulieren, Korrigieren, Gene-
   rieren usw. möglich.

<b>-&gt; A,B AUGE, BILD:</b> Aug- oder Bildpunkteinstellung mittels
   Fadenkreuz,
   Die alten Aug- oder Bildpunktkoordinaten werden angezeigt
   und das Fadenkreuz auf die entsprechende Stelle plaziert.
   Zur Neueinstellung sind alle Fadenkreuzfunktionen wirksam.

<b>-&gt; NPIX, DEFE, ELIN, MANI, GRAF:</b> Funktionen analog Hauptmenü-
   unterfunktionen;

                                    — 15 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;"><b>-&gt; C CORP:</b> Korrektur von Raumpunktkoordinaten mittels Faden-
   kreuzfunktionen;
   Je nach gewähltem Punkte- oder Elementebereich (NPIX) wird
   die Nummer des 1. Punktes dieses Bereiches angezeigt:

   <b>PKT ...</b>

   &gt;BRK&lt;   : Abbruch und Rücksprung in&#x27;s Menü;
   &gt;ENTER&lt; : Das Fadenkreuz wird auf den Punkt gesetzt und
             die Koordinaten werden angezeigt.

   Jetzt sind Manipulationen mittels Fadenkreuz möglich.

   &gt;BRK&lt;   : Die alten Werte bleiben erhalten, die nächste
             Punktnummer wird angezeigt.
   &gt;ENTER&lt; : Die neueingestellten Koordinaten werden gespei-
             chert, die nächste Punktnummer angezeigt.
  
   erneutes &gt;BRK&lt; : zurück in&#x27;s Menü usw.

<b>-&gt; F FIND:</b> Finden der Elementenummern durch Nummernanzeige auf
   dem gewählten Bildschirmausschnitt.
   Die Nummer wird in die Mitte jedes Elementes plaziert.

   <b>Achtung:</b> Überlagerung der Nummern bei zu kleiner Darstel-
   lung, bei Elementeschachtelung oder -überdeckung !

<b>-&gt; L LGEN:</b> Generierungshilfe für Elemente (Flächen, Körper)
 
   Im Gegensatz zu KOIN (Koordinateneingabe), wo alle Koordi-
   naten eines Punktes sowie alle Informationen zu den ent-
   sprechenden Linienverbindungen direkt eingegeben und die
   Elemente nachträglich definiert (DEFE) werden müssen,
   können hier beliebige Körper durch &quot;Zeichnen&quot; auf dem 
   Bildschirm generiert werden. Alle Werte werden automatisch
   abgespeichert.

   <b>Strategie:</b> Eingabe eines Polygonzuges mittels Fadenkreuz-
   und Bogenfunktionen; dannach Definition als Fläche, pyramiden-
   förmiger oder prismatischer Körper möglich.

   Nach Aufruf von LGEN erscheint das Fadenkreuz in Bildschirm-
   mitte, alle Fadenkreuzfunktionen sind verfügbar;
   Wahl der Lage des ersten Polygonpunktes, Abspeichern mit &gt;ENTER&lt;;

   Suchen des zweiten Punktes: eine bei der Fadenkreuzbewegung
   mitgezogene &quot;Gummilinie&quot; erleichtert die Eingabe !
   <b>&gt;ENTER&lt;:</b> Der letzte Punkt wird jeweils durch eine Linie
   mit dem vorherigen Punkt verbunden, usw.;
   <b>&gt;BRK&lt;  :</b> Unterbrechen des Polygonzuges, Menüanzeige:

   <b>GON  ARC  OPN  -&gt;</b>

   <b>-&gt; A ARC:</b> Fortsetzung des Polygons mit Bogenzug; der Bogen
   wird aus einzelnen Polygonpunkten zusammengesetzt.
   Das Fadenkreuz steht noch auf dem letzten Polygonpunkt;

   Anzeige:  <b>MITTE</b>
   Anvisieren des Mittelpunktes des gewünschten Bogenzuges mit
   Fadenkreuz, dann &gt;ENTER&lt;;

                                  — 16 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;">   Frage:    <b>GRAD ? 0</b>
   Eingabe der Schrittweite der einzelnen Punkte des Bogenpolygons
   in Grad (+ positiver, - negativer Uhrzeigersinn),
   Der erste Bogenpunkt wird dann berechnet und das Fadenkreuz ent-
   sprechend plaziert;

   <b>&gt;BRK&lt;   :</b> Fadenkreuz wird gelöscht, der letzte Bogenpunkt 
   nicht gespeichert und in das Polygonmenü zurückgesprungen,
   Fortsetzung des Polygonzuges möglich;
   <b>&gt;ENTER&lt; :</b> Der angezeigte Bogenpunkt wird gespeichert, der
   nächste berechnet und angezeigt.
   Durch wiederholtes Betätigen von &gt;ENTER&lt; kann schrittweise
   ein Bogen aufgebaut werden und mit &gt;BRK&lt; an beliebiger Stelle
   unterbrochen werden.

   <b>-&gt; G GON:</b> Weiterführung des Polygonzuges
 
   Es können also beliebig viele Bögen und Geraden zu einem
   Polygonzug verbunden, also nacheinander gezeichnet werden !

   Die Anzahl der eingegebenen Punkte wird angezeigt.

   <b>-&gt; BRK  :</b> Abbruch des Polygons
   Das Polygon wird nach Abbruch intern automatisch geschlossen,
   d.h. der letzte Punkt wird mit dem ersten verbunden. Es ist
   also nicht notwendig, zum Ausgangspunkt zurückzukehren !

   <b>-&gt; O OPN:</b> Abbruch, das Polygon wird nicht geschlossen !

   <b>PYRA   QUAD  -&gt;</b>

   <b>-&gt; ENTER :</b> das Polygon wird als flächiges Element abgelegt;

   <b>-&gt; P PYRA:</b> pyramidenförmiger Körper
   mittels Fadenkreuz wird die Spitze der Pyramide angewählt,
   Abschluß mit &gt;ENTER&lt; - der Körper wird als letztes Element
   der Datei angefügt, alle Linienverbindungen werden automatisch
   generiert !

   <b>Achtung:</b> auch die Koordinate der Spitze richtig wählen !

   <b>-&gt; Q QUAD:</b> prismatischer Körper

   <b>DICKE ?</b>
   Die gewünschte Höhe des Prismas in der jeweiligen Generierungs-
   ebene wird eingegeben, der Körper wird automatisch generiert und 
   als letztes Element der Datei angefügt.

                                  — 17 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;"><b><b><ins>7.4.3. Koordinateneingabe:</ins></b></b>

Für direkte Eingabe von Elementen, Teilelementen oder Punkten,
die nicht über die LGEN-Funktion erstellt werden können, sowie
für Ergänzungen, Korrekturen und Löschen von Koordinaten oder
Linienverbindungen;

<b>-&gt; K KOIN:</b> Menü: <b>COR  ADD  INS  DEL  -&gt;</b>

   <b>-&gt; C COR:</b> Korrektur von Punktkoordinaten oder Verbindungen

   <b>PIXL  ELMT  All  -&gt; :</b> Wahl des zu korrigierenden Punkte-
                    bereiches analog NPIX;

   <b>KOOR  VERB  -&gt;</b>: Entscheidung zwischen Koordinaten- oder 
                    Verbindungsdatenkorrektur;

      <b>-&gt; BRK   :</b> zurück in&#x27;s Hauptmenü
      <b>-&gt; K KOOR:</b> Koordinateneingabe
      Anzeige der jeweiligen Punktnummer und der alten Koordinaten-
      werte, Überschreiben möglich!

      <b>1.PKT       X? ...     Y? ...     Z? ...</b>

      <b>-&gt; V VERB:</b> Verbindungslinien
      Anzeige der Punktnummer, der Anzahl der alten Verbindungen
      zu anderen Punkten sowie Aufforderung zur Eingabe der
      Anzahl der neuen Verbindungen:

      <b>1. PKT ANZAHL ? ...</b>
      nach der Eingabe von &gt;ENTER&lt; (Werte bleiben) oder einer
      neuen Anzahn erfolgt die Anzeige der Nummern der alten
      Verbindungspunkte sowie die Aufforderung zur Neueingabe:

      <b>ZU PKT. ? ... 
      ZU PKT. ? ...</b>
      Wiederholung je nach Anzahl der Verbindungen;

   <b>-&gt; A ADD:</b> Addieren, Eingabe von neuen Raumpunkten

   <b>ANZAHL?</b>  Eingabe der gewünschten Punkteanzahl,
            dann analog KOOR und VERB; 

   <b>-&gt; I INS:</b> Einfügen von Punkten in vorhandene Elemente:
   Anzeige der vorhandenen Punktezahl sowie Festlegung des ein-
   zufügenden Punktebereiches analog NPIX;
   Eingabe der neuen Punktkoordinaten sowie der Linienverbin-
   dungen anlog KOOR und VERB;

   <b>-&gt; D DEL:</b> Löschen eines Punkte- oder Elementebereiches
   Wahl des Punktebereiches erfolgt analog NPIX; 
   nach Abschluß der Eingabe durch &gt;ENTER&lt; ist der gewählte
   Bereich gelöscht.

<b>Achtung:</b> Abruch numerischer Eingaben nur mit &gt;B&lt; und &gt;ENTER&lt; !

Soll der eingegebene Punktebereich als neues Element definiert
werden, muß DEFE verwendet werden, ansonsten wird er dem je-
weils vorhergehenden Element zugeordnet.

                                     — 18 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;"><b><b><ins>7.4.4. Grafikeditor:</ins></b></b>

Menü:  <b>LINE   QUAD   CIRC   PERS   FILL   DELT   RESS
       WIND   INVR   TEXT   HCOP   &gt;L/S   BIND   MOVE  -&gt;</b>

<b>-&gt; L LINE:</b> Linienzeichnen, Polygone, mit Fadenkreuz Punkte
           anwählen, jeweils &gt;ENTER&lt;.
           In LINE kann auch die Stift- und Radierfunktion des
           Fadenkreuzes genutzt werden.

<b>-&gt; Q QUAD:</b> Rechteckzeichnen, Wahl der diagonalen Eckpunkte
           des zu zeichnenden Rechteckes mit Fadenkreuz, Er-
           leichterung durch Gummifunktion;

<b>-&gt; C CIRC:</b> Kreiszeichnen, Wahl des Mittelpunktes und eines
           Randpunktes, Gummifunktion;

<b>-&gt; P PERS:</b> Darstellung des 3D-Modells je nach Perspektiv-
           modus ohne vorheriges Löschen der Zeichnung; 

<b>-&gt; F FILL:</b> Füllen und Schraffieren von Flächen (45 Grad)

           <b>STEP ? ...</b> : Abstand der Schraffurlinien (1-N),
           Anwahl der zu füllenden Fläche mit Fadenkreuz;

<b>-&gt; D DELT:</b> Löschen von Flächen oder Linien, Anwahl mit
           Fadenkreuz, Achtung: &quot;Pixelfraß&quot;!

<b>-&gt; W WIND:</b> Zeichnen des Bildrandes;

<b>-&gt; I INVR:</b> Inverse Zeichnungsdarstellung;

<b>-&gt; T TEXT:</b> Beschriften der Darstellung mit allen Cursorfunk-
           tionen, Abschluß mit &gt;ENTER&lt;

<b>-&gt; H HCOP:</b> Hardcopyinitalisierung, Hardcopy, Generierung
           hochauflösender Grafiken;
           Matrixdrucker Typ K6313, LX86;

  <b>COPY  INIT  OVER  -&gt;</b>

  <b>-&gt; C COPY:</b> Ausführung einer initialisierten Hardcopyfunktion,
           ein V24-Modul muß gesteckt sein ! Sollten die Steck-
           plätze des Grundgerätes belegt sein, muß die zu drucken-
           de Grafik ausgeladen, der KC abgeschaltet, in Schacht 8
           die V24 und in Schacht C ein 16k-Modul gesteckt, das 
           System und die Grafik neu geladen und dann erst gedruckt  
           werden !
  <b>-&gt; O OVER:</b> Mehrfachüberdruck einstellbar (z.B. bei schwachem
           Farbband)

  <b>-&gt; I INIT:</b> Initialisierung einer Hardcopyfunktion

  <b>NORM  COLO  HIGH  GRAF  -&gt;</b>

  <b>-&gt; N NORM:</b> Hardcopy im A6-Format, ein Bildpunkt entspricht
           einem Druckerpixel, mit <b>TAB LEFT?</b> kann der Abstand
           zum linken Blattrand in Zeichen eingestellt werden;

                                 — 19 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;">  <b>-&gt; C COLO:</b> Hardcopy im A6-Format, bei eingestellter pixel-
           echter Farbauflösung wird in drei Graustufen gedruckt;

  <b>-&gt; H HIGH:</b> hochauflösende Grafikgenerierung und gleichzei-
           tige Hardcopy, Es werden Teilbilder auf beiden Pixel-
           ebenen gezeichnet, dabei Verlust der evtl. vorhandenen
           Grafiken !

           <b>SIZE: 512 * ? 760</b>
           Einstellung der Größe der Hardcopy in Pixeln, wobei
           die 512 fest, die 760 variabel ist. Das Maximalformat
           512 * 760 enspricht ca. einer A4-Seite, wobei das
           horizontal generierte Bild vertikal gedruckt wird.

           <b>MOVE  X? ...  Y? ...</b>
           Der zu generierende Bildauschnitt kann durch Eingabe
           von XY-Pixelwerten verschoben werden.

  <b>-&gt; G GRAF:</b> Generierung einer hochauflösenden Grafik analog
           HIGH und Speicherung auf einer 32k-Speicherebene (nur
           bei Einsatz von 64- oder 256k-Erweiterungen möglich !)

           <b>USE LAST FILE? Y: -&gt;</b>
           Sicherheitsabfrage, ob die letzte verfügbare Speicher-
           ebene für die Grafik genutzt werden soll, da dort
           vorhandene andere Informationen gelöscht werden.

<b>-&gt; R RESS:</b> Einstellung der Auflösung für die Grafikbearbeitung

           <b>LOW  HIGH  ALL  CLS  -&gt;</b>

  <b>-&gt; L LOW :</b> Einstellung der normalen Bildschirmauflösung

  <b>-&gt; H HIGH:</b> Einstellung der hohen Auflösung, das im Speicher
           abgelegte große Bild wird auschnittsweise in den Bild-
           wiederholspeicher geladen und kann grafisch bearbeitet
           werden. Nach Rückkehr aus dem HCOP-Menü wird automa-
           tisch LOW eingestellt!

  <b>-&gt; A ALL :</b> Die gesamte hochauflösende Grafik wird verdichtet
           auf dem Schirm abgebildet. Höhen- und Breitenverhältnis
           beträgt dann 1:2 . Es entsteht eine Übersichtsgrafik.
           Die Anfangsspalte kann eingegeben werden, sonst &gt;ENTER&lt;.

  <b>-&gt; C CLS :</b> Bildschirm- oder Großgrafikspeicherlöschen je
           nach eingestellter Grafikauflösung (LOW oder HIGH).

<b>-&gt; B BIND:</b> Bildverknüpfungen, Menü: <b>PIX  COL  -&gt;</b>
           
  <b>-&gt; P PIX:</b> logische Verknüpfung der 1. und 2. Bildebene,
           Verknüpfungsarten: <b>OR  XOR  AND  -&gt;</b>
  <b>-&gt; C COL:</b> logische Verknüpfung der Pixel- und Colorebene,
           Nur bei pixelechtem Farbmodus sinnvoll!

                                 — 20 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;"><b>-&gt; M MOVE:</b> Bewegen der abgebildeten Grafik über den Bildschirm,

           im LOW-Modus:  pixelweises Vertikal- oder Horizontal-
                          rollen mit Cursortasten;

           im HIGH-Modus: Blättern in der Großgrafik mit Cursor-
                          tasten (auch Shift-Funktionen!)
                          <b>&gt;M&lt;</b> in MOVE = Sprung zur Grafikmitte
           Grafikeditierungen sind erst nach einem &quot;Blättern&quot;
           abgespeichert und können sonst vorher mit RESS und HIGH
           wieder rückgängig gemacht werden!

<b>-&gt; &gt; &gt;L/S:</b> Ein- oder Ausladen von Bildschirm- oder Groß-
           grafiken von oder auf Kassette/Diskette,

  <b>LOAD  SAVE  -&gt;</b> Laden - Retten
  <b>LOW   HIGH  -&gt;</b> aktuelle Bildschirm- der Großgrafik

  <b>Achtung für Diskettenaufzeichnung:</b> Nach der Wahl von LOW
  oder HIGH wird die Namenseingabe gefordert. Die Dateitypen
  .LGR für LOW-Grafiken und
  .HGR für HIGH-Grafiken sind unbedingt mit eingeben !

  <b>Achtung für Kassettenaufzeichnung:</b> Die Großgrafiken umfassen
  über 100h-Blöcke!

Im Grafikeditor werden in den Fadenkreuzfunktionen die realen
Bildschirmpixelwerte angezeigt (X,Y)  

Soll in HELP die Achsenanzeige und Ausschnittbemaßung ausgeblendet
werden: <b>GRAF</b> anwählen, mit &gt;BRK&lt; zurück in das HELP-Menü und mit
<b>PLAN</b> erneut den Ausschnitt anzeigen lassen. GRAF wirkt hier als
Schalter.

<b>Funktionstastenbelegung:</b> Escape-Funktionen

           <b>F1:</b> Anzeige und Beschreiben Bild 0
           <b>F2:</b> Anzeige und Beschreiben Bild 1
           <b>F3:</b> Ein-/ Abschalten der Farbebene des Bildes
           <b>F4:</b> Ein-/ Abschalten hochauflösende Farbdarstellung
           <b>F5:</b> Inverses Schreiben Ein/ Aus
           <b>F6:</b> Farben komplimentieren
           <b>F7:</b> Anzeige Bild 0, Beschreiben Bild 1
           <b>F8:</b> Anzeige Bild 1, Beschreiben Bild 0
           <b>F9:</b> Modulkontrollanzeige
           <b>FA:</b> CAOS-Systemcheck

<b>Zusätzliche CAOS-Systemfunktionen:</b>

           <b>%CAP</b> Aufruf von &quot;3D-Grafik&quot; mit Aktualisierung der
                Ebene 1 und Zeichnungsgenerierung;
           <b>%REC</b> Aufruf von &quot;3D-Grafik&quot;, Warmstart in das Haupt-
                menü der aktuellen Ebene (nur in Kassettenversion!)
           <b>%RDAT</b> Ebeneninitialisierung oder -schaltung aus dem
                CAOS-Menü

   Sprung in&#x27;s CAOS-Menü durch <b>SHIFT und C</b> im Hauptmenü von 3D-G.

                                     — 21 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;"><b><b><ins>8.  Zusammenfassung der Kommandos:</ins></b></b>

<b>Hauptmenü:

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

                                 — 22 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;"><b>-&gt; MANI:</b> Manipulation:

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

                                    — 23 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;">   <b>-&gt; LGEN:</b> grafische Elementegenerierung

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


<b><b><ins>9.  Symbole, Abkürzungen, Begriffe:</ins></b></b>

<b>3D</b>        dreidimensional
<b>&gt;  &lt;</b>      Tastenbezeichnung
<b>-&gt;</b>        Aufforderung zum Tastendruck (1. Zeichen des Kürzels)
<b>?</b>         verlangt meist direkte Werteingabe
<b>PKT</b>       Punkt, Raumpunkt: definiert durch XYZ-Koordinaten,
<b>Linie</b>     sichtbare Verbindung zwischen 2 Punkten, aber nur
          einem Punkt zugeordnet (Anzahl der Verbindungen,
          Nummern der Verbindungspunkte)
<b>NR.</b>       Nummer: Punkte und Elemente fortlaufend nummeriert
<b>Element</b>   durch Marke definierte Punktemenge mit Verbindungen
<b>Augpunkt</b>  Koordinaten des Betrachterauges im Raum
<b>Bildpunkt</b>  Koordinaten des die Blickrichtung bestimmenden Punktes
          im Raum  
<b>Ebene</b>     32 KByte Speicherbereich, von 0 bis 7FFFh im RAM


<b><b><ins>10. Fehlermeldungen:</ins></b></b>

<b>ERROR</b>     bei direkter Werteingabe:
          - falsches Zahlenformat
          - Zahl enthält falsche Zeichen
          - Zahl außerhalb des Wertebereiches
          nach &quot;Error&quot; erneute Werteingabe möglich !

<b>NO MEMORY</b> Speicherüberlaufwarnung: die zuletzt eingegebenen
          Werte werden ignoriert !

<b>FALSE BASE!</b> Keine oder falsche Speicherebeneninitialisierung

                                 — 24 —</pre>

<pre style="font-family: 'Courier New', Courier, monospace; font-size: 12px; line-height: 1.35; color:#000; padding:20px 16px 12px; border:1px solid #bbb; white-space: pre; display: inline-block; margin: 6px 0; background:#fafaf5;"><b><b><ins>11. Literatur:</ins></b></b>

/1/ Thomae, Reiner: Perspektive und Axonometrie, Verlag Kohlhammer
    1976
/2/ Lampe, Bernhard: Algorithmen der Mikrorechentechnik, Maschi-
    nenprogrammierung und Interpretertechniken des U880/D,
    2. Auflage 1983
/3/ VEB Mikroelektronik &quot;Wilhelm Pieck&quot; Mühlhausen: Kleincomputer
    KC 85/2, Systembeschreibung, Stand 9/85
/4/ VEB Mikroelektronik &quot;Karl Marx&quot; Erfurt: Befehlsbeschreibung
    U880/D
/5/ Schlenzig, Klaus u. Stefan: Tips und Tricks für kleine Computer,
    Militärverlag der DDR, Berlin, 1988
      

                                  — 25 —</pre>
