import unittest
from process_tweets import clean_line, get_tweet_text, read_stopwords, process_tweet_text, process_tweet_file, write_words

class TestProcessTweets(unittest.TestCase):

    def test_clean_line(self):
        # Test clean_line function with different input cases
        self.assertEqual(clean_line("This is a #hashtag!, this a is a Number123  @userName"),
                         "this is a #hashtag this a is a number  @username")
        self.assertEqual(clean_line("Hello! @world #example"), "hello @world #example")
        self.assertEqual(clean_line("123 @456 #789"), " @ #")
        self.assertEqual(clean_line(""), "")

    def test_get_tweet_text(self):
        # Test get_tweet_text function with different input cases
        self.assertEqual(get_tweet_text("Twitter,Thank you!,11-15-2017 10:58:18,96,433,false,9307"),
                         "Thank you!")
        self.assertEqual(get_tweet_text("John,Doe,2021-01-01,10,5,false,12345"), "Doe")
        self.assertEqual(get_tweet_text("ABC,Hello!,2021-01-01,0,0,true,54321"), "Hello!")

    def test_read_stopwords(self):
        # Test read_stopwords function to ensure the stopwords are correctly read from the file
        stopwords = read_stopwords()
        self.assertIn("and", stopwords)
        self.assertIn("the", stopwords)
        self.assertIn("is", stopwords)
        self.assertIn("at", stopwords)

    def test_process_tweet_text(self):
        # Test process_tweet_text function with different input cases
        self.assertEqual(process_tweet_text("this is a #hashtag this a is a number  @username"),
                         ['#hashtag', 'number', '@username'])
        self.assertEqual(process_tweet_text("I like #Python and @programming!"),
                         ['like', '#python', '@programming'])
        self.assertEqual(process_tweet_text(""), [])

    # Since process_tweet_file function reads from an external file,
    # you can create some test files with sample tweet data to test this function.
    # Then, run the function and compare the output with expected results.

    # The write_words function simply writes data to a file and doesn't have complex logic.
    # You can use the process_tweet_file function to generate the word_freqs data,
    # and then test whether the write_words function writes the data correctly.

if __name__ == '__main__':
    unittest.main()
