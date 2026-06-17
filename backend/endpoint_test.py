import os

import requests


api_key = url = os.getenv("ENDPOINT_URL")
api_key = os.getenv("API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "input_data": {
        "columns": [
            "school","sex","age","address","famsize","Pstatus",
            "Medu","Fedu","Mjob","Fjob","reason","guardian",
            "traveltime","studytime","failures","schoolsup",
            "famsup","paid","activities","nursery","higher",
            "internet","romantic","famrel","freetime","goout",
            "Dalc","Walc","health","absences"
        ],
        "data": [[
            "GP","F",18,"U","GT3","A",
            4,4,"at_home","teacher","course","mother",
            2,2,0,"yes","no","no","yes","yes",
            "yes","yes","no",4,3,4,
            1,1,3,6
        ]]
    }
}

response = requests.post(
    url,
    headers=headers,
    json=payload
)

print(response.status_code)
print(response.text)