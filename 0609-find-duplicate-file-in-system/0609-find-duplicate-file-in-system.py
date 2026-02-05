class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = {}
        for folder in paths:
            whitespace = folder.index(" ")
            root_path = folder[:whitespace]
            files = folder[whitespace + 1:].split()
            for file in files:
                content = file[file.index('(') + 1: -1]
                content_map[content] = content_map.get(content, []) + [root_path+ "/" + (file[:file.index("(")])]
        res = []
        for i in content_map:
            if len(content_map[i]) > 1:
                res.append(content_map[i])
        return res
                
        