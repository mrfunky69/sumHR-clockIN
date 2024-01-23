import requests
import time
import datetime
import pytz 
print('script started')
def hit_api():
    try:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOjU5NDA2LCJhY2NvdW50aWQiOjI4MSwic3Vic2NyaXB0aW9uaWQiOjI5MCwiZW1wbG95ZWVpZCI6OTE5MTksInRpbWV6b25laWQiOjI1MSwicm9sZWlkIjo4NDMsIm1hc3RlcnByb2ZpbGVpZCI6NywibG9naW5pbmZvaWQiOjMxMjYwNTQsImVtYWlsaWQiOiJyb2hpdC5rdW1hcjJAbWNraW5sZXlyaWNlLmNvIiwiZXhwIjoxNzA2NTAyNTg3LCJpYXQiOjE3MDU4OTc3ODd9.YEzYLMZ3G-xTbfJUcraqVaNU1zTCUnPpwNzvrhdFozY',
            'Connection': 'keep-alive',
            'Origin': 'https://mckinley.sumhr.io',
            'Referer': 'https://mckinley.sumhr.io/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
        }

        # Replace 'your_api_endpoint_here' with the actual API endpoint
        response = requests.get('https://api.sumhr.io:3000/api/attendance/initwebpunch/122.169.8.177', headers=headers)
        
        print('API Response:', response.text)
    except Exception as e:
        print('Error hitting the API:', str(e))

def schedule_api_hits():
  # Set the timezone to Indian Standard Time (IST)
    ist_timezone = pytz.timezone('Asia/Kolkata')
    # Schedule the API hits every day except Saturday and Sunday
    while True:
        current_day = datetime.datetime.now(ist_timezone).strftime('%A')
        if current_day not in ['Saturday', 'Sunday']:
            current_time = datetime.datetime.now(ist_timezone).strftime('%H:%M')
            if current_time == '09:47' or current_time == '18:47':
                print('Clocking In / Out Hiting API')
                hit_api()
        time.sleep(50)  # Check every minute

# Run the scheduled tasks
schedule_api_hits()

