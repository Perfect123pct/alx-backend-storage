#!/usr/bin/env python3
"""
Module to update topics of a school document based on the name.
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates topics of a school document based on the name.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of topics approached in the school.

    Returns:
        None
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})

if __name__ == "__main__":
    # Example usage
    from pymongo import MongoClient

    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Access the desired collection
    school_collection = client.my_db.school

    # Update topics for a school
    update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])

    # Display all schools after update
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

    # Update topics for the same school with different topics
    update_topics(school_collection, "Holberton school", ["iOS"])

    # Display all schools after the second update
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

