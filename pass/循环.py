demo = {
     'AA':'学习',
     'BB':'睡觉',
     'CC':{
         'DD':'吃饭',
         'EE':['梨子','苹果','桃子','西瓜']
    }
}
for i in demo:
    print(demo['CC']['EE'])

