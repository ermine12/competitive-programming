class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0   
        j = 0   

        while i < len(chars):
            letter = chars[i]
            count = 0

            
            while i < len(chars) and chars[i] == letter:
                i += 1
                count += 1

            
            chars[j] = letter
            j += 1

            
            if count > 1:
                for c in str(count):
                    chars[j] = c
                    j += 1

        return j
