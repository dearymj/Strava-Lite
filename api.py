from flask_restful import Resource, reqparse
from uuid import uuid4

class UserListResource(Resource):
    def __init__(self, data_store):
        self.data_store = data_store

    def get(self):
        # This get method now corresponds to GET /users
        # Return only "id", "name", "age"
        users_list = []
        for u in self.data_store["users"].values():
            users_list.append({
                "id": u["id"],
                "name": u["name"],
                "age": u["age"]
            })
        return {"users": users_list}, 200

    def post(self):
        # This post method corresponds to POST /user
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True, help="Name is required")
        parser.add_argument("age", type=int, required=False)
        args = parser.parse_args()

        user_id = str(uuid4())
        self.data_store["users"][user_id] = {
            "id": user_id,
            "name": args["name"],
            "age": args["age"],
            "workouts": [],
            "following": set()
        }

        # Return only "id", "name", "age"
        user = self.data_store["users"][user_id]
        user_serializable = {
            "id": user["id"],
            "name": user["name"],
            "age": user["age"]
        }

        return user_serializable, 200

class UserResource(Resource):
    def __init__(self, data_store):
        self.data_store = data_store

    def get(self, user_id):
        # GET /user/<user_id>
        user = self.data_store["users"].get(user_id)
        if not user:
            return "", 404
        user_serializable = {
            "id": user["id"],
            "name": user["name"],
            "age": user["age"]
        }
        return user_serializable, 200

    def delete(self, user_id):
        # DELETE /user/<user_id>
        if user_id not in self.data_store["users"]:
            return "", 404
        del self.data_store["users"][user_id]
        return "", 200
