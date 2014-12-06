DATA_DIRECTORY  = '../data/'
LETTER_FILENAME = 'part'

class DataSet():
    def __init__(self, p_train_dirs, p_test_dir):
        self.train = p_train_dirs
        self.test  = p_test_dir

# No spaces, lowercase, all characters, 
genesis1 = DataSet(
    ['danish_genesis1',
    'english_genesis1',
    'finnish_genesis1',
    'german_genesis1',
    'norwegian_genesis1',
    'spanish_genesis1',
    'polish_genesis1',
    'swedish_genesis1'
    ], 'test_genesis1')

# Spaces present, lowercase, all characters, 
genesis2 = DataSet(
    ['danish_genesis2',
    'english_genesis2',
    'finnish_genesis2',
    'german_genesis2',
    'norwegian_genesis2',
    'spanish_genesis2',
    'polish_genesis2',
    'swedish_genesis2'
    ], 'test_genesis2')

# Spaces present, lowercase, latin characters, non-latin removed 
genesis3 = DataSet(
    ['danish_genesis3',
    'english_genesis3',
    'finnish_genesis3',
    'german_genesis3',
    'norwegian_genesis3',
    'spanish_genesis3',
    'polish_genesis3',
    'swedish_genesis3'
    ], 'test_genesis3')

# Spaces present, lowercase, non-latin characters, latin removed 
genesis4 = DataSet(
    ['danish_genesis4',
    'english_genesis4',
    'finnish_genesis4',
    'german_genesis4',
    'norwegian_genesis4',
    'spanish_genesis4',
    'polish_genesis4',
    'swedish_genesis4'
    ], 'test_genesis4')

# No spaces present, lowercase, non-latin characters, latin removed 
genesis5 = DataSet(
    ['danish_genesis5',
    'english_genesis5',
    'finnish_genesis5',
    'german_genesis5',
    'norwegian_genesis5',
    'spanish_genesis5',
    'polish_genesis5',
    'swedish_genesis5'
    ], 'test_genesis5')

# Spaces present, all characters, mixed-case
genesis6 = DataSet(
    ['danish_genesis6',
    'english_genesis6',
    'finnish_genesis6',
    'german_genesis6',
    'norwegian_genesis6',
    'spanish_genesis6',
    'polish_genesis6',
    'swedish_genesis6'
    ], 'test_genesis6')

# Spaces present, all characters, mixed-case, full Bible used
full1 = DataSet(
    ['swedish_whole_full1',
    'polish_whole_full1',
    'norwegian_whole_full1',
    'english_whole_full1',
    'finnish_whole_full1',
    'danish_whole_full1',
    ], 'test_full1')

# Spaces removed, all characters, lowercase, full Bible used
full2 = DataSet(
    ['swedish_whole_full2',
    'polish_whole_full2',
    'norwegian_whole_full2',
    'english_whole_full2',
    'finnish_whole_full2',
    'danish_whole_full2',
    ], 'test_full2')

# Spaces removed, Latin characters only, lowercase, full Bible used
full3 = DataSet(
    ['swedish_whole_full3',
    'polish_whole_full3',
    'norwegian_whole_full3',
    'english_whole_full3',
    'finnish_whole_full3',
    'danish_whole_full3',
    ], 'test_full3')

# Spaces removed, Non-Latin characters only, lowercase, wiktionary
dict1 = DataSet(
    ['danish_dict_dict1',
    'swedish_dict_dict1',
    'norwegian_dict_dict1',
    'finnish_dict_dict1',
    'italian_dict_dict1'
    ], 'test_dict1')

# Spaces removed, all characters, lowercase, wiktionary
dict2 = DataSet(
    ['danish_dict_dict2',
    'swedish_dict_dict2',
    'norwegian_dict_dict2',
    'finnish_dict_dict2',
    'italian_dict_dict2'
    ], 'test_dict2')

# Spaces removed, all characters, lowercase, wikipedia
wiki1 = DataSet(
    ['swedish_wiki_wiki1',
    'norwegian_wiki_wiki1',
    'finnish_wiki_wiki1',
    'danish_wiki_wiki1',
    'italian_wiki_wiki1'
    ], 'test_wiki1')

# Spaces removed, only non-Latin, lowercase, wikipedia
wiki2 = DataSet(
    ['swedish_wiki_wiki2',
    'norwegian_wiki_wiki2',
    'finnish_wiki_wiki2',
    'danish_wiki_wiki2',
    'italian_wiki_wiki2'
    ], 'test_wiki2')

# Spaces removed, only Latin characters, lowercase, wikipedia
wiki3 = DataSet(
    ['swedish_wiki_wiki3',
    'norwegian_wiki_wiki3',
    'finnish_wiki_wiki3',
    'danish_wiki_wiki3',
    'italian_wiki_wiki3'
    ], 'test_wiki3')

# Spaces removed, only Latin characters, lowercase, wikipedia
wiki_short = DataSet(
    ['swedish_whole_wiki3',
    'norwegian_whole_wiki3',
    'finnish_whole_wiki3',
    'danish_whole_wiki3'
    ], 'test_short_wiki3')