# Titanic Data Analysis Mini Project

## 1. About the Dataset

- **Name:** Titanic Passenger Dataset
- **Source:** https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
- **Rows / Columns:** 891 passengers, 12 columns
- **What it contains:** Information about the passengers on the Titanic, including
  whether they survived, their age, sex, ticket class, fare paid, and family details.

| Column      | Meaning                                          |
|-------------|---------------------------------------------------|
| PassengerId | Unique ID for each passenger                      |
| Survived    | 0 = Died, 1 = Survived                             |
| Pclass      | Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)           |
| Name        | Passenger's name                                   |
| Sex         | Male / Female                                       |
| Age         | Age in years                                        |
| SibSp       | Number of siblings/spouses aboard                   |
| Parch       | Number of parents/children aboard                   |
| Ticket      | Ticket number                                       |
| Fare        | Ticket price                                        |
| Cabin       | Cabin number                                        |
| Embarked    | Port of boarding (C, Q, or S)                        |

## 2. Project Files

```
project/
├── titanic_analysis.py      # main Python script
├── data/
│   └── titanic.csv          # original dataset
├── outputs/
│   ├── titanic_cleaned.csv       # dataset after cleaning
│   ├── chart_survival_count.png
│   ├── chart_survival_by_gender.png
│   ├── chart_survival_by_class.png
│   ├── chart_age_distribution.png
│   └── key_findings.txt
└── README.md
```

## 3. How to Run

1. Make sure Python is installed along with `pandas` and `matplotlib`:
   ```
   pip install pandas matplotlib
   ```
2. Run the script from inside the `project` folder:
   ```
   python titanic_analysis.py
   ```
3. All results (cleaned data, charts, and findings) will appear in the `outputs/` folder.

## 4. Data Cleaning Process

The raw dataset had missing values in three columns:

| Column   | Missing Values | How It Was Fixed                          |
|----------|-----------------|---------------------------------------------|
| Age      | 177             | Filled with the **median** age of all passengers |
| Embarked | 2               | Filled with the **most common** boarding port     |
| Cabin    | 687             | Column **dropped** (too many missing values to fill reliably) |

After cleaning, the dataset has **no missing values** in the remaining columns.

## 5. Analysis Performed

- Loaded the CSV file with Pandas and looked at its shape, columns, and data types.
- Checked and cleaned missing values (see above).
- Calculated summary statistics: `describe()`, value counts for survival, sex, and class.
- Explored relationships using `groupby()`:
  - Survival rate by gender
  - Survival rate by passenger class
  - Average age of survivors vs. non-survivors
  - Average ticket fare by class
- Created 4 charts using Matplotlib to visualize the findings.

## 6. Key Findings

1. Overall survival rate was about **38.4%** (342 out of 891 passengers survived).
2. **Gender mattered a lot:** women survived at **74.2%**, men only at **18.9%**.
3. **Class mattered too:** 1st class passengers survived at **63.0%**, compared to
   only **24.2%** for 3rd class passengers.
4. Passengers who survived were, on average, slightly **younger (28.3 years)** than
   those who did not survive (30.0 years).
5. 1st class passengers paid a much higher average fare (**84.15**) than 3rd class
   passengers (**13.68**), reflecting the class-based nature of survival chances.

## 7. Conclusion

The analysis shows that survival on the Titanic was strongly influenced by **gender**
and **passenger class**, consistent with the historical "women and children first"
policy and better lifeboat access for wealthier, higher-class passengers.
