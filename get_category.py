#!/usr/bin/python

from ConfigParser import SafeConfigParser


def main():
    parser = SafeConfigParser()
    parser.read('palabras.ini')

    ListaCategoria = parser.items('Categorias')

    #print ListaCategoria

    for cat, catname in ListaCategoria:
        print 'La categoria es: %s' %catname

if __name__ == "__main__":
    main()
