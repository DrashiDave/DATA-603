from mrjob.job import MRJob
import re
import enchant

class InvalidWordFrequencyAnalyzer(MRJob):

    def __init__(self, *args, **kwargs):
        super(InvalidWordFrequencyAnalyzer, self).__init__(*args, **kwargs)
        self.english_dict = enchant.Dict("en_US")

    def mapper(self, _, line):
        words = self.tokenize(line.lower())
        for word in words:
            if self.is_valid_word(word):
                yield (word, 1)

    def reducer(self, word, counts):
        yield (word, sum(counts))

    def tokenize(self, text):
        return re.findall(r'\b\w+\b', text)

    def is_valid_word(self, word):
        return len(word) > 1 and not self.english_dict.check(word)

if __name__ == '__main__':
    InvalidWordFrequencyAnalyzer.run()
