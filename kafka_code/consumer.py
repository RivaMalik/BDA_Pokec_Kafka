import json
import plotly.express as px
import pandas as pd
from kafka import KafkaConsumer
from collections import Counter


def processReceivedDataFrame(df):
    df['user_category'] = ""
    df['user_category'].mask(df['lang_count'] == 0, "No Response", inplace=True)
    df['user_category'].mask(df['lang_count'] == 1, "Unilingual", inplace=True)
    df['user_category'].mask(df['lang_count'] == 2, "Bilingual", inplace=True)
    df['user_category'].mask(df['lang_count'] == 3, "Trilingual", inplace=True)
    df['user_category'].mask(df['lang_count'] == 4, "Quadrilingual", inplace=True)
    df['user_category'].mask(df['lang_count'] >= 5, "Multilingual", inplace=True)

    vals = Counter(df['user_category'])
    new_df = pd.DataFrame(list(vals.items()), columns=['user_category', 'count'])

    return new_df


def visualizeData(df):

    fig = px.pie(df, values='count', names='user_category', title='Population of European continent')
    fig.show()


if __name__ == "__main__":
    print("in consumer")
    consumer=KafkaConsumer(
            'user_language_topic',
            bootstrap_servers = ['localhost:9092'],
            auto_offset_reset='earliest',
            group_id = "my-group"
    )

    print("starting cons")
    for msg in consumer:
        data_received=json.loads(msg.value)

        df_rec= pd.DataFrame(eval(data_received))
        processed_df=processReceivedDataFrame(df_rec)
        #print(processed_df)
        processed_df.to_csv("kafka_result_data.csv")
        visualizeData(processed_df)



