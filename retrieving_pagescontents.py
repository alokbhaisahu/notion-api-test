#page is a special "block" so page id can acts a block id i guess
import requests
block_id="4e965cca-a743-447f-901f-3ed6a0ef6c02"
url=f"https://api.notion.com/v1/blocks/{block_id}/children"
api_key="secret_kkzmCEQ4SH0ajJDWNsx4EMoxNdGXGAPSYkhmNgIFwVD"

headers = {
    "Authorization": f"Bearer {api_key}",
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "content-type": "application/json"
}
response = requests.get(url, headers=headers)

print(response.text)