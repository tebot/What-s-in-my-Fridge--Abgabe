# What-s-in-my-Fridge--Abgabe
Ich habe an einer code-competition teilgenommen und das ist meine Abgabe

Um das Programm zu starten öffnen sie eine Linux oder Python-Konsole 
und geben sie python chefkoch3.py ein
Beantworten sie die Fragen dann wird ihnen ein Rezept vorgeschlagen.

Wenn man Linux verwendet kann es sein das man Zeile 29, 66 und 86 auskommentieren muss und dafür Zeile 30,67 und 87 einfügen muss. 
Ich habe das Programm in Windows getestet. (Leider steht mir kein Linux Rechner zur Verfügung an dem ich das Testen kann)

Ich habe erst überlegt mit einer API zuarbeiten. Es gab ein paar APIs auf Deutsch, ich fand die aber entweder nicht gut oder sie waren kostenpflichtig.
Da immer wenn meine Freunde oder ich ein Rezept im Internet suchen wir auf chefkoch.de gehen, dachte ich das eine API von chefkoch.de am besten wäre. Die Webseite eine große Community und Bekanntheit hat und dadurch auch sehr viele Rezepte hat. 
Für chefkoch.de gab es aber keine API auf die ich Zugriff bekommen konnte. Ich habe mir dann die Webseite genauer angeschaut. Ich habe festgestellt das wenn man einen request macht man ein HTML File bekommt das viel JSON-Dateien enthält. Ich habe dann eine Art Semantic Search gemacht und mir die Teile aus dem HTML File rausgesucht die ich brauchte.
Zudem ist mir aufgefallen dass man allein über die URL suchen starten kann (sogar mit Preferencen). Ich habe dann ein paar Codes für die Preferencen rausgesucht und damit dann meine requests gemacht.
Um genauer zu sein habe ich die URL genommen und alles was ich suchen wollte angehängt und danach Rezepte.html angehängt. Also z.B. https://www.chefkoch.de/rs/s0g111/nudeln+tomaten/Rezepte.html 
rs=nach etwas suchen
s0g111=ist vegan 
nudeln+tomaten=ist nach was ich gesucht habe

Ich fand das eine sehr einfache Lösung und war mit den Ergebnissen einigermaßen zufrieden.

Ich habe mich für SQLite als Datenbank entschieden da die Bibliothek in Python standartmäßig enthalten ist und ich keine zusätzliche Software verwenden/installieren musste.
Außerdem denke ich das SQLite voll kommen ausreichend für die Anwendung ist.
