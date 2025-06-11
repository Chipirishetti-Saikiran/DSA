class Solution(object):
    def longestCommonPrefix(self, words):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=words[0]
        for i in words[1:]:
            while not i.startswith(prefix):
                prefix=prefix[:-1]
                if not prefix:
                    return ""
        return prefix