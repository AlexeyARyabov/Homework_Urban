class WordsFinder:

    def __init__(self, *names):
        self.names = names

    def get_all_words(self):
        all_words = {}
        list_word = []
        del_chars = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.names:
            with open(name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for char in del_chars:
                        line = str(line).replace(char, '')
                    for word in line.split():
                        list_word.append(word)
                all_words.update({name: list_word})
            list_word = []
        return all_words

    def find(self, word):
        word = word.lower()
        find_words = {}
        for name, list_word in WordsFinder.get_all_words(self).items():
            if word in list_word:
                find_words.update({name: list_word.index(word)+1})
        return find_words

    def count(self, word):
        word = word.lower()
        count_words = {}
        for name, list_word in WordsFinder.get_all_words(self).items():
            if word in list_word:
                count_words.update({name: list_word.count(word)})
        return count_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
