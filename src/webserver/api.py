from flask import jsonify, request

import data
import overlay


def init(app):
    @app.route("/api/logs", methods=["GET"])
    def get_logs():
        return jsonify(overlay.overlay.logs)

    @app.route("/api/stats", methods=["GET"])
    def get_stats():
        return jsonify(
            {
                "games": data.games,
                "xp": data.xp,
                "bloodpoints": data.bloodpoints,
                "iri_shards": data.iri_shards,
                "starting_iri_shards": data.starting_iri_shards,
                "time_in_game": data.total_time_in_game,
            }
        )

    @app.route("/api/settings", methods=["POST"])
    def update_settings():
        body = request.json

        data.config.set_json(body)

        return jsonify({"status": "success", "message": "Settings updated!"})

    @app.route("/api/settings", methods=["GET"])
    def get_settings():
        return data.config.get_json()

    @app.route("/api/killers", methods=["GET"])
    def get_killers():
        return jsonify([killer.name for killer in data.Killer])
