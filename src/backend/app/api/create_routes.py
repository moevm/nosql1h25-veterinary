from flask import Blueprint, request, jsonify
from app.services.entity_service import create_entity
from app.utils.functools import error_handler

create_routes = Blueprint("create_routes", __name__)


@create_routes.route("/<entity_name>", methods=["GET"])
@error_handler
def filter_entities_route(entity_name):
    data = request.get_json() or {}
    results = create_entity(entity_name, data)
    print(results)
    serialized = []
    for result in results:
        result_map = result.to_dict()
        result_map.update(result.get_relationships())
        serialized.append(result_map)

    return jsonify(serialized), 200
