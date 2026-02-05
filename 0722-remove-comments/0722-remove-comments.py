class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        res = []
        in_block = False
        new_line = []
        
        for line in source:
            i = 0
            while i < len(line):
                if in_block:
                    if i + 1 < len(line) and line[i:i+2] == '*/':
                        in_block = False
                        i += 1 
                else:
                    if i + 1 < len(line) and line[i:i+2] == '/*':
                        in_block = True
                        i += 1 
                    elif i + 1 < len(line) and line[i:i+2] == '//':
                        break
                    else:
                        new_line.append(line[i])
                i += 1
            if not in_block and new_line:
                res.append("".join(new_line))
                new_line = [] 
                
        return res