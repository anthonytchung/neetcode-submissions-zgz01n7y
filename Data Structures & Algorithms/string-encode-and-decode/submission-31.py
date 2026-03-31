class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return 
        string = "BREAKER".join(strs)
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        if s is None:
            return []
        elif s == "":
            return [""]
        else:
            return s.split("BREAKER")
