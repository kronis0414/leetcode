class Solution:
    def angleClock(self, hour, minutes):
        if hour == 12:
            hour = 0
            
        deg1 = hour * 30 + minutes * 0.5
        deg2 = minutes * 6
        
        return min(360-abs(deg1-deg2), abs(deg1-deg2))
        
#從順時針方向, 分成時針和分針從0開始的角度
#分針因為有60個刻度, 所以一分鐘等於360/60=6 degree
#時針因為有12個小時, 所以一小時等於360/12=30 degree, 又因為也會隨著分針跑, 所以當分鐘移動一分鐘則時針移動30/60=0.5
#最後2者相減找最小