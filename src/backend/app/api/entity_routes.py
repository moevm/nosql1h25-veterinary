from flask import Blueprint, request, jsonify
from app.services.entity_service import filter_entities
from app.utils.functools import error_handler

filter_routes = Blueprint("filter_bp", __name__)


@filter_routes.route("/<entity_name>", methods=["GET"])
@error_handler
def filter_entities_route(entity_name):
    filters = request.get_json() or {}
    results = filter_entities(entity_name, filters)
    print(results)
    serialized = []
    for result in results:
        result_map = result.to_dict()
        result_map.update(result.get_relationships())
        serialized.append(result_map)

    return jsonify(serialized), 200
