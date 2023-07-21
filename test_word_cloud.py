import unittest
from process_tweets import clean_line, get_tweet_text, read_stopwords, process_tweet_text, process_tweet_file, print_statistics, write_words

class TestProcessTweets(unittest.TestCase):

    def test_clean_line(self):
        self.assertEqual(clean_line("This is a #hashtag!, this a is a Number123  @userName"),
                         'this is a #hashtag this a is a number  @username')
        self.assertEqual(clean_line("#hashtag!"), '#hashtag')

    def test_get_tweet_text(self):
        self.assertEqual(get_tweet_text("Twitter,Thank you!,11-15-2017 10:58:18,96,433,false,9307"),
                         'Thank you!')
        self.assertEqual(get_tweet_text("Twitter,,11-15-2017 10:58:18,96,433,false,9307"), '')

    def test_read_stopwords(self):
        stopwords = read_stopwords()
        self.assertTrue(isinstance(stopwords, set))
        self.assertTrue(len(stopwords) > 0)
        self.assertIn("the", stopwords)
        self.assertIn("and", stopwords)

    def test_process_tweet_text(self):
        text = "this is a #hashtag this a is a number  @username"
        result = process_tweet_text(text)
        self.assertEqual(result, ['#hashtag', 'number', '@username'])

    def test_process_tweet_file(self):
        file_name = 'tweets_test.txt'  # Create a test file with sample tweet texts for testing
        with open(file_name, 'w') as test_file:
            test_file.write("Twitter,Thank you!,11-15-2017 10:58:18,96,433,false,9307\n")
            test_file.write("Twitter,Great day!,11-16-2017 11:11:11,100,500,true,9308\n")
            test_file.write("Twitter,Hello world!,11-17-2017 12:12:12,50,300,false,9309\n")

        word_freqs = process_tweet_file(file_name)
        self.assertEqual(word_freqs['thank'], 1)
        self.assertEqual(word_freqs['great'], 1)
        self.assertEqual(word_freqs['hello'], 1)
        self.assertEqual(word_freqs['world'], 1)

    def test_print_statistics(self):
        word_freqs = {'thank': 1, 'great': 1, 'hello': 2, 'world': 2}
        self.assertIsNone(print_statistics(word_freqs))

    def test_write_words(self):
        word_freqs = {'thank': 1, 'great': 1, 'hello': 2, 'world': 2}
        file_name = 'words_test.txt'  # Create a test file for writing the word frequencies
        write_words(word_freqs, file_name)

        with open(file_name, 'r') as test_file:
            lines = test_file.readlines()
            self.assertEqual(len(lines), 4)
            self.assertIn("thank 1\n", lines)
            self.assertIn("great 1\n", lines)
            self.assertIn("hello 2\n", lines)
            self.assertIn("world 2\n", lines)
    
        # Clean up the test files
        import os
        os.remove(file_name)
        os.remove('tweets_test.txt')

if __name__ == '__main__':
    unittest.main()
