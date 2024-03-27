#!/usr/bin/env python3
"""
Module to retrieve schools having a specific topic.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Retrieves the list of schools having a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of school documents matching the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))

if __name__ == "__main__":
    # Example usage
    from pymongo import MongoClient

    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Access the desired collection
    school_collection = client.my_db.school

    # Define sample schools with topics
    j_schools = [
        {'name': "Holberton school", 'topics': ["Algo", "C", "Python", "React"]},
        {'name': "UCSF", 'topics': ["Algo", "MongoDB"]},
        {'name': "UCLA", 'topics': ["C", "Python"]},
        {'name': "UCSD", 'topics': ["Cassandra"]},
        {'name': "Stanford", 'topics': ["C", "React", "Javascript"]}
    ]

    # Insert sample schools into the collection
    for j_school in j_schools:
        insert_school(school_collection, **j_school)

    # Get schools having the topic "Python"
    schools = schools_by_topic(school_collection, "Python")

    # Display the schools having the topic "Python"
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

