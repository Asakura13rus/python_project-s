with open('test_file.txt', 'w', encoding='utf-8') as file:
    file.write(
        "It's a text for task. Найти везде. Используйте его для самопроверки. Успехов в решении задачи. TEXT TEXT TEXT")


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()

                for p in punctuation:
                    text = text.replace(p, '')

                words = text.split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1

        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            result[file_name] = words.count(word)

        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))