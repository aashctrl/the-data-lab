import pandas as pd

# Sample DataFrame
data = {
    'Col_name': [10, 15, 12, 8, 20, 25, 7, 300000]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

# -------------------------
# Z-Score Method
# -------------------------

z_scores = (
    (df['Col_name'] - df['Col_name'].mean())
    / df['Col_name'].std()
)

threshold = 3

outliers = df[abs(z_scores) > threshold]

print("\nOutliers using Z-Score")
print(outliers)

# -------------------------
# IQR Method
# -------------------------

Q1 = df['Col_name'].quantile(0.25)
Q3 = df['Col_name'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers_iqr = df[
    (df['Col_name'] < lower)
    | (df['Col_name'] > upper)
]

print("\nOutliers using IQR")
print(outliers_iqr)
