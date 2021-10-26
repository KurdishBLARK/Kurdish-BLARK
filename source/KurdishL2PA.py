# -*-coding: utf-8 -*-

# Hossein Hassani
# Started @: 07 June 2021
# Last update @: 23 October 2021

# Kurdish Latin into Persian/Arabic transliterator
# This program reads a text (assuming it has been written in Kudish using
# Latin script) and converts it to its RTL equivalent in Persian/Arabic script.
# Usage: KurdishL2PA.py "LatinFile" "outputFile"


import os
import sys

def KurdishL2PA(inputFile, outputFile):

    import codecs

    def replace_all(text, trigramDic, bigramDic, digramDic):
        for i, j in trigramDic.iteritems():
            text = text.replace(i, j.decode('utf-8'))

        for i, j in bigramDic.iteritems():
            text = text.replace(i, j.decode('utf-8'))


        for i, j in digramDic.iteritems():
            text = text.replace(i, j.decode('utf-8'))

        return text

    # -------------------------------------
    # The order of process is important!
    # -------------------------------------

    digramDic = {
            '٠'.decode('utf-8'): '٠',
            '1'.decode('utf-8'): '١',
            '2'.decode('utf-8'): '٢',
            '3'.decode('utf-8'): '٣',
            '4'.decode('utf-8'): '٤',
            '5'.decode('utf-8'): '٥',
            '٦'.decode('utf-8'): '٦',
            '7'.decode('utf-8'): '٧',
            '٨'.decode('utf-8'): '٨',
            '9'.decode('utf-8'): '٩',
            '0'.decode('utf-8'): '٠',
            '1'.decode('utf-8'): '١',
            '2'.decode('utf-8'): '٢',
            '3'.decode('utf-8'): '3',
            '4'.decode('utf-8'): '٤',
            '5'.decode('utf-8'): '٥',
            '6'.decode('utf-8'): '٦',
            '7'.decode('utf-8'): '٧',
            '8'.decode('utf-8'): '٨',
            '9'.decode('utf-8'): '٩',
            '['.decode('utf-8'): '[',
            ']'.decode('utf-8'): ']',
            '/'.decode('utf-8'): '/',
            ':'.decode('utf-8'): ':',
            '”'.decode('utf-8'): '"',
            '“'.decode('utf-8'): '"',
            '٠'.decode('utf-8'): '٠',
            ','.decode('utf-8'): '،',
            ' '.decode('utf-8'): ' ',
            '،'.decode('utf-8'): ',',
            '?'.decode('utf-8'): '؟',
            'a'.decode('utf-8'): 'ا',
            'e'.decode('utf-8'): 'ە',
            'e'.decode('utf-8'): 'ە',
            'a'.decode('utf-8'): 'ا',
            'ê'.decode('utf-8'): 'ێ',
            'b'.decode('utf-8'): 'ب',
            'p'.decode('utf-8'): 'پ',
            't'.decode('utf-8'): 'ت',
            'ṭ'.decode('utf-8'): 'ط',
            'ṣ'.decode('utf-8'): 'ص',
            'c'.decode('utf-8'): 'ج',
            'ç'.decode('utf-8'): 'چ',
            'ḥ'.decode('utf-8'): 'ح',
            'x'.decode('utf-8'): 'خ',
            'd'.decode('utf-8'): 'د',
            'r'.decode('utf-8'): 'ر',
            'z'.decode('utf-8'): 'ز',
            'j'.decode('utf-8'): 'ژ',
            's'.decode('utf-8'): 'س',
            'ş'.decode('utf-8'): 'ش',
            'ẋ'.decode('utf-8'): 'غ',
            'f'.decode('utf-8'): 'ف',
            'q'.decode('utf-8'): 'ق',
            '‘'.decode('utf-8'): 'ع',
            'ẋ'.decode('utf-8'): 'غ',
            'k'.decode('utf-8'): 'ک',
            'k'.decode('utf-8'): 'ك',
            'g'.decode('utf-8'): 'گ',
            'l'.decode('utf-8'): 'ل',
            'm'.decode('utf-8'): 'م',
            'n'.decode('utf-8'): 'ن',
            'o'.decode('utf-8'): 'ۆ',
            'h'.decode('utf-8'): 'ه',
            'i'.decode('utf-8'): '',
            'î'.decode('utf-8'): 'ی',
            'u'.decode('utf-8'): 'و',
            'v'.decode('utf-8'): 'ڤ',
            'û'.decode('utf-8'): 'وو',
            'w'.decode('utf-8'): 'و',
            'y'.decode('utf-8'): 'ی',
            'E'.decode('utf-8'): 'ئ',
            'A'.decode('utf-8'): 'ا',
            'Ê'.decode('utf-8'): 'ێ',
            'B'.decode('utf-8'): 'ب',
            'P'.decode('utf-8'): 'پ',
            'T'.decode('utf-8'): 'ت',
            'C'.decode('utf-8'): 'ج',
            'Ç'.decode('utf-8'): 'چ',
            'Ḥ'.decode('utf-8'): 'ح',
            'X'.decode('utf-8'): 'خ',
            'D'.decode('utf-8'): 'د',
            'R'.decode('utf-8'): 'ر',
            'Z'.decode('utf-8'): 'ز',
            'J'.decode('utf-8'): 'ژ',
            'S'.decode('utf-8'): 'س',
            'Ş'.decode('utf-8'): 'ش',
            'F'.decode('utf-8'): 'ف',
            'Q'.decode('utf-8'): 'ق',
            'K'.decode('utf-8'): 'ک',
            'k'.decode('utf-8'): 'ك',
            'G'.decode('utf-8'): 'گ',
            'L'.decode('utf-8'): 'ل',
            'M'.decode('utf-8'): 'م',
            'N'.decode('utf-8'): 'ن',
            'O'.decode('utf-8'): 'ۆ',
            'H'.decode('utf-8'): 'ه',
            'Î'.decode('utf-8'): 'ی',
            'U'.decode('utf-8'): 'و',
            'V'.decode('utf-8'): 'ڤ',
            'Û'.decode('utf-8'): 'وو',
            'W'.decode('utf-8'): 'و',
            'Y'.decode('utf-8'): 'ی',
            }

    bigramDic = {
             ' i'.decode('utf-8'): '',
            'iî'.decode('utf-8'): 'ئی',
            'ae'.decode('utf-8'): 'ائە',
            'eh'.decode('utf-8'): 'هە',
            ' a'.decode('utf-8'): ' ئا',
            '-a'.decode('utf-8'): ' ئا',
            ' ê'.decode('utf-8'): ' ئێ',
            '“e'.decode('utf-8'): '”ئە',
            ' A'.decode('utf-8'): ' ئا',
            ' Ê'.decode('utf-8'): ' ئێ',
            'rr'.decode('utf-8'): 'ڕ',
            ' I'.decode('utf-8'): ' ئی',
            ' o'.decode('utf-8'): ' ئۆ',
            ' O'.decode('utf-8'): ' ئۆ',
            '“o'.decode('utf-8'): '"ئۆ',
            '“O'.decode('utf-8'): '"ئۆ',
            }

    trigramDic = {
            ' e '.decode('utf-8'): 'ە ',
            ' e.'.decode('utf-8'): 'ە.',
            ' e,'.decode('utf-8'): 'ە، ',
            '-i '.decode('utf-8'): 'ی ',
            ' î.'.decode('utf-8'): 'ی.',
            ' î '.decode('utf-8'): 'ی ',
            ' û '.decode('utf-8'): ' و ',
            '-û-'.decode('utf-8'): ' و ',
            ' be'.decode('utf-8'): ' بە',
            ' el'.decode('utf-8'): ' ئەل',
            ' eê'.decode('utf-8'): ' ئی',
            ' ed'.decode('utf-8'): ' ئەد',
            ' eg'.decode('utf-8'): ' ئەگ',
            ' eḥ'.decode('utf-8'): ' ئەح',
            ' em'.decode('utf-8'): ' ئەم',
            ' es'.decode('utf-8'): ' ئەس',
            ' ez'.decode('utf-8'): ' ئەز',
            ' ev'.decode('utf-8'): ' ئەڤ',
            ' ew'.decode('utf-8'): ' ئەو',
            ' eẋ'.decode('utf-8'): ' ئەغ',
            ' êw'.decode('utf-8'): ' ئیو',
            ' Ed'.decode('utf-8'): ' ئەد',
            ' Eg'.decode('utf-8'): ' ئەگ',
            ' Em'.decode('utf-8'): ' ئەم',
            ' Es'.decode('utf-8'): ' ئەس',
            ' Ez'.decode('utf-8'): ' ئەز',
            ' Ev'.decode('utf-8'): ' ئەڤ',
            ' Ew'.decode('utf-8'): ' ئەو',
            ' Eẋ'.decode('utf-8'): ' ئەغ',
            'qq,'.decode('utf-8'): 'ق،',
            'qq.'.decode('utf-8'): 'ق.',
            }


    f = codecs.open(inputFile, encoding='utf-8')
    originalText = f.read()
    f.close()


    convertedText = replace_all(originalText, trigramDic, bigramDic, digramDic)
     
    o = codecs.open(outputFile, 'w', encoding='utf-8')
    o.write(convertedText);
    o.close()

def main():
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    if not os.path.isfile(inputFile):
        print("File path {} does not exist. Exiting...".format(inputFile))
        sys.exit()

    if os.path.isfile(outputFile):
        print("File path {} alreday exists. Exiting...".format(outputFile))
        sys.exit()
    
    KurdishL2PA(inputFile, outputFile)	

if __name__ == '__main__':
   main()












