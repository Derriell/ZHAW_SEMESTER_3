# Braining Cave

Indexes für verschiedene Faktoren, die die verschiedenen Aspekte des Spielflusses beeinflussen.
    . Temperatur                wenn ein gewisser Wert erreicht wird, ist das Spiel verloren? (evt. könnte
                                die Temperatur, die Anzahl Naturkatastrophen so weit erhöhen, dass das Spiel nicht
                                 mehr gewonnen werden kann.)
    . Bevölkerungsanzahl        Mit fortlaufender Zeit steigt die Bevölkerungszahl. Mit steigender Bevölkerungszahl
                                steigt der Einfluss auf die CO2-Emissionen.
    . CO2-Emissionen            Die CO2-Emissionen sind ein Indiz für die Umweltverschmutzung. Mit steigenden CO2-Emissionen
                                steigt die Temperatur.
    . Naturkatastrophen index   Mit steigender Temperatur steigt die Anzahl Naturkatastrophen. Naturkatastrophen können
                                die Bevölkerungszahl reduzieren und die CO2-Emissionen erhöhen.
    . Forschungsstand           Der Stand der Forschung steigt mit fortlaufender Zeit. Sie steigt schneller, mit wachsender
                                Bevölkerungszahl und wird zeitweise gesenkt wenn Katastrophen passieren.

Ideen für GameLogik
    Grund-Implementierung
    Die Bevölkerungszahl steigt mit der Zeit. Mit steigender Bevölkerungszahl steigen die CO2-Emissionen. Mit steigenden CO2-Emissionen steigt die Temperatur. Erhöhte Temperatur führt zu mehr Naturkatastrophen. Naturkatastrophen reduzieren die Bevölkerungszahl und erhöhen die CO2-Emissionen.

    Verkehrsmittel-orientierte Game-logik
    Je nach Standort sind unterschiedliche Verkehrsmittel verfügbar. So kann ein Punkt am Wasser, 
    ein Hafen sein, an dem Schiffe anlegen. Ein Punkt an wichtigen Knotenpunkten kann ein Flughafen sein. Velo und Auto sind überall verfügbar, 
    sie verursachen jedoch unterschiedliche CO2-Emissionen, und können keine wasserbasierten Transporte durchführen. Zudem können Velos sich in die Diagonalen Richtungen bewegen, was eine schnellere Bewegung bedeutet. Es gibt Knotenpunkte von wo aus Züge fahren. Diese sind jedoch nicht überall verfügbar, dafür aber effizienter und umweltfreundlicher als Autos.

    Forschung-orientierte Game-logik
    Die Forschungspunkte können durch das Neutralisieren von Naturkatastrophen und das Reduzieren von CO2-Emissionen erlangt werden. Diese Punkte
    können dann in die Forschung von neuen Technologien investiert werden, die die CO2-Emissionen reduzieren und die Bevölkerungszahl erhöhen. 

    Basics-orientierte Game-logik
    Der Spieler kann sich auf der Weltkarte in 8 Richtungen bewegen. Ein erreichter Punkt wird Grün markiert, und dehnt sich mit der Zeit in allen Richtungen aus (wenn angrenzend an andere Punkte). 

Ablaufmöglichkeiten
    Beim eintreten eines Ereignisses (z.B. Naturkatastrophe) wird das Spiel angehalten und eine Anzeige erscheint, die den Spieler über das Ereignis informiert.
