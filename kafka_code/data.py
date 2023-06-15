from faker import Faker
import pandas as pd

df_complete=pd.read_csv("asg3_data.csv")
df_chunk1=df_complete.head(100)
df_chunk2=df_complete.head(200)
df_chunk3=df_complete.head(300)



def get_data(chunk_number):
    print("this is chunk number ",chunk_number)
    js_format = ""
    if chunk_number==0:
        js_format = df_chunk1.to_json(orient='records')

    elif chunk_number==1:
        js_format = df_chunk2.to_json(orient='records')

    elif chunk_number==2:
        js_format = df_chunk3.to_json(orient='records')

    return js_format


