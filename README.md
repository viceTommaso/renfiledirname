# renfiledirname


## Prerequisites
python 3

## Program
Il programma può essere usato per rimpiazzare un carattere nel nome di file e cartelle (anche nelle sottocartelle, sottocartelle comprese).
Ad esempio, se un qalsiasi programma potrebbe dare errore con file contenenti spazi nel nome del file, con questo programma basterà inserire lo spazio quando viene richiesto "Before" e confermare senza aggiungere altri caratteri quando viene richesto "After".

Utilizzando i seguenti parametri:

`BEFORE`: carattere da sostituire

`AFTER`: carattere con il quale sostituire

`DIRECTORY`: cartella dal quale partire ad elaborare file, cartelle e sottocartelle

Il programma può essere eseguito da linea comando nel seguente modo: "`renfiledirname BEFORE AFTER DIRECTORY`" L'ultimo parametro può essere tralasciato

## Warning
Attenzione a non lasciare il parametro BEFORE vuoto, altrimenti il carattere che volete inserire sarà presente tra ogni carattere, in ogni caso il programma chiederà conferma di questa operazione e per confermarla basterà digitare "`Y`"/"`y`"

## Author
Vicentini Tommaso
