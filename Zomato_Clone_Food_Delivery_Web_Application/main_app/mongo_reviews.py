from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["zomato_reviews"]
collection = db["reviews"]

# Save a review
def save_review(user, restaurant_id, review, rating):
    collection.insert_one({
        "user": user.username,
        "restaurant_id": str(restaurant_id),
        "review": review,
        "rating": rating
    })

# Get reviews for a restaurant
def get_reviews(restaurant_id):
    return list(collection.find({"restaurant_id": str(restaurant_id)}))
