The Api so far has 2 methods

Get, to get the stock of a specific item at a shop with the closet expiry date
Post, will add entry to the database with a new item with the 3 values to be unique gtin with shop and expiry date

get request example:
http://127.0.0.1:8000/stock/?gtin=112&shop=Paris
will get the items with gtin 112 at the Paris shop with the nearest expiry date

post request example:

{
    "gtin": "111111",
    "shop": "Paris",
    "quantity": 45,
    "expirydate": "2021-09-11"
}