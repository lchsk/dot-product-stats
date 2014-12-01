DATA_DIRECTORY  = '../data/'
LETTER_FILENAME = 'part'

class DataSet():
    def __init__(self, p_train_dirs, p_test_dir):
        self.train = p_train_dirs
        self.test  = p_test_dir

genesis = DataSet(['danish_genesis',
    'english_genesis',
    'finnish_genesis',
    'german_genesis',
    'norwegian_genesis',
    'spanish_genesis',
    'swedish_genesis'
], 'test_genesis')

genesis_spaces = DataSet(['danish_genesis_spaces',
    'english_genesis_spaces',
    'finnish_genesis_spaces',
    'german_genesis_spaces',
    'norwegian_genesis_spaces',
    'spanish_genesis_spaces',
    'swedish_genesis_spaces'
], 'test_genesis_spaces')

genesis_uppercase = DataSet(['danish_genesis_uppercase',
    'english_genesis_uppercase',
    'finnish_genesis_uppercase',
    'norwegian_genesis_uppercase',
    'spanish_genesis_uppercase',
    'swedish_genesis_uppercase'
], 'test_genesis_uppercase')

genesis_uppercase_spaces = DataSet(['danish_genesis_uppercase_spaces',
    'english_genesis_uppercase_spaces',
    'finnish_genesis_uppercase_spaces',
    'norwegian_genesis_uppercase_spaces',
    'spanish_genesis_uppercase_spaces',
    'swedish_genesis_uppercase_spaces'
], 'test_genesis_uppercase_spaces')

genesis_no_latin = DataSet(['danish_genesis_nolatin',
    'english_genesis_nolatin',
    'finnish_genesis_nolatin',
    'norwegian_genesis_nolatin',
    'spanish_genesis_nolatin',
    'swedish_genesis_nolatin'
], 'test_genesis_nolatin')

genesis_latin_only = DataSet(['danish_genesis_latinonly',
    'english_genesis_latinonly',
    'finnish_genesis_latinonly',
    'norwegian_genesis_latinonly',
    'spanish_genesis_latinonly',
    'german_genesis_latinonly',
    'swedish_genesis_latinonly'
], 'test_genesis_latinonly')


whole_bible = DataSet(['danish_whole_whole_bible',
    'finnish_whole_whole_bible',
    'norwegian_whole_whole_bible',
    'swedish_whole_whole_bible',
    'polish_whole_whole_bible'
], 'test_whole_bible')

whole_bible_spaces = DataSet(['danish_whole_whole_bible_spaces',
    'finnish_whole_whole_bible_spaces',
    'norwegian_whole_whole_bible_spaces',
    'swedish_whole_whole_bible_spaces',
    'polish_whole_whole_bible_spaces'
], 'test_whole_bible_spaces')

whole_bible_only_nonlatin = DataSet(['danish_whole_whole_bible_only_nonlatin',
    'finnish_whole_whole_bible_only_nonlatin',
    'norwegian_whole_whole_bible_only_nonlatin',
    'swedish_whole_whole_bible_only_nonlatin',
    'polish_whole_whole_bible_only_nonlatin'
], 'test_whole_bible_only_nonlatin')