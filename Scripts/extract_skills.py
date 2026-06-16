import pandas as pd

# Read jobs data
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
jobs_path = os.path.join(BASE_DIR, "data", "jobs.csv")

df = pd.read_csv(jobs_path)

# Skills to track
skills = {
    "SQL": r"\bSQL\b",
    "Python": r"\bPython\b",
    "Excel": r"\bExcel\b",
    "Power BI": r"\bPower\s*BI\b",
    "Tableau": r"\bTableau\b",
    "Machine Learning": r"\bMachine Learning\b",
    "R": r"\bR\b",
    "AWS": r"\bAWS\b"
}

skill_counts = {}

# Count occurrences
skill_counts = {}

for skill, pattern in skills.items():
    count = df["Description"].str.contains(
        pattern,
        case=False,
        na=False,
        regex=True
    ).sum()

    skill_counts[skill] = count

# Convert to DataFrame
skills_df = pd.DataFrame(
    list(skill_counts.items()),
    columns=["Skill", "Count"]
)

# Save results
skills_path = os.path.join(BASE_DIR, "data", "skills.csv")
skills_df.to_csv(skills_path, index=False)

print(skills_df)