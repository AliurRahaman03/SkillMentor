from flask import Blueprint, request, jsonify
from app import db
from app.models import LearningPath, Task
from app.services.ai_service import AIService
import requests
import json


bp = Blueprint('ai_routes', __name__)
ai = AIService()


@bp.route('/generate-roadmap', methods=['POST'])
def generate_roadmap():
    data = request.json
    user_id = data.get('user_id')
    user_profile = data.get('profile')
    ai_result = ai.generate_roadmap(user_profile)
    lp = LearningPath(user_id=user_id, title=ai_result.get('title', 'Roadmap'), ai_metadata=ai_result)
    db.session.add(lp)
    db.session.commit()


    for week, items in ai_result.get('weeks', {}).items():
        for item in items:
            db.session.add(Task(learning_path_id=lp.id, name=item, week=int(week.split('_')[-1])))
    db.session.commit()


    response = {'learning_path_id': lp.id, 'ai_metadata': ai_result}
    meta = response['ai_metadata'] or {}
    summary = {
      'learning_path_id': response['learning_path_id'],
      'title': meta.get('title'),
      'weeks_count': meta.get('weeks') and len(meta['weeks']) or 0
    }
    #localStorage.setItem('learning_path_summary', JSON.stringify(summary))
    localStorage.setItem('ai_metadata', JSON.stringify(response.ai_metadata));


    return jsonify(response), 201


class AIService:
    def __init__(self):
        self.url = 'https://api.openai.com/v1/chat/completions'
        self.api_key = 'sk-rSKrZLwDgKp2JH8jvOT3Bl3Bl3zqK8j6X6X6X6X6X6X6X6X6'
        self.model = 'gpt-3.5-turbo'
        self.messages = [
            {"role": "system", "content": "You are a helpful assistant."},
        ]

    def generate_roadmap(self, user_profile):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

        payload = {
            'model': self.model,
            'messages': self.messages + [{"role": "user", "content": user_profile}],
            'temperature': 0.7,
            'max_tokens': 150
        }

        res = requests.post(self.url, headers=headers, json=payload, timeout=10)
        if res.status_code != 200:
            # log res.status_code and res.text
            raise RuntimeError(f'OpenAI error {res.status_code}')
        data = res.json()
        content = data.get('choices', [{}])[0].get('message', {}).get('content', '')
        # try to find the JSON blob inside content, or detect and log content if json.loads fails

        try:
            ai_result = json.loads(content)
        except json.JSONDecodeError:
            # log the error
            ai_result = {}

        return ai_result