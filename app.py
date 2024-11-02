from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Replace with your actual OpenAI API key
openai.api_key = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    # Call the OpenAI API with a system prompt for the UMPIRE method
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI assistant that helps students prepare for technical interviews using the UMPIRE method. "
                    "Guide the student systematically through the steps of Understand, Match, Plan, Implement, Review, and Evaluate."
                )
            },
            {"role": "user", "content": user_message}
        ]
    )
    reply = response.choices[0].message.content.strip()
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
