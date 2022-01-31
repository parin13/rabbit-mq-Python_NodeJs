from distutils.log import error
import json
from json.tool import main
import pika



exchange_name = 'backend_service_node_3'
queue_name ='authorization_node_3'



def local_queue():
    connection = None
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.exchange_declare(
            exchange = exchange_name,
            exchange_type = 'direct',
            durable=True
        )
        channel.queue_declare(
            queue = queue_name,
            durable=True
        )

        message_payload = {
            "namespace":"customer.user.loggedin",
            "model":{
                "id":2307,
                "email":"parin.r@xgmail.com",
                "phone":"4555446755",
                "firstName":"PARIN",
                "lastName":"R",
                "streetAddress":"1 / 92a Mona Vale Road",
                "city":"WA",
                "zip":"6803",
                "state":"NSW",
                "country":None,
                "gender":None,
                "profileImage":None,
                "authKey":"",
                "passwordHash":"hCWxb0pnlBO6CpWokDnip2EzN2I0ZTRhZTIwNDJjZWEwZTI0NTQ4YTQ0ZTg2ODBiNTE3ZmFjNzY4ZGZjNWU1NTE4NWUzMGM3MjdmNGMwM2Ni0FFaPaYcSEv/dHZkuUKGkqMb1y5SAe8y8mA4Tw58qw==",
            },
            "token":"eyJhbGciSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1rVkZPVUkyUlVSR05VVXhRVGN4UlRGRE1ERkNPREF5TVRZM05VSTRNa1V4UXpsRE9FUTJOdyJ9.eyJpc3MiOiJodHRwczovL3NhYXMtZnJhbWUuYXUuYXV0aDAuY29tLyIsInN1YiI6IndscWI2SnNvWXhlOTJVUlRabDhlT2Z6OTVVNjAzdk14QGNsaWVudHMiLCJhdWQiOiJkZWZhdWx0LWFwaSIsImlhdCI6MTYzODI1NzI3MCwiZXhwIjoxNjM4MzQzNjcwLCJhenAiOiJ3bHFiNkpzb1l4ZTkyVVJUWmw4ZU9mejk1VTYwM3ZNeCIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyJ9.sP7zTq9N1LY3mWi1Ho3mbr11ciQT5otzZlEVdvNyXvzLGnW-bnTFOvvQrYGa1Nm-GPJR8pZ8IaP4I0FMb9hXASPahDZ8QQ5odhmzngpEMxbmWP7DE3DMmyBC5bh-m1VDmMG0RkPPWzqylf2Szcfl7uGN4mxTTxQ7pW8GJ_CdUfj7qMM8Gxb2j7kq0oNwnr_VJqa5bjBHeqJE0DioWnqvX7PD4LUR2HQe75UWQ7G3afPx39NHDUsrMljlp0yi76cksRlbuv6_TXfZLmR6r5H5VJYHB9OHFs1eWAhHnehWoJdPy0QQWm8iezZ3MmEw1OOqaf7r3VV1Y2ahJAg"
        }

        channel.basic_publish(
            exchange=exchange_name,
            routing_key='customer.user.loggedin',
            body = json.dumps(message_payload)
        )

        print("Published Auth Message Sucessfully")

    except Exception as e:
        print(e)
        print ("Into exception") 
    finally:
        connection.close()



if __name__ == '__main__':
    local_queue()
 