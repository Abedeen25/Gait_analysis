import Train
import Test

Train.Train(10)
cc = 0
"""
for i in range(1,20):
    userID, userName = Test.Test('action_'+str(i*2)+'.txt')
    if(userID[0][0] == i):
        cc = cc + 1
"""
print(Test.Test('joints_s01_e01.txt'))
# print(cc)

