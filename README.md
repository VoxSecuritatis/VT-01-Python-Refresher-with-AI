# **Analyzing Customer Orders Using Python**

Course-End Project 1 -- VT Week 1: Introduction to Python using AI
**Author:** Brock Frary | **Date:** 2026-05-09

---

## Overview

This project analyzes simulated e-commerce customer orders using Python's core data structures and control flow. The goal is to classify customers by spending tier, identify revenue trends by product category, and surface business insights -- all without external libraries.

The script demonstrates practical use of lists, tuples, dictionaries, and sets alongside loops, conditionals, sorting, and list comprehensions.

---

## Dataset

The dataset is hardcoded in `customer_order_analysis.py` as a list of tuples. Each tuple represents one order:

```
(customer_name, product, price, category)
```

- **Customers:** 11 (Alice, Bob, Charlie, Diana, Eve, Frank, Grace, Henry, Ivy, Jack, Kelly)
- **Orders:** 48 total transactions
- **Categories:** Electronics, Clothing, Home Essentials
- **Products:** 33 unique items (e.g., Laptop, T-Shirt, Blender, Smartphone)
- **Price range:** $2.00 to $800.00

---

## Tasks Completed

### 1. Store Customer Orders
- List of unique customer names extracted from raw orders
- Each order stored as a `(name, product, price, category)` tuple in a master list
- Dictionary mapping each customer name to their list of order tuples
- Dictionary mapping each customer name to their list of purchased product names

### 2. Classify Products by Category
- Dictionary mapping each product to its category
- Set of unique product categories (deduplication)
- Printed display of all available categories

### 3. Analyze Customer Orders
- Total spending calculated per customer via loop
- Customers classified by spending tier:

| Tier | Threshold |
|---|---:|
| High-value buyer | above $100.00 |
| Moderate buyer | $50.00 to $100.00 |
| Low-value buyer | below $50.00 |

### 4. Generate Business Insights
- Total revenue per product category stored in a dictionary
- Unique products extracted across all orders using a set
- Electronics customers identified using list comprehension
- Top 3 highest-spending customers identified via `sorted()`

### 5. Organize and Display Data
- Full report printed to console with labeled sections
- Set operations used to find customers purchasing from multiple categories
- Intersection logic identifies customers who bought both Electronics and Clothing

---

## Functions

| Function | Purpose |
|---|---|
| `get_customer_names` | Returns a deduplicated list of customer names |
| `build_customer_orders` | Maps each customer to their full order tuples |
| `build_customer_products` | Maps each customer to their purchased product names |
| `build_product_categories` | Maps each product to its category |
| `get_unique_categories` | Returns the set of all unique categories |
| `display_categories` | Prints sorted category list |
| `calculate_customer_totals` | Sums total spend per customer |
| `classify_customers` | Assigns High/Moderate/Low tier to each customer |
| `calculate_category_revenue` | Sums revenue per product category |
| `find_unique_products` | Returns set of all unique products ordered |
| `find_electronics_customers` | List comprehension to find Electronics buyers |
| `find_top_customers` | Returns top N spenders via sorting |
| `find_multi_category_customers` | Finds customers who bought across categories |
| `find_common_category_customers` | Finds customers who bought from two named categories |
| `find_most_frequently_purchased_products` | Finds products with the highest order count |
| `print_report` | Prints the complete formatted analysis report |
| `main` | Orchestrates all functions and runs the analysis |

---

## Python Concepts Demonstrated

- **Lists** -- storing and iterating over ordered collections
- **Tuples** -- immutable order records; unpacking with `customer, product, price, category = order`
- **Dictionaries** -- mapping customers to orders, products to categories, categories to revenue
- **Sets** -- deduplication of products and categories; membership testing
- **Loops** -- iterating over orders to aggregate totals and classify customers
- **Conditionals** -- spending tier branching (`if / elif / else`)
- **List comprehension** -- filtering electronics buyers in one line
- **Sorting** -- `sorted()` with `key=lambda` and `reverse=True` for top-spender ranking
- **Set operations** -- multi-category and cross-category customer detection
- **f-strings** -- formatted currency output (`${total:.2f}`)

---

## How to Run

No dependencies beyond the Python standard library. No `requirements.txt` needed.

```bash
python customer_order_analysis.py
```

The script prints category listings followed by the full analysis report to stdout.

---

## Sample Output (abbreviated)

```
Available Product Categories:
- Clothing
- Electronics
- Home Essentials

==================================================
CUSTOMER ORDER ANALYSIS REPORT
==================================================

1. Customer Classifications:
   Alice: High-value buyer ($1047.00)
   Bob: High-value buyer ($375.00)
   ...

2. Total Revenue per Category:
   Electronics: $...
   Clothing: $...
   Home Essentials: $...

3. Unique Products:
   Total unique products: 33
   ...

4. Top 3 Highest-Spending Customers:
   1. Alice ($1047.00)
   ...

Key Business Insights:
- Electronics is the highest revenue category.
- High-value buyers contribute significantly to revenue.
- Many customers purchase from multiple categories, indicating diverse interests.
- Clothing items are frequently purchased, suggesting popularity.
```

---

## Project Context

This script was completed as **Project 1** of the Simplilearn VT Applied Agentic AI program, Week 1 module: "Introduction to Python using AI." It was developed with GitHub Copilot assistance to demonstrate AI-aided Python development for data analysis use cases.
