import requests
import json

# Replace YOUR_API_KEY with your actual API key
api_key = 'YOUR_API_KEY'

# Set up the API endpoint and authentication
endpoint = "https://analyticsreporting.googleapis.com/v4/reports:batchGet"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

# Replace YOUR_VIEW_ID with the actual View ID of the Google Analytics view you want to pull data from
view_id = 'YOUR_VIEW_ID'

# Set the parameters for the API request
metrics = [{"expression": "ga:sessions"}]
dimensions = [{"name": "ga:date"}]
date_range = {"startDate": "7daysAgo", "endDate": "today"}

# Build the request body
body = {
    "reportRequests": [
        {
            "viewId": view_id,
            "dateRanges": [date_range],
            "metrics": metrics,
            "dimensions": dimensions,
        }
    ]
}

# Send the API request
response = requests.post(endpoint, headers=headers, json=body)

# Print the response in JSON format
data = json.loads(response.text)
print(json.dumps(data, indent=4))
