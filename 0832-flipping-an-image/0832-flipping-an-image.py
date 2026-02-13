class Solution(object):
    def flipAndInvertImage(self, image):
        for i in image:
            i.reverse()
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
        return image
        

