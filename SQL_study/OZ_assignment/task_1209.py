from pymongo import MongoClient
from datetime import datetime

def insert_data():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local
    
    # 문제 1
    # genre 데이터 삽입
    query = {}
    update = {"$set": {"genre": "fantasy"}}
    db.books.update_many(query, update)

    # 문제 2
def calculate_average_ratings(db):
    movies_collection = db.movies
    pipeline = [
        {"$group": {"_id": "$director", "average_rating": {"$avg": "$rating"}}},
        {"$sort": {"average_rating": -1}}
    ]

    results = movies_collection.aggregate(pipeline)
    for result in results:
        print(result)

    # 문제 3
def calculate_average_ratings(db):
    movies_collection = db.movies
    pipeline = [
        {"$group": {"_id": "$director", "average_rating": {"$avg": "$rating"}}},
        {"$sort": {"average_rating": -1}}
    ]

    results = movies_collection.aggregate(pipeline)
    for result in results:
        print(result)

    calculate_average_ratings(db)

    #문제 4
def count_books_by_year(db):
    books_collection = db.books
    pipeline = [
        {"$group": {"_id": "$year", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]

    results = books_collection.aggregate(pipeline)
    for result in results:
        print(result)

    #함수 실행 코드
    count_books_by_year(db)

    #문제 5
    from datetime import datetime

def update_user_actions_before_date(db, user_id, date, old_action, new_action):
    user_actions_collection = db.user_actions
    query = {"user_id": user_id, "action": old_action, "timestamp": {"$lt": date}}
    update = {"$set": {"action": new_action}}

    result = user_actions_collection.update_many(query, update)
    print(f"Updated {result.modified_count} documents.")

    #함수 실행 코드
    update_user_actions_before_date(db, 1, datetime(2023, 4, 13), "view", "seen")

if __name__ == "__main__":
    insert_data()

