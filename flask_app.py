from flask import Flask, request, jsonify
import query_data

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    question = data.get('question')
    response = query_data.main(question)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, use_reloader = False)
