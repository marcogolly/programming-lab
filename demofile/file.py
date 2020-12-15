#crea file che contiene delle righe di prova separate da ,

#apro il file
f = open("demofile/demofile.txt", "w")


contenuto="ciao,mondo\nciao,atutti\nhello,world"
f.write(contenuto)

#chiudo
f.close()
