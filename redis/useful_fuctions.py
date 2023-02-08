import pandas as pd
import json
import redis

def clear_redis_database():
    # Connect to the Redis database
    redis_client = redis.Redis(host='localhost', port=6379)

    # Delete all keys in the database
    redis_client.flushall()

    # Confirm that the database is now empty
    print("Redis database cleared successfully.")

def store_data_in_redis(key,data):
    # Connect to Redis
    redis_host = "localhost"
    redis_port = 6379
    r = redis.Redis(host=redis_host, port=redis_port)
    r.set("key", json.dumps(data))

def get_data_from_redis():
    # Connect to Redis
    redis_host = "localhost"
    redis_port = 6379
    r = redis.Redis(host=redis_host, port=redis_port)

    # Retrieve the data from Redis
    data = r.get("data").decode()

    return json.loads(data)

def json_to_dataframe(json_string, key):
    data_dict = json.loads(json_string)
    data = data_dict[key]
    df = pd.DataFrame.from_dict(data, orient='index')
    return df
