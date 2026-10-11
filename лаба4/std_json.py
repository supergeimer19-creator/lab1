import json

def test_json():
    data = {"project": "Lab4", "status": "Ready"}
    json_str = json.dumps(data)
    print(f"json: Серіалізований рядок -> {json_str}")