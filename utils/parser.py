import re, json

def extract_json_only(text):
    text = re.sub(r"```json|```", "", text)
    text = text.split("assistant")[-1].strip()

    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("JSON not found")

    return json.loads(match.group())