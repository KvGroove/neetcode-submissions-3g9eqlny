class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        s_letters = {s.count(letter)*letter for letter in alphabet if s.count(letter) > 0}
        t_letters = {t.count(letter)*letter for letter in alphabet if t.count(letter) > 0}
        return s_letters == t_letters