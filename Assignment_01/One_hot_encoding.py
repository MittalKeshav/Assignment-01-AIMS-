import pandas as pd
data = {
    'Size' : [ 'small' , 'medium' , 'small' , 'large' ]
}
df = pd.DataFrame(data)
category_1 = [] 
for x in df['Size']:
    if x not in category_1:
        category_1.append(x) 
for category_2 in category_1: 
    encoded_column = []
    for x in df['Size']:
        if x ==category_2 :
            encoded_column.append(1) 
        else :    
            encoded_column.append(0)
    df[category_2] = encoded_column  
print(df)     
