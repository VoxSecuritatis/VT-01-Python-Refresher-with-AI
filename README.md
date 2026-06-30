# Analyzing Customer Orders Using Python
##### VT_AGI: Python Refresher with AI Module Project | Brock Frary | 2026-05-09

E-commerce order analysis using Python's built-in data structures. A standalone script
processes 48 customer transactions across three product categories, classifies buyers by
spending tier, identifies revenue trends, and surfaces cross-category purchasing patterns
-- no external libraries required.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-None%20(stdlib%20only)-4CAF50)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&logoColor=white)

---

## Primary Project Artifact:
### **[customer_order_analysis.py](https://github.com/VoxSecuritatis/VT-01-Python-Refresher-with-AI/blob/main/customer_order_analysis.py)**

---

## About This Project

This is the module project for **VT_AGI: Python Refresher with AI**, part of the
*Applied Agentic AI: Systems, Design & Impact* course at Virginia Tech / Simplilearn.

The project analyzes simulated e-commerce customer order data to generate business
insights a data analyst would present to business managers. The dataset -- 48 orders
from 11 customers across 3 product categories -- is hardcoded as a list of tuples,
making it a clean demonstration of Python data structures without I/O complexity.

The analysis pipeline runs entirely through the Python standard library: lists, tuples,
dictionaries, sets, loops, conditionals, sorting, and list comprehensions. The final
output is an 8-section formatted console report covering customer classifications,
category revenue, unique products, top spenders, and cross-category purchasing patterns.

---

## Analysis Pipeline

```
[Raw Orders List]  -- 48 tuples: (customer_name, product, price, category)
        |
        v
[Data Organization]  -- unique customer names, order details dict, products dict
        |
        v
[Category Classification]  -- product -> category mapping, unique categories set
        |
        v
[Customer Spend Analysis]  -- total spend per customer, buyer tier classification
        |                        High-value (>$100) / Moderate ($50-$100) / Low (<$50)
        v
[Business Insights]  -- revenue per category, unique products set, top 3 spenders
        |
        v
[Cross-Category Analysis]  -- multi-category customers, Electronics & Clothing intersection
        |
        v
[Report Output]  -- 8-section formatted console report
```

---

## Report Sections

| # | Section | Method |
|---|---|---|
| 1 | Customer Classifications | Loop + conditionals over per-customer totals |
| 2 | Total Revenue per Category | Dictionary accumulation |
| 3 | Unique Products | Set deduplication |
| 4 | Top 3 Highest-Spending Customers | `sorted()` with `key=lambda`, `reverse=True` |
| 5 | Customers Who Purchased Electronics | List comprehension + deduplication loop |
| 6 | Customers Who Purchased from Multiple Categories | Set membership count per customer |
| 7 | Customers Who Bought Both Electronics and Clothing | Set intersection logic |
| 8 | Most Frequently Purchased Products | Dict count accumulation + max filter |

---

## Key Design Decisions

| Decision | Choice | Rationale |
|---|---|---|
| Hardcoded dataset vs. file input | Hardcoded list of tuples | Keeps focus on data structure manipulation rather than I/O; no file dependency for reviewers |
| Functions vs. classes | Functions only | The pipeline is linear with no shared mutable state; classes would add abstraction without benefit |
| Standard library only vs. pandas | stdlib only | Demonstrates core Python competency; pandas would obscure the data structure work the project is meant to show |
| Deduplication via list vs. set | List for ordered output, set for uniqueness checks | Preserves insertion order for report display while using set semantics for membership testing |
| One function per operation | Separate named functions | Keeps each transformation testable and independently readable; avoids one large procedural block |

---

## Key Learnings

**Sets for deduplication and intersection:** Python sets eliminate duplicate-tracking
code that would otherwise require repeated `if x not in list` checks. The
`find_unique_products` and `get_unique_categories` functions demonstrate this -- a single
`set.add()` per iteration replaces a conditional branch. The intersection logic in
`find_common_category_customers` identifies cross-category buyers without nested loops.

**Dictionary accumulation pattern:** The revenue and spending total functions use the
same pattern -- check for key existence, initialize to 0.0 if missing, then accumulate.
This is the idiomatic Python alternative to `defaultdict` when keeping dependencies
minimal, and it applies directly to any aggregation problem.

**List comprehension with filtering:** `find_electronics_customers` filters orders in a
single readable line using an inline `if` condition. The subsequent deduplication loop
shows the trade-off: comprehensions are concise for filtering but need a separate pass
when uniqueness matters (or a seen-set approach for larger datasets).

**`sorted()` with `key=lambda`:** Sorting a dictionary's `.items()` by value in
descending order using `key=lambda x: x[1], reverse=True` is a reusable pattern for
ranked output. Slicing with `[:top_n]` makes it trivially extensible to any rank depth.

---

## Tech Stack

| Layer | Technology | Notes |
|---|---|---|
| Language | Python 3.12 | No virtual environment or packages required |
| Data structures | list, tuple, dict, set | All stdlib; zero third-party dependencies |
| Development tool | GitHub Copilot | AI-assisted development; all logic reviewed and validated manually |

---

## Dataset

| Attribute | Value |
|---|---|
| Customers | 11 (Alice, Bob, Charlie, Diana, Eve, Frank, Grace, Henry, Ivy, Jack, Kelly) |
| Orders | 48 total transactions |
| Categories | Electronics, Clothing, Home Essentials |
| Unique products | 33 |
| Price range | $2.00 -- $800.00 |

---

## Prerequisites

| Requirement | Version |
|---|---|
| Python | 3.8+ (3.12 recommended) |

No packages to install. No virtual environment needed.

---

## Setup and Run

```bash
python customer_order_analysis.py
```

The script prints the available product categories, then the full 8-section analysis
report, to stdout.

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
   Charlie: Moderate buyer ($227.00)
   ...

4. Top 3 Highest-Spending Customers:
   1. Alice ($1047.00)
   2. Diana ($885.00)
   3. Eve ($810.00)

Key Business Insights:
- Electronics is the highest revenue category.
- High-value buyers contribute significantly to revenue.
- Many customers purchase from multiple categories, indicating diverse interests.
- Clothing items are frequently purchased, suggesting popularity.
```

---

## Project Structure

```
.
├── customer_order_analysis.py  # Full analysis pipeline: data, functions, report
├── README.md                   # This file
└── .gitignore                  # Excludes .venv and CLAUDE.md
```

---

> © 2026 Brock Frary. All rights reserved.
