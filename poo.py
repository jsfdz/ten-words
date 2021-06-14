class CountWords:
    file = ''
    dictionary = {}

    def count(self):
        self.file = input('Ingresa el nombre del archivo sin la extención:')
        try:
            text = open(f'{self.file}.txt', mode='r')
        except:
            print(f'No se encuentra el archivo con ese nombre')
            quit()

        words = text.read()
        wordsInterator = words.lower().split()

        for word in wordsInterator:
            self.dictionary[word] = self.dictionary.get(word, 0) + 1

        tmp = list()
        for key, value in self.dictionary.items():
            tmp.append((value, key))

        tmp = sorted(tmp, reverse=True)
        return tmp[:10]


tenWords = CountWords()
print(tenWords.count())
