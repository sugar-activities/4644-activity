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
import pango 

from random import choice

from gettext import gettext as _

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

        # label with the text, make the string translatable
        # label = gtk.Label(_("Hello World!"))
        # self.set_canvas(label)
        # label.show()

        # Instances to Elephants classes
        words = elephant.word_list()
        choice_letter = elephant.letters()


        
        # Vertical box conteinter definition
        vbox_main = gtk.VBox()

        # Horizontal boxes conteiners definition
        hbox_01 = gtk.HBox()
        hbox_02 = gtk.HBox()
        hbox_03 = gtk.HBox()

        # Buttons definitions
        button_repeat = gtk.Button()
        button_repeat.set_label('Repetir')
	        
        button_option1 = gtk.Button()
        button_option1.set_label('Opcion 1:')
        
        button_option2 = gtk.Button()
        button_option2.set_label('Opcion 2:')
        
        button_option3 = gtk.Button()
        button_option3.set_label('Opcion 3:')

        #Old activity title
        #image_word = gtk.Image()
        #pixbuf = gtk.gdk.pixbuf_new_from_file("images/elefante_logo.png")
        #scaled_pixbuf = pixbuf.scale_simple(150,150,gtk.gdk.INTERP_BILINEAR)
        #image_word.set_from_pixbuf(scaled_pixbuf)
        
        #label_word = gtk.Label()
        #label_word.set_text('Elefante')

        
        #Get a word form word list and path
        word, path = self.get_random_word(words)

        #Image and label word
        image_word = self.show_image(path)
        label_word = self.show_label(word)
        
        # Create layout
        self.set_canvas(vbox_main)
        vbox_main.add(hbox_01)
        vbox_main.add(hbox_02)
        vbox_main.add(hbox_03)

        # Put label and label on layout
        hbox_02.add(image_word)
        hbox_02.add(label_word)

        # Put buttons on layout
        hbox_01.add(button_repeat)
        hbox_03.add(button_option1)
        hbox_03.add(button_option2)
        hbox_03.add(button_option3)

        #ShowMeTheMoney!!!
        vbox_main.show_all()

    # Get random word form word list
    def get_random_word(self, words):
        word_list = words.get_word_list()
        word = choice(word_list)
        path = words.get_word_image_path(word)

        return word, path

    # Create image from path
    def show_image(self, path):
        image = gtk.Image()
        pixbuf = gtk.gdk.pixbuf_new_from_file(path)
        scaled_pixbuf = pixbuf.scale_simple(150,150,gtk.gdk.INTERP_BILINEAR)
        image.set_from_pixbuf(scaled_pixbuf)

        return image

    # Crete label form word
    def show_label(self,word):
	upper_word = word.upper()
	label = gtk.Label()
	label.set_use_markup(True)
	label.set_markup("<span font_desc='Verdana' size='40000'><b>%s</b></span>" % upper_word)
	
        return label
        
