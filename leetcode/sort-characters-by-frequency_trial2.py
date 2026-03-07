class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        
        items = []
        for ch in freq:
            items.append([ch, freq[ch]])

        
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if items[j][1] > items[i][1]:
                    items[i], items[j] = items[j], items[i]

        
        result = ""
        for pair in items:
            char = pair[0]
            count = pair[1]
            for k in range(count):
                result += char

        return result
