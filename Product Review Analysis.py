

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

def first_30_characters():
    review = input("Passing along but getting better at Python Programming also!")
    for review in reviews:
        if reviews[0:30:1]:
            print(f"{review} {reviews}")
            
            
first_30_characters()