#!/usr/bin/env python3
"""
Module to insert a new document into a MongoDB collection based on kwargs.
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection based on kwargs.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        **kwargs: Keyword arguments representing the fields and values of the new document.

    Returns:
        str: The _id of the newly inserted document.
    """
    return str(mongo_collection.insert_one(kwargs).inserted_id)

if __name__ == "__main__":
    # Example usage
    from pymongo import MongoClient

    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Access the desired collection
    school_collection = client.my_db.school

    # Insert a new school document
    new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new_school_id))

    # Display all schools
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('address', "")))

