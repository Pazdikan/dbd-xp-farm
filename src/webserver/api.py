from flask import jsonify, request

import data


logs = [
    "Log entry 1",
    "Log entry 2",
    "Log entry 3"
]

stats = [
    "Game Started",
    "Player 1: 100 points",
    "Player 2: 150 points"
]

def init(app):
    @app.route('/api/logs', methods=['GET'])
    def get_logs():
        return jsonify(logs)

    @app.route('/api/stats', methods=['GET'])
    def get_stats():
        return jsonify(stats)

    @app.route('/api/settings', methods=['POST'])
    def update_settings():
        body = request.json

        data.config.set_json(body)

        return jsonify({"status": "success", "message": "Settings updated!"})

    @app.route('/api/settings', methods=['GET'])
    def get_settings():
        return data.config.get_json()
    
    @app.route('/api/killers', methods=['GET'])
    def get_killers():
        return jsonify([killer.name for killer in data.Killer])