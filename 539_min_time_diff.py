class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i,time in enumerate(timePoints):
            hours,minutes=time.split(":")
            min_past_midnight=int(hours)*60+int(minutes)
            timePoints[i]=min_past_midnight
        timePoints.sort()
        res=1440+timePoints[0]-timePoints[-1]
        for i in range(1,len(timePoints)):
            res=min(res,timePoints[i]-timePoints[i-1])
        return res