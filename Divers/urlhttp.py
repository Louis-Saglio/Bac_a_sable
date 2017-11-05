import urllib.request as ur

fichier = ur.urlopen('http://www.voidspace.org.uk')
a = fichier.read()
print(a)
help(fichier)
