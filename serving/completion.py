from flask import Blueprint, request, jsonify

completion_bp = Blueprint('completion', __name__, url_prefix='/completion')

@completion_bp.route('/', methods=['POST'])
def handle_completion():
    try:
        data = request.get_json(force=True)
        messages = data.get('messages', [])

        if not messages or messages[0].get('role') != 'user':
            return jsonify({"status": "error", "message": "Invalid request format. Expected a 'user' message." }), 400

        user_message = messages[0].get('content', '')
        assistant_reply = f"Echo: {user_message}"  # Replace with actual logic

        return jsonify({ "status": "success", "response": [{"role": "assistant", "message": assistant_reply}]}), 200

    except Exception as e:
        return jsonify({"status": "error","message": f"An error occurred: {str(e)}" }), 500
