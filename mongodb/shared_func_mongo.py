import requests
import json
import os
from pymongo import MongoClient

def create_folder_if_not_exists(folder_name):
    """
    Create a folder if it does not exist.

    :param folder_name: The name of the folder to create.
    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created.")
    else:
        print(f"Folder '{folder_name}' already exists.")

def get_data_with_request(url):
    # Loop through each collection and save the data as a JSON file
    response = requests.get(url)
    # Check if the request was successful
    try:
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            return data
    except:
        print(f"Failed to retrieve {collection_name}: Status code {response.status_code}")
        print(f"url: {url}")
        return None

def save_the_data_in_a_json_file(data, file_name ):
    try:
        #Save the data to a file
        print("saving:",file_name)
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("error", e)

def create_the_nobel_database():
    download_the_nobelprize_dataset()

    prizes = load_the_dataset("dataset/nobelPrizes.json")
    laureates = load_the_dataset("dataset/laureates.json")

    upload_data_into_mongo(
            document=prizes['nobelPrizes'],
            collection_name="prizes",
            db_name="nobel"
            )

    upload_data_into_mongo(
            document=laureates["laureates"],
            collection_name="laureates",
            db_name="nobel"
            )

def download_the_nobelprize_dataset():
    create_folder_if_not_exists("dataset")

    # Define the base URL of the Nobel Prize API
    #src: https://www.nobelprize.org/

    version = "2.1"
    api_base_url = f"https://api.nobelprize.org/{version}/"
    for collection_name in ["nobelPrizes", "laureates"]:
        # Make a request to the API
        url = f"{api_base_url}{collection_name}"
        file_name = f"dataset/{collection_name}.json"
        data = get_data_with_request(url)
        save_the_data_in_a_json_file(data, file_name)

def load_the_dataset(file_name):
    print("loading:",file_name)
    with open (file_name, "r") as outfile:
        data = json.load(outfile)
    return data

def connect_to_mongodb(uri='mongodb://172.19.0.2:27017/', username = "admin", password="admin"):
    # Replace 'localhost' with the IP address or hostname of your Docker host if necessary
    client = MongoClient(uri,
                         username=username,
                         password=password,
                         authSource='admin'
                         )
    print("client:",client)
    return client
    

def upload_data_into_mongo(document, collection_name, db_name="nobel"):
    """
    Load a list of documents into a specified MongoDB collection.

    :param document: The list of documents (dictionaries) to insert.
    :param collection_name: The name of the collection to insert documents into.
    :param db_name: The name of the database where the collection exists or will be created.
    """
    try:
        client = connect_to_mongodb()
        db = client[db_name]
        collection = db[collection_name]

        # Insert the documents into the collection
        insert_result = collection.insert_many(document)
        print(f"Inserted {len(insert_result.inserted_ids)} documents into collection '{collection_name}'")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection to MongoDB
        client.close()

            
