class Solution(object):
    def imageSmoother(self, img):
        res = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                tot = 0
                count = 0
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if k >= 0 and l >= 0 and k < len(img) and l < len(img[0]):
                            tot += img[k][l]
                            count += 1
                res[i][j] = tot // count
        return res
            
