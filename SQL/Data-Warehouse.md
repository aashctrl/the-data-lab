# Data Warehouse Fundamentals

## What is a Data Warehouse?
A Data Warehouse is a centralized repository that stores historical data collected from multiple sources. It is designed for reporting, analytics, and business intelligence rather than day-to-day transactions.

### Characteristics
- Stores historical data
- Integrates data from multiple sources
- Optimized for analysis and reporting
- Read-heavy workload

## Keys in Data Warehouse
### Candidate Key
A column (or set of columns) that can uniquely identify each record in a table.
Example:
- Student_ID
- Email
### Primary Key
The candidate key selected to uniquely identify each row.
Properties:
- Unique
- Cannot contain NULL values
- Only one primary key per table
Example:
Student(Student_ID, Name)
Student_ID → Primary Key
### Foreign Key
A column that references the primary key of another table.
Purpose:
- Creates relationships between tables
- Maintains referential integrity
Example:
Orders(Customer_ID)
Customer_ID → Foreign Key referencing Customers(Customer_ID)
### Surrogate Key
A system-generated unique identifier with no business meaning.
Example:
- 1
- 2
- 3
- 4
Advantages:
- Stable
- Faster joins
- Independent of business data

## Fact Table
A fact table stores measurable business data.
Examples:
- Sales Amount
- Quantity Sold
- Profit
- Revenue
Example:
| Order_ID | Product_ID | Customer_ID | Amount |
|----------|------------|-------------|--------|
| 101 | P01 | C01 | 500 |
## Dimension Table
A dimension table stores descriptive information used to analyze facts.
Examples:
- Customer
- Product
- Time
- City
Example:
| Customer_ID | Name | City |
|-------------|------|------|
| C01 | Aashi | Delhi |

## Fact vs Dimension Table
| Fact Table | Dimension Table |
|------------|-----------------|
| Stores numerical values | Stores descriptive information |
| Large | Comparatively smaller |
| Frequently updated | Less frequently updated |
| Used for calculations | Used for filtering and grouping |

## Key Takeaways
- A Data Warehouse is built for analytics, not transactions.
- Primary and Foreign Keys create relationships.
- Surrogate Keys improve consistency and performance.
- Fact Tables store measurable business data.
- Dimension Tables provide context to analyze facts.
