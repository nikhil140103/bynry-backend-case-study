Bynry backend engineering Case Study

This is repository contains my submission for the Backend Engineering Intern role for Byrny.

##  Problem 

The case study consisted of three parts:

1. **Fixing an existing API**: API that accepts product details via POST request.
2. **Designing the Database Schema**: SQL schema to support the product inventory system.
3. **Creating a new REST API**: An API that returns low stock alerts based on a given threshold.

____

## Implementation Details.

### Part 1 - `main.py`
- Debugged the product POST API using flask.
- Ensured input validation and correct database saved.

### Part 2 - `schema.sql`
- Designed a normal schema with tables for Products.
- Included sample fields like name, description, price, stock_quantity, threshold_quantity.

### Part 3 - `low_stock_api.py`
- Developed a REST GET API to fetch products below the stock threshold.
- The API is clean, simple and uses mock data / SQL for now.

___

## Tech Stack

- Python
- Flask 
- SQL (schema + logic)
- Postman (for testing)

____

##  How to Run

1. Clone the repo
2. Install requirements: `pip install -r requirements.txt`
3. Run: `python main.py` or `python low_stock_api.py`
4. Use Postman or browser to test the endpoints

___

##  Thank You

Thank you for the opportunity. I looking forward to the next steps...

Nikhil Pandhare
nikhilpandhare14@gmail.com
