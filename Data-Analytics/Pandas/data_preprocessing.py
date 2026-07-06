import pandas as pd
import re

# Sample DataFrame
data = {
    'Col_name': ['Value1', 'Value2', 'Old_String', 'Value4']
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

# Lowercase
df['Col_name'] = df['Col_name'].str.lower()
print("\nLowercase")
print(df)

# Uppercase
df['Col_name'] = df['Col_name'].str.upper()
print("\nUppercase")
print(df)

# Replace substring
df['Col_name'] = df['Col_name'].str.replace('OLD_STRING', 'new_string')

print("\nReplace Substring")
print(df)

# Replace specific values
df['Col_name'] = df['Col_name'].replace({
    'VALUE1': 'A',
    'VALUE2': 'B'
})

print("\nReplace Values")
print(df)

# Replace using regex
df['Col_name'] = df['Col_name'].replace(
    'new_string',
    'C',
    regex=True
)

print("\nRegex Replace")
print(df)

# Type Conversion Example

df2 = pd.DataFrame({
    'Col_name': ['1', '2', '3', '4', '5', 'apple']
})

print("\nOriginal Numeric Data")
print(df2)

# Convert to numeric with errors handled
df2['Col_name'] = pd.to_numeric(
    df2['Col_name'],
    errors='coerce'
)

print("\nConvert to Numeric")
print(df2)
