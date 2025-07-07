import time
import requests

# === CONFIGURATION ===
OPENROUTER_API_KEY = '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'
TELEGRAM_BOT_TOKEN = '7872187986:AAGU5OISiKAcsYbgCtL101ikHhzObFJpfkI'
TELEGRAM_CHAT_ID = '1096672706'  # User ID for direct message testing

# === PROMPT ===
BIBLE_PROMPT = 'Share a unique, inspiring, and concise Bible fact, scripture, or Christian teaching. Include the scripture reference if possible.'

def generate_post(topic_prompt):
    url = 'https://openrouter.ai/api/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {OPENROUTER_API_KEY}',
        'Content-Type': 'application/json',
        'HTTP-Referer': 'https://openrouter.ai/',
        'X-Title': 'Telegram Poster Bot'
    }
    data = {
        'model': 'openrouter/auto',
        'messages': [
            {"role": "system", "content": "You are a helpful assistant that writes engaging social media posts."},
            {"role": "user", "content": topic_prompt}
        ],
        'max_tokens': 80,
        'temperature': 0.9
    }
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error generating post: {e}")
        return ""

def post_to_telegram(content):
    if not content:
        print("No content to post.")
        return
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': content
    }
    try:
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()
        print(f"Posted to Telegram: {content}")
    except Exception as e:
        print(f"Error posting to Telegram: {e}")

def main():
    while True:
        for i in range(3):
            unique_prompt = f"{BIBLE_PROMPT} (Fact #{int(time.time())}-{i})"
            post_content = generate_post(unique_prompt)
            post_to_telegram(post_content)
            time.sleep(20)  # Spread 3 posts evenly over 1 minute
        print("Waiting for the next minute batch...")

if __name__ == "__main__":
    main() 
