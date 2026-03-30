import requests
import json
import os

# Configuration settings
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
TENANT_ID = os.getenv('TENANT_ID')
WORKSPACE_ID = os.getenv('WORKSPACE_ID')
POWER_BI_API_URL = "https://api.powerbi.com/v1.0/myorg"

def get_access_token():
    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'scope': 'https://analysis.windows.net/powerbi/api/.default',
        'grant_type': 'client_credentials'
    }
    
    response = requests.post(url, headers=headers, data=data)
    if response.status_code != 200:
        raise Exception(f"Error obtaining access token: {response.text}")
    return response.json().get('access_token')

def import_workbook(workbook_id):
    url = f"{POWER_BI_API_URL}/workspaces/{WORKSPACE_ID}/importFiles/{workbook_id}/import"
    token = get_access_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, headers=headers)
    
    if response.status_code != 202:
        raise Exception(f"Error importing workbook: {response.text}")

def main():
    try:
        workbook_id = "your-workbook-id-here"  # Replace with your Power BI Workbook ID
        import_workbook(workbook_id)
        print(f"Workbook {workbook_id} imported successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()