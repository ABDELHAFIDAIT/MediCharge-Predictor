# Import Pandas library
import pandas as pd


# Read Data CSV file
data = pd.read_csv('./data/raw/data.csv')


# Display Data Columns
columns =  data.columns
print("Data Columns: =================================================================")
for col in columns:
    print("-",col)


# Display Data Types
dtypes = data.dtypes
print("\nData Types: ====================================================================")
for col, dtype in dtypes.items():
    print(f"- {col}: {dtype}")


# Display Data Shape [Rows, Columns]
shape = data.shape
print(f"\nData Shape: ====================================================================\n- Rows: {shape[0]}\n- Columns: {shape[1]}")


# Display first 5 rows of the Data
print("\nFirst 5 rows of the Data: ==============================================================")
print(data.head())


# Display Data Information
print("\nData Information: ==================================================================")
data.info()


# Display summary statistics of the Data
print("\nSummary Statistics of the Data: =====================================================")
print(data.describe())
print("=======================================================================================")
print(data.describe(include='all'))


# Check for missing values in each column
missing_values = data.isnull().sum()
print("\nMissing Values in each column: ======================================================")
for col, missing in missing_values.items():
    print(f"- {col}: {missing} missing values")


# Check for duplicate rows in the Data
duplicate_rows = data.duplicated().sum()
print(f"\nDuplicate Rows in the Data: ========================================================\n- {duplicate_rows} duplicate rows found")
# If duplicates exist, display the duplicate rows
if duplicate_rows > 0:
    print("\nDuplicate Rows: ====================================================================")
    print(data[data.duplicated()])