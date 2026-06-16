import requests
import pandas as pd

APP_ID ="f2bdb7cc"
API_KEY ="62fb4b1ff16b9d78ca444487ce4b88ef"


jobs = []

# Fetch 5 pages
for page in range(1, 6):

    print(f"Fetching Page {page}...")

    url = f"https://api.adzuna.com/v1/api/jobs/in/search/{page}"

    params = {
        "app_id": APP_ID,
        "app_key": API_KEY,
        "what": "Data Analyst",
        "results_per_page": 20
    }

    response = requests.get(url, params=params)

    print("Status Code:", response.status_code)

    data = response.json()

    for job in data["results"]:
        jobs.append({
            "Title": job.get("title"),
            "Company": job.get("company", {}).get("display_name"),
            "Location": job.get("location", {}).get("display_name"),
            "Created": job.get("created"),
            "Description": job.get("description")
        })


# Create DataFrame
df = pd.DataFrame(jobs)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save CSV
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "jobs.csv")

df.to_csv(data_path, index=False)

print("\n🎉 Success!")
print("Total Jobs Collected:", len(df))
print("Saved to data/jobs.csv")

        

