#def dif(J, S):
    #x = set(J)
    #count = 0
    #for y in S:
        #if y in x:
            #count += 1
    #return count
#J = "ab"
#S = "aabbccd"
#result = dif(J, S)
#print(result)

#def dif(candidates, target):
    #candidates.sort()
    #result = []
    #def dif2(x, y, z):
        #if y == 0:
            #result.append(x[:])
            #return
        #if y < 0:
            #return
        #for i in range(z, len(candidates)):
            #if i > z and candidates[i] == candidates[i - 1]:
                #continue
            #dif2(x + [candidates[i]], y - candidates[i], i + 1)

    #dif2([], target, 0)
    #return result

#candidates = [10, 1, 2, 7, 6, 1, 5]
#target = 8
#print(dif(candidates, target))

#def dif(nums) :
    #x = set()
    #for i in nums:
        #if i in x:
            #return True
        #x.add(i)
    #return False
#nums1 = [1, 2, 3, 1]
#print(dif(nums1))



