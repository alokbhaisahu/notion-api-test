import requests

url = "https://api.notion.com/v1/pages"

api_key="secret_kkzmCEQ4SH0ajJDWNsx4EMoxNdGXGAPSYkhmNgIFwVD"
parent_page_id="fad5f51e-75af-46ae-b23d-56e8f9db761f"

payload = {
    "parent": { "page_id": parent_page_id },
    "properties": {
		"title": {
      "title": [{ "type": "text", "text": { "content": "A note from your pals at Notion" } }]
		}
}
}
headers = {
    "Authorization": f"Bearer {api_key}",
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)