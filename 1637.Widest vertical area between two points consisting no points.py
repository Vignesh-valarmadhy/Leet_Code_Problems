
# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

# Note that points on the edge of a vertical area are not considered included in the area.



class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        l=[]
        for i in range(len(points)):
            l.append(points[i][0])
        l.sort()
        if(len(l)==0 or len(l)==1):
            return 0
        c=0
        for i in range(len(l)-1,0,-1):
            d=l[i]-l[i-1]
            if(c<d):
                c=d
        return c