import ConfigParser
import random

# Global definition
CONF_FILE='elephant.conf'
CAT_SECTION='Categories'
WORDS_SECTION='Words'
MAIN_SECTION='Main'

# Class word_list
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

# Class letters
class letters:
    
    def __init__(self, word):
        self._arguments = self._get_letter_index(word)
        self.letter_index = self._arguments[0]
        self.letter = self._arguments[1]
        # Just for debugging
        # print self.letter
        # print self.letter_index

        self.all_indexes = self._get_all_indexes(word, self.letter)
        # Just for debuggin
        # print self.all_indexes

        self.false_options = self._get_false_options(word, self.all_indexes)
        # Just for debugging
        # print self.false_options

        self.relative_place = self._get_relative_place(self.letter_index, \
                                                       self.all_indexes)

        self.place_word = self.translate_to_str(self.relative_place)

        self.random_places = self._get_random_places(self.letter_index, \
                                                     self.false_options)

    # Return a random letter for a given word and index
    def _get_letter_index(self, word):

        word_len = len(word)

        # Generate a random index of a letter in the word
        letter_index = random.randint(0, word_len - 1)

        # Get the letter at position letter_index
        letter = word[letter_index]
        
        return letter_index, letter

    # Return list of indexes for every ocurrence ot the letter in the word.
    def _get_all_indexes(self, word, letter):

        # Init vars
        word_len = len(word)
        indexes = []
        
        # Generates a list with indexes of ocurrences of the letter
        i = 0
        while (i < word_len):
            if word[i] == letter:
                indexes.append(i)
            i+=1
               
        return indexes

    # Return false options non-overlaping with true options
    def _get_false_options(self, word, true_indexes):
        word_len = len(word)
        false_choices = []

        i = 0
        while (i < 2):
            false_choice = random.randint(0, word_len - 1)
            if (false_choice not in true_indexes and \
                false_choice not in false_choices) == True:
                    false_choices.append(false_choice)
                    i += 1            

        return false_choices

    # Return the relative place of a letter in case there are multiples
    # ocurrences of the letter. False in case there are only one.
    def _get_relative_place(self, letter_index, true_indexes):

        if len(true_indexes) == 1:
            return 999

        relative_place = true_indexes.index(letter_index)

        return relative_place


    # Translate relative place to words
    def translate_to_str(self, relative_place):

        if relative_place == 999:
            return False

        places = ['Primera', \
                  'Segunda', \
                  'Tercera', \
                  'Cuarta',  \
                  'Quinta',  \
                  'Sexta',   \
                  'Septima', \
                  'Octava',  \
                  'Novena',  \
                  'Decima']

        return places[relative_place]

    # Generate random places for options
    def _get_random_places(self, true_choice, false_choice):
        options = []

        options.append(true_choice)
        options.append(false_choice[0])
        options.append(false_choice[1])
        
        random.shuffle(options)

        return options

  