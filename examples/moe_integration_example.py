import requests
response = requests.post("http://localhost:5000/run_pipeline", json={"repo": "moe_repo", "version": "3.7"})
print(response.json())
