from flask import request, jsonify

def register_routes(app, data_store):
    @app.route("/workouts/<user_id>", methods=["PUT"])
    def add_workout(user_id):
        user = data_store["users"].get(user_id)
        if not user:
            return "", 404

        body = request.get_json()
        if not body or "date" not in body or "time" not in body or "distance" not in body:
            return "", 400

        workout = {
            "date": body["date"],
            "time": body["time"],
            "distance": body["distance"]
        }
        user["workouts"].append(workout)
        return jsonify(workout), 200

    @app.route("/workouts/<user_id>", methods=["GET"])
    def list_workouts(user_id):
        user = data_store["users"].get(user_id)
        if not user:
            return "", 404
        return jsonify({"workouts": user["workouts"]}), 200

    # Extra Credit: FollowFriend
    @app.route("/follow-list/<user_id>", methods=["PUT"])
    def follow_friend(user_id):
        user = data_store["users"].get(user_id)
        if not user:
            return "", 404

        body = request.get_json()
        if not body or "follow_id" not in body:
            return "", 400

        follow_id = body["follow_id"]
        friend = data_store["users"].get(follow_id)
        if not friend:
            return "", 404

        user["following"].add(follow_id)
        return jsonify({"following": list(user["following"])}), 200

    # Extra Credit: ShowFriendWorkouts
    @app.route("/follow-list/<user_id>/<follow_id>", methods=["GET"])
    def show_friend_workouts(user_id, follow_id):
        user = data_store["users"].get(user_id)
        friend = data_store["users"].get(follow_id)
        if not user or not friend:
            return "", 404

        if follow_id not in user["following"]:
            return "", 403

        return jsonify({"workouts": friend["workouts"]}), 200
