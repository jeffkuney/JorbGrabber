import requests

# Set up API key and endpoint (example for RapidAPI's JSearch API)
API_KEY = "your_rapidapi_key"
url = "https://jsearch.p.rapidapi.com/search"

# Define job search parameters
query_params = {
    "query": "Project Manager",  # Your search query
    "location": "New York",      # Your location preference
    "page": 1                    # Pagination if you want more results
}

# Set up headers for authorization
headers = {
    "x-rapidapi-host": "jsearch.p.rapidapi.com",
    "x-rapidapi-key": API_KEY
}

# Make the API request
response = requests.get(url, headers=headers, params=query_params)

# Check if the request was successful
if response.status_code == 200:
    job_data = response.json()  # Get job listings in JSON format
    # Process the job listings
    for job in job_data.get("data", []):
        print("Job Title:", job.get("title"))
        print("Company:", job.get("company_name"))
        print("Location:", job.get("location"))
        print("Description:", job.get("snippet"))
        print("Posted:", job.get("posted_at"))
        print("-" * 20)
else:
    print("Error:", response.status_code, response.text)