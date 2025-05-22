from flask import Blueprint, jsonify

status_bp = Blueprint('status', __name__, url_prefix='/status')

# Simulated model status - in real case, this could come from a DB or service
MODEL_STATUS = "NOT_DEPLOYED"  # Change as needed: PENDING, DEPLOYING, RUNNING

@status_bp.route('/', methods=['GET'])
def get_model_status():
    if MODEL_STATUS not in {"NOT_DEPLOYED", "PENDING", "DEPLOYING", "RUNNING"}:
        return jsonify({"status": "error", "message": "Unknown model status" }), 500

    return jsonify({"status": MODEL_STATUS}), 200
