class Solution:

    encoding_character = '@'

    @staticmethod
    def decode_next_string(string: str, start_pos: int) -> str:
        # Decode length
        length = 0

        while string[start_pos: start_pos + len(Solution.encoding_character)] != Solution.encoding_character:
            digit = int(string[start_pos])
            length = length * 10 + digit

            start_pos += 1

        # Return decoded string
        str_start_idx = start_pos + len(Solution.encoding_character) # Index next to @
        str_end_idx = str_start_idx + length - 1

        decoded_string = string[str_start_idx: str_end_idx + 1]

        return decoded_string

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for string in strs:
            encoded_string += str(len(string)) + Solution.encoding_character + string

        return encoded_string


    def decode(self, s: str) -> List[str]:
        strs = []
        s_len = len(s)

        next_str_len_idx = 0
        while next_str_len_idx < s_len:
            decoded_string = Solution.decode_next_string(s, next_str_len_idx)
    
            strs.append(decoded_string)

            next_str_len_idx += len(str(len(decoded_string))) + len(Solution.encoding_character) + len(decoded_string)

        return strs