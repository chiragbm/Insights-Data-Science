'''
Created on Oct 29, 2017

@author: chiragm
'''
import heapq

class Receiver:
        
        def __init__(self):
            self.total_transactions = 0
            self.total_contributions = 0
            self.mnHeap = []
            self.mxHeap = []
            self.median = 0
        
        def getMedian(self):
            
            if(len(self.mnHeap) == 0 and len(self.mxHeap) == 0): return 0
            elif(len(self.mnHeap) > len(self.mxHeap)):    return self.mnHeap[0]
            else: return (self.mnHeap[0] + (-1)*self.mxHeap[0]) / float(2)
        
        def insertVal(self, value):
            
            self.total_transactions+=1
            self.total_contributions+=value
            
            med = self.getMedian()
            if value > med:
                heapq.heappush(self.mnHeap, value)
            else:
                heapq.heappush(self.mxHeap, value*-1)
            
            if len(self.mxHeap) > len(self.mnHeap):
                mx = (-1) * heapq.heappop(self.mxHeap)
                heapq.heappush(self.mnHeap, mx)
            elif(len(self.mnHeap) - len(self.mxHeap) > 1):
                mn = heapq.heappop(self.mnHeap)
                heapq.heappush(self.mxHeap, (-1)*mn)
            
            med = self.getMedian()
            int_med = int(med)
            if(med - int_med >=0.5):
                self.median = int_med + 1
            else:
                self.median = int_med
            
            
        
