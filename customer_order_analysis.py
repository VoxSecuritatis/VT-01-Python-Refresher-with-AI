# customer_order_analysis.py
# Analyzing Customer Orders Using Python
# VT_Week_1-Introduction to Python using AI
# Brock Frary, 2026-05-09
# Project 21  – Customer Order Analysis (using GitHub Copilot)


# Sample dataset: list of customer orders as tuples (customer_name, product, price, category)
customer_orders = [
    ("Alice", "Laptop", 800.00, "Electronics"),
    ("Bob", "T-Shirt", 20.00, "Clothing"),
    ("Alice", "Headphones", 100.00, "Electronics"),
    ("Charlie", "Blender", 50.00, "Home Essentials"),
    ("Bob", "Jeans", 40.00, "Clothing"),
    ("Diana", "Smartphone", 600.00, "Electronics"),
    ("Alice", "Socks", 10.00, "Clothing"),
    ("Eve", "Vacuum Cleaner", 150.00, "Home Essentials"),
    ("Charlie", "Microwave", 80.00, "Home Essentials"),
    ("Diana", "Dress", 30.00, "Clothing"),
    ("Frank", "Tablet", 300.00, "Electronics"),
    ("Bob", "Sweater", 25.00, "Clothing"),
    ("Alice", "Coffee Maker", 70.00, "Home Essentials"),
    ("Grace", "Monitor", 200.00, "Electronics"),
    ("Charlie", "Pillow", 15.00, "Home Essentials"),
    ("Diana", "Shoes", 50.00, "Clothing"),
    ("Eve", "Toaster", 25.00, "Home Essentials"),
    ("Frank", "Mouse", 15.00, "Electronics"),
    ("Grace", "Keyboard", 40.00, "Electronics"),
    ("Alice", "Book", 12.00, "Home Essentials"),
    ("Bob", "Hat", 18.00, "Clothing"),
    ("Charlie", "Lamp", 35.00, "Home Essentials"),
    ("Diana", "Earrings", 20.00, "Clothing"),
    ("Eve", "Iron", 30.00, "Home Essentials"),
    ("Frank", "Charger", 10.00, "Electronics"),
    ("Grace", "Mouse Pad", 8.00, "Electronics"),
    ("Alice", "Phone Case", 15.00, "Electronics"),
    ("Bob", "Belt", 22.00, "Clothing"),
    ("Charlie", "Towel", 12.00, "Home Essentials"),
    ("Diana", "Necklace", 45.00, "Clothing"),
    ("Eve", "Blender", 55.00, "Home Essentials"),
    ("Frank", "Headphones", 90.00, "Electronics"),
    ("Grace", "Sweater", 28.00, "Clothing"),
    ("Alice", "Lamp", 40.00, "Home Essentials"),
    ("Bob", "Tablet", 250.00, "Electronics"),
    ("Charlie", "Dress", 35.00, "Clothing"),
    ("Diana", "Vacuum Cleaner", 140.00, "Home Essentials"),
    ("Eve", "Smartphone", 550.00, "Electronics"),
    ("Frank", "Jeans", 45.00, "Clothing"),
    ("Grace", "Coffee Maker", 65.00, "Home Essentials"),
    ("Henry", "Pen", 5.00, "Home Essentials"),
    ("Ivy", "Notebook", 3.00, "Home Essentials"),
    ("Jack", "Keychain", 2.00, "Home Essentials"),
    ("Henry", "Scissors", 15.00, "Home Essentials"),
    ("Ivy", "Eraser", 10.00, "Home Essentials"),
    ("Jack", "Ruler", 8.00, "Home Essentials"),
    ("Kelly", "Wallet", 60.00, "Clothing"),
    ("Kelly", "Bag", 25.00, "Clothing")
]

# Function to create a list of unique customer names
def get_customer_names(customer_orders):
    customers = []
    for order in customer_orders:
        customer_name = order[0]
        if customer_name not in customers:
            customers.append(customer_name)
    return customers

# Function to create a dictionary where keys are customer names and values are lists of order details (tuples)
def build_customer_orders(customer_orders):
    customer_order_details = {}
    for order in customer_orders:
        customer_name = order[0]
        if customer_name not in customer_order_details:
            customer_order_details[customer_name] = []
        customer_order_details[customer_name].append(order)
    return customer_order_details

# Function to create a dictionary where keys are customer names and values are lists of ordered products
def build_customer_products(customer_orders):
    customer_products = {}
    for order in customer_orders:
        customer_name, product, price, category = order
        if customer_name not in customer_products:
            customer_products[customer_name] = []
        customer_products[customer_name].append(product)
    return customer_products

# Function to create a dictionary that maps each product to its category
def build_product_categories(customer_orders):
    product_categories = {}
    for order in customer_orders:
        product, category = order[1], order[3]
        product_categories[product] = category
    return product_categories

# Function to create a set of unique product categories
def get_unique_categories(customer_orders):
    categories = set()
    for order in customer_orders:
        categories.add(order[3])
    return categories

# Function to display all available product categories
def display_categories(categories):
    print("Available Product Categories:")
    for category in sorted(categories):
        print(f"- {category}")

# Function to calculate the total amount each customer spends
def calculate_customer_totals(customer_orders):
    customer_totals = {}
    for order in customer_orders:
        customer_name, product, price, category = order
        if customer_name not in customer_totals:
            customer_totals[customer_name] = 0.0
        customer_totals[customer_name] += price
    return customer_totals

# Function to classify customers based on total spending
def classify_customers(customer_totals):
    classifications = {}
    for customer, total in customer_totals.items():
        if total > 100.00:
            classifications[customer] = "High-value buyer"
        elif 50.00 <= total <= 100.00:
            classifications[customer] = "Moderate buyer"
        else:
            classifications[customer] = "Low-value buyer"
    return classifications

# Function to calculate total revenue per product category
def calculate_category_revenue(customer_orders):
    category_revenue = {}
    for order in customer_orders:
        category, price = order[3], order[2]
        if category not in category_revenue:
            category_revenue[category] = 0.0
        category_revenue[category] += price
    return category_revenue

# Function to extract unique products from all orders using a set
def find_unique_products(customer_orders):
    products = set()
    for order in customer_orders:
        products.add(order[1])
    return products

# Function to find all customers who purchased Electronics using list comprehension
def find_electronics_customers(customer_orders):
    electronics_customers = [order[0] for order in customer_orders if order[3] == "Electronics"]
    # Remove duplicates
    unique_customers = []
    for customer in electronics_customers:
        if customer not in unique_customers:
            unique_customers.append(customer)
    return unique_customers

# Function to identify the top three highest-spending customers using sorting
def find_top_customers(customer_totals, top_n=3):
    # Sort customers by total spending in descending order
    sorted_customers = sorted(customer_totals.items(), key=lambda x: x[1], reverse=True)
    top_customers = sorted_customers[:top_n]
    return [customer for customer, total in top_customers]

# Function to find customers who purchased from multiple categories using set operations
def find_multi_category_customers(customer_orders):
    customer_categories = {}
    for order in customer_orders:
        customer, category = order[0], order[3]
        if customer not in customer_categories:
            customer_categories[customer] = set()
        customer_categories[customer].add(category)
    
    multi_category_customers = []
    for customer, categories in customer_categories.items():
        if len(categories) > 1:
            multi_category_customers.append(customer)
    return multi_category_customers

# Function to identify customers who bought both Electronics and Clothing using set operations
def find_common_category_customers(customer_orders, category_one, category_two):
    customer_categories = {}
    for order in customer_orders:
        customer, category = order[0], order[3]
        if customer not in customer_categories:
            customer_categories[customer] = set()
        customer_categories[customer].add(category)
    
    common_customers = []
    for customer, categories in customer_categories.items():
        if category_one in categories and category_two in categories:
            common_customers.append(customer)
    return common_customers

# Function to find the most frequently purchased products
def find_most_frequently_purchased_products(customer_orders):
    product_counts = {}
    for order in customer_orders:
        product = order[1]
        if product not in product_counts:
            product_counts[product] = 0
        product_counts[product] += 1
    
    # Find the max count
    max_count = max(product_counts.values())
    frequent_products = [product for product, count in product_counts.items() if count == max_count]
    return frequent_products

# Function to print a clear final report
def print_report(customer_totals, classifications, category_revenue, unique_products, top_customers, electronics_customers, multi_category_customers, common_customers, frequent_products):
    print("\n" + "="*50)
    print("CUSTOMER ORDER ANALYSIS REPORT")
    print("="*50)
    
    print("\n1. Customer Classifications:")
    for customer, classification in classifications.items():
        print(f"   {customer}: {classification} (${customer_totals[customer]:.2f})")
    
    print("\n2. Total Revenue per Category:")
    for category, revenue in category_revenue.items():
        print(f"   {category}: ${revenue:.2f}")
    
    print("\n3. Unique Products:")
    print(f"   Total unique products: {len(unique_products)}")
    for product in sorted(unique_products):
        print(f"   - {product}")
    
    print("\n4. Top 3 Highest-Spending Customers:")
    for i, customer in enumerate(top_customers, 1):
        print(f"   {i}. {customer} (${customer_totals[customer]:.2f})")
    
    print("\n5. Customers Who Purchased Electronics:")
    for customer in electronics_customers:
        print(f"   - {customer}")
    
    print("\n6. Customers Who Purchased from Multiple Categories:")
    for customer in multi_category_customers:
        print(f"   - {customer}")
    
    print("\n7. Customers Who Bought Both Electronics and Clothing:")
    for customer in common_customers:
        print(f"   - {customer}")
    
    print("\n8. Most Frequently Purchased Products:")
    for product in frequent_products:
        print(f"   - {product}")
    
    print("\nKey Business Insights:")
    print("- Electronics is the highest revenue category.")
    print("- High-value buyers contribute significantly to revenue.")
    print("- Many customers purchase from multiple categories, indicating diverse interests.")
    print("- Clothing items are frequently purchased, suggesting popularity.")

# Main function to run the analysis
def main():
    # Get unique customer names
    customers = get_customer_names(customer_orders)
    
    # Build customer order details
    customer_order_details = build_customer_orders(customer_orders)
    
    # Build customer products dictionary
    customer_products = build_customer_products(customer_orders)
    
    # Build product categories dictionary
    product_categories = build_product_categories(customer_orders)
    
    # Get unique categories
    categories = get_unique_categories(customer_orders)
    
    # Display categories
    display_categories(categories)
    
    # Calculate customer totals
    customer_totals = calculate_customer_totals(customer_orders)
    
    # Classify customers
    classifications = classify_customers(customer_totals)
    
    # Calculate category revenue
    category_revenue = calculate_category_revenue(customer_orders)
    
    # Find unique products
    unique_products = find_unique_products(customer_orders)
    
    # Find electronics customers
    electronics_customers = find_electronics_customers(customer_orders)
    
    # Find top customers
    top_customers = find_top_customers(customer_totals)
    
    # Find multi-category customers
    multi_category_customers = find_multi_category_customers(customer_orders)
    
    # Find customers who bought both Electronics and Clothing
    common_customers = find_common_category_customers(customer_orders, "Electronics", "Clothing")
    
    # Find most frequently purchased products
    frequent_products = find_most_frequently_purchased_products(customer_orders)
    
    # Print the report
    print_report(customer_totals, classifications, category_revenue, unique_products, top_customers, electronics_customers, multi_category_customers, common_customers, frequent_products)

# Run the script if executed directly
if __name__ == "__main__":
    main()