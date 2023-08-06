import requests

url = "https://api.notion.com/v1/pages"
api_key="secret_kkzmCEQ4SH0ajJDWNsx4EMoxNdGXGAPSYkhmNgIFwVD"
parent_page_id="fad5f51e-75af-46ae-b23d-56e8f9db761f"

header={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

data={
	"parent": { "page_id": "fad5f51e-75af-46ae-b23d-56e8f9db761f" },
	"properties": {
		"title": {
      "title": [{ "type": "text", "text": { "content": "A note from your pals at Notion" } }]
		}
	},
	"children": [
    {
      "object": "block",
      "type": "paragraph",
      "paragraph": {
        "rich_text": [{ "type": "text", "text": { "content": "You made this page using the Notion API. Pretty cool, huh? We hope you enjoy building with us." } }]
      }
    }
  ]
}

r=requests.post(url=url,headers=header,json=data)
print(r.text)
