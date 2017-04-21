# Copyright 2013 D.Sc. Ing. Diego Pinto, Lic. Roberto Cristaldo
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import gtk
import logging
import elephant
import subprocess

from time       import sleep
from random     import choice
from gettext    import gettext as _

from sugar.activity import activity
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.activity.widgets import ActivityButton
from sugar.activity.widgets import ActivityToolbox
from sugar.activity.widgets import TitleEntry
from sugar.activity.widgets import StopButton
from sugar.activity.widgets import ShareButton
      
class ElephantActivity(activity.Activity):
    """ElephantActivity class as specified in activity.info"""

    def __init__(self, handle):
        """Set up the Elephant activity."""
        activity.Activity.__init__(self, handle)
        
        # we do not have collaboration features
        # make the share option insensitive
        self.max_participants = 1

        # toolbar with the new toolbar redesign
        toolbar_box = ToolbarBox()

        activity_button = ActivityButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        title_entry = TitleEntry(self)
        toolbar_box.toolbar.insert(title_entry, -1)
        title_entry.show()

        share_button = ShareButton(self)
        toolbar_box.toolbar.insert(share_button, -1)
        share_button.show()
        
        separator = gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        # Instances to Elephants classes
        words = elephant.word_list()
        
        # Get a word form word list and path
        self.get_random_word(words)
       
        # Vertical box conteinter definition
        vbox_main = gtk.VBox()

        # Horizontal boxes conteiners definition
        hbox_01 = gtk.HBox()
        hbox_02 = gtk.HBox()
        hbox_03 = gtk.HBox()

        # Buttons definitions
        self.button_repeat = gtk.Button()
        self.button_repeat.set_label('Repetir')
        
        self.button_option1 = gtk.Button()
        self.button_option2 = gtk.Button()
        self.button_option3 = gtk.Button()

        # Image and label word
        self.label_word = gtk.Label()
        self.image_word = gtk.Image()
        #self.image_word = self.show_image(path)
        #self.label_word = self.show_label(word)
        
        # Create layout
        self.set_canvas(vbox_main)
        vbox_main.add(hbox_01)
        vbox_main.add(hbox_02)
        vbox_main.add(hbox_03)

        # Put label and label on layout
        hbox_02.add(self.image_word)
        hbox_02.add(self.label_word)

        # conectors
        self.connect('realize', self.__window_realize)
        self.button_repeat.connect('clicked', self.__button_clicked_rep)
        self.button_option1.connect('clicked', self.__button_clicked_op)
        self.button_option2.connect('clicked', self.__button_clicked_op)
        self.button_option3.connect('clicked', self.__button_clicked_op)
        
        # Put buttons on layout
        hbox_01.add(self.button_repeat)
        hbox_03.add(self.button_option1)
        hbox_03.add(self.button_option2)
        hbox_03.add(self.button_option3)

        # ShowMeTheMoney!!!
        vbox_main.show_all()
        #label_word.show()
        self.elephant_is_saying()
        

    # Get random word form word list
    def get_random_word(self, words):
        word_list = words.get_word_list()
        self.word = choice(word_list)
        self.path = words.get_word_image_path(self.word)

    # Create image from path
    def show_image(self):
        pixbuf = gtk.gdk.pixbuf_new_from_file(self.path)
        scaled_pixbuf = pixbuf.scale_simple(150,150,gtk.gdk.INTERP_BILINEAR)
        self.image_word.set_from_pixbuf(scaled_pixbuf)


    # Crete label form word
    def show_label(self):
        self.label_word.set_text(self.word)
        
    # Create proper lables for options buttons
    def set_option_label(self, option, position):
        label = option
        label += ' Es la '
        label += position
        label += ' letra'

        return label

    def __window_realize(self, window):
        self.elephant_is_saying(self.word, self.path)
        

    # Say the word and riddle on button click
    def __button_clicked_rep(self, button):
            self.speech_to_say()

    def __button_clicked_op(self, button):
       
        if button == self.button_true:
            self.say('Felicitaciones. Tu respuesta es correcta')

            # Repeat
            words = elephant.word_list()
            self.get_random_word(words)

            self.elephant_is_saying()            
        else:
            self.say('Intenta de nuevo.')
            self.speech_to_say() 

                   
    # Say the word and riddle
    def speech_to_say (self):

        speech_to_say = 'Donde esta la '
        if self.place_word == False:
            speech_to_say += ''
        else:
            speech_to_say += self.place_word
        speech_to_say += ' letra '
        speech_to_say += self.letter_to_say 

        self.say(self.word)
        self.say(speech_to_say)

    # Say.. sayyyy.... saaaaayyyy...
    def say(self, text):
        subprocess.call(['espeak', '-v', 'es', text])

    def elephant_is_saying (self):
        choice_letter = elephant.letters(self.word)
        
        self.letter_index = choice_letter.letter_index
        self.letter_to_say = choice_letter.letter
        self.place_word = choice_letter.place_word
        self.random_places = choice_letter.random_places
        
        self.show_image()
        self.show_label()

        op_label = choice_letter.translate_to_str(self.random_places[0])
        label = self.set_option_label('Opcion 1:',  op_label)
        self.button_option1.set_label(label)

        op_label = choice_letter.translate_to_str(self.random_places[1])
        label = self.set_option_label('Opcion 2:', op_label)      
        self.button_option2.set_label(label)

        op_label = choice_letter.translate_to_str(self.random_places[2])
        label = self.set_option_label('Opcion 3:', op_label)      
        self.button_option3.set_label(label)
        
        if self.letter_index == self.random_places[0]:
            self.button_true = self.button_option1
        elif self.letter_index == self.random_places[1]:
            self.button_true = self.button_option2
        elif self.letter_index == self.random_places[2]:
            self.button_true = self.button_option3
        else:
            self.speech_to_say('Algo salio mal')
        
        self.speech_to_say()