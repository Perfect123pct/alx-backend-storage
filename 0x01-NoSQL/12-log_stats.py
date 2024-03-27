#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

def get_logs_count(mongo_collection):
    """Get the number of logs in the collection."""
    return mongo_collection.count_documents({})

def get_method_counts(mongo_collection):
    """Get counts of different HTTP methods."""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    counts = {}
    for method in methods:
        counts[method] = mongo_collection.count_documents({"method": method})
    return counts

def get_status_check_count(mongo_collection):
    """Get the number of logs with method=GET and path=/status."""
    return mongo_collection.count_documents({"method": "GET", "path": "/status"})

if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Get logs count
    logs_count = get_logs_count(nginx_collection)
    print(f"{logs_count} logs")

    # Get method counts
    method_counts = get_method_counts(nginx_collection)
    print("Methods:")
    for method, count in method_counts.items():
        print(f"    method {method}: {count}")

    # Get status check count
    status_check_count = get_status_check_count(nginx_collection)
    print(f"{status_check_count} status check")

