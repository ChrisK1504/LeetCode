class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_msg = ""
        for i in strs:
            encoded_msg += i
            encoded_msg += "|"
        print(encoded_msg)
        return encoded_msg

    def decode(self, s: str) -> List[str]:
        decoded_msg = s.split("|")
        return decoded_msg[:-1]