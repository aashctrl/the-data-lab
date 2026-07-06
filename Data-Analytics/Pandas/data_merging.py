import pandas as pd

# First DataFrame
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['John', 'Alice', 'Bob', 'Emily']
})

# Second DataFrame
df2 = pd.DataFrame({
    'ID': [2, 3, 5, 6],
    'City': ['New York', 'London', 'Paris', 'Berlin']
})

print("DataFrame 1")
print(df1)

print("\nDataFrame 2")
print(df2)

# Inner Join
inner_join = pd.merge(
    df1,
    df2,
    on='ID',
    how='inner'
)

print("\nInner Join")
print(inner_join)

# Left Join
left_join = pd.merge(
    df1,
    df2,
    on='ID',
    how='left'
)

print("\nLeft Join")
print(left_join)

# Right Join
right_join = pd.merge(
    df1,
    df2,
    on='ID',
    how='right'
)

print("\nRight Join")
print(right_join)

# Outer Join
outer_join = pd.merge(
    df1,
    df2,
    on='ID',
    how='outer'
)

print("\nOuter Join")
print(outer_join)
