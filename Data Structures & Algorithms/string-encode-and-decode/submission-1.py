class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            word_size = len(s)
            encoded_str += f"{word_size}#" + s

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_arr = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            word_size = int(s[i:j])
            decoded_arr.append(s[j + 1 : j + 1 + word_size])
            i = j + 1 + word_size

        return decoded_arr