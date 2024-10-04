from mrjob.job import MRJob
import re

class CountWords(MRJob):
    def mapper(self, _, line):
        words = self.tokenize(line)
        for word in words:
            if word and len(word) > 0:
                yield (word, 1)

    def reducer(self, word, counts):
        total_count = sum(counts)
        yield (word, total_count)

    def tokenize(self, line):
        return re.findall(r'\b[a-z]+\b', line.lower())

if __name__ == '__main__':
    CountWords.run()
