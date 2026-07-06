import pandas as pd

# Creating a sample DataFrame
data = {
    'Col1': [1, 2, None, 4, 5],
    'Col2': ['A', 'B', None, 'D', 'E'],
    'Col3': ['X', 'Y', 'Z', None, 'W']
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

# Check missing values
print("\nMissing Values")
print(df.isnull())

# Count missing values
print("\nMissing Value Count")
print(df.isnull().sum())

# Check if any missing values exist
print("\nAny Missing Values?")
print(df.isnull().values.any())

# Drop rows containing missing values
print("\nDrop Rows with Missing Values")
print(df.dropna())

# Drop columns containing missing values
print("\nDrop Columns with Missing Values")
print(df.dropna(axis=1))

# Drop rows based on selected columns
print("\nDrop Rows Based on Selected Columns")
print(df.dropna(subset=['Col1', 'Col2']))

# Fill missing values with mean
print("\nFill Numeric Missing Values with Mean")
print(df.fillna(df.mean(numeric_only=True)))

# Fill missing values with median
print("\nFill Numeric Missing Values with Median")
print(df.fillna(df.median(numeric_only=True)))

# Forward Fill
print("\nForward Fill")
print(df.ffill())

# Backward Fill
print("\nBackward Fill")
print(df.bfill())
