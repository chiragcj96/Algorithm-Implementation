class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)      # split will only work ones, can be written as log.split(" ", 1)
                                                        # dig3 8 1 5 1 -> _id=dig3, rest=8 1 5 1
            return (0, rest, _id) if rest[0].isalpha() else (1, )   # checks for isalpha(), assigns it a 0 key and 
                                                                    # returns sorted first acc to rest value and 
                                                                    # second to _id, otherwise it assigns 1 key and returns as it is
        return sorted(logs, key=get_key)            # sort acc to the key