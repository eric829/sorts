def make_list(size=10,max=50):
        from random import randint
        return [randint(1,max) for i in range(size)]

class Many_sort:
    def __init__(self,data):
        self.list = data

    def Insertion_Sort(self):
        
        for i in range(1,len(self.list)):
            compar= self.list[i]
            k = i-1
            while compar < self.list[k] and k>= 0 :
                self.list[k+1] = self.list[k]
                k=k-1
            self.list[k+1] = compar
        return self.list

    def Bubble_Sort(self):
        
        swap_times = len (self.list)-1
        while swap_times > 0:
            for i in range(0,len(self.list)-1):
                if self.list[i] > self.list[i+1]:
                    tmp = self.list[i]
                    self.list[i]=self.list[i+1]
                    self.list[i+1]=tmp
                else:
                    continue
            swap_times = swap_times-1
        return self.list
    
    def Quick_sort(self,data):

        small = []
        large = []

        if len(data)<=1 :
            return data
        else:
            mid = data[0]
            for i in range(1,len(data)):
                if data[i] < mid :
                    small.append(data[i])
                else:
                    large.append(data[i])

        small = self.Quick_sort(small)
        large = self.Quick_sort(large)

        return small+ [mid] + large


    def Merge(self,left,right):
        final = []  # merged
        L_item ,R_item = 0,0

        while L_item< len (left) and R_item< len(right):
            if left[L_item] < right[R_item] :
                final.append(left[L_item])
                L_item +=1
            else :
                left[L_item] > right[R_item] 
                final.append(right[R_item])
                R_item +=1

        if L_item == len(left): 
            final = final + right[R_item:]
        else:
            final = final + left[L_item:]
        return final


    def Merge_sort(self,data):
        if len (data) ==1 :
            return data
        
        left,right = self.Merge_sort(data[:len(data/2)]),self.Merge_sort(data[len(data/2):])

        return Merge(left,right)

        		
    def Binary_sort(self):
        	


        

l = make_list()
k = Many_sort(l)

print l
#print k.Bubble_Sort()
#print k.Insertion_Sort()
#print k.Quick_sort(l)           
print k.Merge_sort(l)   
#print k.Merge()