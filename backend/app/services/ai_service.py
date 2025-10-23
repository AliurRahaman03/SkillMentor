import os, requests, json


class AIService:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.url = 'https://api.openai.com/v1/chat/completions'


    def generate_roadmap(self, profile):
        prompt = f"Generate a 6-week learning roadmap for this profile: {profile}. Respond in JSON."
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}
        payload = {
        'model': 'gpt-4o-mini',
        'messages': [{'role': 'user', 'content': prompt}],
        'temperature': 0.2
        }
        res = requests.post(self.url, headers=headers, json=payload)
        data = res.json()
        try:
            content = data['choices'][0]['message']['content']
            return json.loads(content)
        except Exception:
            return {'title': 'Roadmap', 'weeks': {}}