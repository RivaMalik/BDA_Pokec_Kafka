from time import sleep
from json import dumps
from kafka import KafkaProducer
from data import get_data
from time import sleep


def json_serializer(data):
    return dumps(data).encode('utf-8')


producer=KafkaProducer(bootstrap_servers=['localhost:9092'],
                       value_serializer=json_serializer)


if __name__ == "__main__":
    for i in range(3):

         print(" i val ", i)
         p_data=get_data(i)
         print("This is the data in producer ",p_data)
         producer.send("user_language_topic", p_data)
         sleep(100)

