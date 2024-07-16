#!/usr/bin/env python3
"""
This script provides stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def log_stats():
    """
    Function to print stats about Nginx logs.
    Connects to the MongoDB database, counts the total logs, and prints the
    count of different HTTP methods.
    It also counts and prints the number of logs where method is GET and path
    is "/status".
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    logs_count = nginx_collection.count_documents({})
    print(f"{logs_count} logs")

    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check_count = nginx_collection.\
        count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
