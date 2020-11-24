from utilities.database_utilities import create_database
from utilities.database_utilities import save_words_to_database


class TestDBUtils:
    def test_create_database(self):
        results = create_database("word.db")
        assert results == True

    def test_save_words_to_database(self):
        results = save_words_to_database("word.db", ["word1", "word2", "word3"])
        assert results == True
