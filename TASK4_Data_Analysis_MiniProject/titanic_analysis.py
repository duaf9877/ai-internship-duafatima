
import pandas as pd
import matplotlib
matplotlib.use("Agg")   # lets us save charts without opening a window
import matplotlib.pyplot as plt
import os

# ---------- Settings ----------
DATA_FILE = "data/titanic.csv"
OUTPUT_FOLDER = "outputs"

# Make sure the outputs folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# ===================================================================
# STEP 1: Load the dataset
# ===================================================================
print("STEP 1: Loading the dataset")
print("-" * 40)

data = pd.read_csv(DATA_FILE)

print("Number of rows and columns:", data.shape)
print("\nFirst 5 rows of the data:")
print(data.head())

print("\nColumn names:")
print(list(data.columns))


# ===================================================================
# STEP 2: Clean missing values
# ===================================================================
print("\nSTEP 2: Cleaning missing values")
print("-" * 40)

# See how many values are missing in each column
print("Missing values BEFORE cleaning:")
print(data.isnull().sum())

# Age has some missing values -> fill them with the median age
median_age = data["Age"].median()
data["Age"] = data["Age"].fillna(median_age)

# Embarked has a couple of missing values -> fill with the most common value
most_common_port = data["Embarked"].mode()[0]
data["Embarked"] = data["Embarked"].fillna(most_common_port)

# Cabin is missing for most passengers, so we simply drop this column
data = data.drop(columns=["Cabin"])

print("\nMissing values AFTER cleaning:")
print(data.isnull().sum())

# Save the cleaned data to a new CSV file
data.to_csv(os.path.join(OUTPUT_FOLDER, "titanic_cleaned.csv"), index=False)
print(f"\nCleaned data saved to {OUTPUT_FOLDER}/titanic_cleaned.csv")


# ===================================================================
# STEP 3: Summary statistics
# ===================================================================
print("\nSTEP 3: Summary statistics")
print("-" * 40)

print("Basic statistics for numeric columns:")
print(data.describe())

print("\nHow many people survived (1) vs died (0):")
print(data["Survived"].value_counts())

print("\nHow many passengers were male / female:")
print(data["Sex"].value_counts())

print("\nHow many passengers were in each class (1st, 2nd, 3rd):")
print(data["Pclass"].value_counts())


# ===================================================================
# STEP 4: Exploratory Data Analysis (EDA)
# ===================================================================
print("\nSTEP 4: Exploratory Data Analysis")
print("-" * 40)

# Survival rate by gender
survival_by_sex = data.groupby("Sex")["Survived"].mean() * 100
print("Survival rate (%) by gender:")
print(survival_by_sex)

# Survival rate by passenger class
survival_by_class = data.groupby("Pclass")["Survived"].mean() * 100
print("\nSurvival rate (%) by passenger class:")
print(survival_by_class)

# Average age of people who survived vs who did not
avg_age_by_survival = data.groupby("Survived")["Age"].mean()
print("\nAverage age (0 = died, 1 = survived):")
print(avg_age_by_survival)

# Average ticket fare by class
avg_fare_by_class = data.groupby("Pclass")["Fare"].mean()
print("\nAverage fare by passenger class:")
print(avg_fare_by_class)


# ===================================================================
# STEP 5: Simple charts
# ===================================================================
print("\nSTEP 5: Creating charts")
print("-" * 40)

# Chart 1: How many people survived vs died
plt.figure()
data["Survived"].value_counts().plot(kind="bar", color=["red", "green"])
plt.title("Survived vs Died")
plt.xlabel("0 = Died, 1 = Survived")
plt.ylabel("Number of Passengers")
plt.savefig(os.path.join(OUTPUT_FOLDER, "chart_survival_count.png"))
plt.close()

# Chart 2: Survival rate by gender
plt.figure()
survival_by_sex.plot(kind="bar", color="blue")
plt.title("Survival Rate by Gender")
plt.ylabel("Survival Rate (%)")
plt.savefig(os.path.join(OUTPUT_FOLDER, "chart_survival_by_gender.png"))
plt.close()

# Chart 3: Survival rate by class
plt.figure()
survival_by_class.plot(kind="bar", color="purple")
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate (%)")
plt.savefig(os.path.join(OUTPUT_FOLDER, "chart_survival_by_class.png"))
plt.close()

# Chart 4: Age distribution
plt.figure()
data["Age"].plot(kind="hist", bins=20, color="teal", edgecolor="black")
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.savefig(os.path.join(OUTPUT_FOLDER, "chart_age_distribution.png"))
plt.close()

print("4 charts saved in the 'outputs' folder.")


# ===================================================================
# STEP 6: Key findings
# ===================================================================
print("\nSTEP 6: Key findings")
print("-" * 40)

overall_rate = data["Survived"].mean() * 100

findings = f"""
Key Findings from the Titanic Dataset
--------------------------------------
1. Overall survival rate was about {overall_rate:.1f}%.
2. Women survived much more often than men
   (female: {survival_by_sex['female']:.1f}%, male: {survival_by_sex['male']:.1f}%).
3. Passengers in 1st class survived more often than those in 3rd class
   (1st class: {survival_by_class[1]:.1f}%, 3rd class: {survival_by_class[3]:.1f}%).
4. People who survived were, on average, slightly younger
   ({avg_age_by_survival[1]:.1f} years) than those who did not
   ({avg_age_by_survival[0]:.1f} years).
5. First class passengers paid a much higher average fare
   ({avg_fare_by_class[1]:.2f}) than third class passengers
   ({avg_fare_by_class[3]:.2f}).
"""

print(findings)

with open(os.path.join(OUTPUT_FOLDER, "key_findings.txt"), "w") as f:
    f.write(findings)

print("Project finished successfully. Check the 'outputs' folder for results.")
