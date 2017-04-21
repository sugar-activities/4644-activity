#!/usr/bin/python

import ConfigParser

# Global definition
CONF_FILE='elephant.conf'
CAT_SECTION='Categories'
WORDS_SECTION='Words'

# Class
# Return the word list from config file and numbers of word
class word_list:

    
    def __init__(self):
        # Number of words
        self.number_of_words = len(self.get_word_list())

    # Get all categories from config file
    def get_categories(self):    
        parser = ConfigParser.SafeConfigParser()
        parser.read(CONF_FILE)

        full_list = parser.items(CAT_SECTION)
        category_list = [row[1] for row in full_list]

        return category_list

    # Get all words from a specifir category
    #def get_words_in_category(self, category):
    #    parser = ConfigParser.SafeConfigParser()
    #    parser.read(CONF_FILE)
    #
    #    word_list = parser.options(category)
    #
    #    return word_list

    # Get all words form config file
    def get_word_list(self):
        parser = ConfigParser.SafeConfigParser()
        parser.read(CONF_FILE)
        
        full_list = parser.items(WORDS_SECTION)
        word_list = [row[0] for row in full_list]

        return word_list

    # Get path of choosen image
    def get_word_image_path(self, word):
        parser = ConfigParser.SafeConfigParser()
        parser.read(CONF_FILE)

        image_path = parser.get(WORDS_SECTION, word)

        return image_path



       