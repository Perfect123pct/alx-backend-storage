#!/usr/bin/env python3
"""
Module to list all documents in a MongoDB collection.
"""

def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.

    Returns:
        list: A list containing all documents in the collection.
    """
    return list(mongo_collection.find())

if __name__ == "__main__":
    # Example usage
    from pymongo import MongoClient

    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Access the desired collection
    school_collection = client.my_db.school

    # Get all documents from the collection
    schools = list_all(school_collection)

    # Print the details of each document
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))

