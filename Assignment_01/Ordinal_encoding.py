import pandas as pd
data = {
    'Difficulty' : ['Easy' , 'Hard' , 'Medium' ,'Hard' , 'Medium' , 'Medium']
} 
df = pd.DataFrame(data)
encoding = {'Easy':1 , 'Medium':2, 'Hard':3} 
df['Encoded value'] = [encoding[x] for x in df['Difficulty']]  

print( df)