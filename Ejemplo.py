#!/usr/bin/python

import elephant

from subprocess import Popen

def main():
    words = elephant.word_list()

    word_list = words.get_word_list()
    print 'Lista de palabras'
    print word_list
    print 'Cantidad de palabras %s' %words.number_of_words
    print ' '
    
    print 'path de imagenes'
    for word in word_list:
        print words.get_word_image_path(word)
    print ' '

    from random import choice
    word = choice(word_list)
    path = words.get_word_image_path(word)

    print 'Palabra aleatoria %s y el path correspndiente %s' %(word, path)

    choice_letter = elephant.letters(word)

    letter_to_say_index = choice_letter.letter_index
    letter_to_say = choice_letter.letter

    print 'Indice %s y letra %s' %(letter_to_say_index, letter_to_say)

    #   all_indexes = choice_letter.get_all_indexes(word, letter_to_say)
    all_indexes = choice_letter.all_indexes
    print 'Todos los indices validos %s' %all_indexes

    #false_choices = choice_letter.get_false_options(word, all_indexes)
    false_choices = choice_letter.false_options
    print 'Opciones invalidas %s. No tienen que coincidir con los validos' \
        %false_choices

    #relative_place = choice_letter.get_relative_place( \
    #    letter_to_say_index, \
    #    all_indexes)
    relative_place = choice_letter.relative_place
    print 'Lugar relativo %s' %relative_place

    #place_word = choice_letter.translate_relative_place(relative_place)
    place_word = choice_letter.place_word
    print 'Lugar relativo %s' %place_word

    speech_to_say = 'Donde esta la '
    if place_word == False:
        speech_to_say += ''
    else:
        speech_to_say += place_word
    speech_to_say += ' letra '
    speech_to_say += letter_to_say 
    
    print speech_to_say
    
    say(speech_to_say)

    options_places = choice_letter.random_places
    print 'Opciones'
    print 'Opcion 1 %s' %choice_letter.translate_to_str(options_places[0])
    print 'Opcion 2 %s' %choice_letter.translate_to_str(options_places[1])
    print 'Opcion 3 %s' %choice_letter.translate_to_str(options_places[2])

def say(text):
    Popen(['espeak', '-v', 'es', text])
    
if __name__ == "__main__":
    main()