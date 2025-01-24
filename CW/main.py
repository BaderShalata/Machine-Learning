import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("/Users/badershalata/Documents/StatsCW/MavenRail.csv")
num_records = df.shape[0]
print(f"Number of records: {num_records}")
# This method just outputs the different categories in the columns
# It also checks if the column has any missing values
def attributeCol(Column):
    df_column = df[Column].unique()
    print(f"{Column} Missing Values", df[Column].isna().sum())
    print(df_column)
for i in df.columns:
    attributeCol(i)

print("TICKET PRICES")
# This visualizes tickets prices with their frequency
df['Price'].plot(kind='hist', bins=30, color='blue', alpha=0.7)
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()
print()
print(df['Price'].describe())
# MULTIVARIATE
# This does Crosstab tables to check correlation between Journey Status and Refund requests
crosstab_analysis = pd.crosstab(df['Journey.Status'], df['Refund.Request'])
print(crosstab_analysis)