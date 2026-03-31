class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        from collections import defaultdict

        groups = defaultdict(list)
        for word in words:
            letters = [0] * 26

            for letter in word:
                letters[ord(letter) - ord("a")] += 1

            key = tuple(letters)
            groups[key].append(word)

        return list(groups.values())


