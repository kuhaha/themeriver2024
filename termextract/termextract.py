import numpy as np

from collections import defaultdict
"""
LR: Left/Right Collocation
PP: PerPlexity
cn: compound noun
ln, rn: left/right collocation frequency
ldn, rdn: left/right collocation varieties　
"""
class LRValue:
    def __init__(self):
        self.__init_stat()

    def __init_stat(self):
        self._ldn = defaultdict(lambda: defaultdict(int))
        self._rdn = defaultdict(lambda: defaultdict(int))
        self._compound_noun = defaultdict(int)

    @property
    def compound_noun(self):       
        return self._compound_noun

    @staticmethod
    def ngram(words, n=2):
        return list(zip(*(words[i:] for i in range(n))))

    def fit(self, compound_nouns):
        self.__init_stat()
        for compound_noun in compound_nouns:
            self._compound_noun[" ".join(compound_noun)] += 1
            for bigram in self.ngram(compound_noun, n=2):
                self.update(bigram)
        return self

    def transform(self, compound_nouns, mode=1):
        # return {" ".join(cn): self.FLR(cn) for cn in compound_nouns}
        f = lambda cn: self.FLR(cn) if mode==1 else self.LR(cn) if mode==2 else self.PP(cn)
        return {" ".join(cn): f(cn) for cn in compound_nouns}

    def fit_transform(self, compound_nouns, mode=1):
        return self.fit(compound_nouns).transform(compound_nouns, mode)

    def FLR(self, compound_noun):
        return self._compound_noun[" ".join(compound_noun)] * self.LR(compound_noun)

    def LR(self, compound_noun):
        a = np.array([(self.ln(n) + 1) * (self.rn(n) + 1) for n in compound_noun])
        return np.power(a.cumprod()[-1], 1/(2 * len(compound_noun)))

    def PP(self, compound_noun):
        a = np.array([(self.ldn(n) + 1) * (self.rdn(n) + 1) for n in compound_noun])
        return np.power(a.cumprod()[-1], 1/(2 * len(compound_noun)))
           
    def update(self, bigram):
        self._ldn[bigram[1]][bigram[0]] += 1
        self._rdn[bigram[0]][bigram[1]] += 1

    def ln(self, word):
        return sum(self._ldn[word].values())

    def rn(self, word):
        return sum(self._rdn[word].values())

    def ldn(self, word):
        return len(self._ldn[word])

    def rdn(self, word):
        return len(self._rdn[word])
        