class Solution(object):
    def totalFruit(self, fruits):
        one=two=-1
        count=cur_max=maxii=0
        for i in range(len(fruits)):
            fruit=fruits[i]
            if (fruit == one or fruit == two):
                cur_max+=1
            else:
                cur_max=count+1
            if (fruit == two):
                count+=1
            else:
                count=1
                one=two
                two=fruit
            maxii=max(maxii,cur_max)
        return maxii