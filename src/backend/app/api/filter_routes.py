from flask import Blueprint, request, jsonify
from app.services.entity_service import filter_entities
from app.utils.functools import error_handler

filter_routes = Blueprint("filter_routes", __name__)


@filter_routes.route("/<entity_name>", methods=["POST"])
# @error_handler
def filter_entities_route(entity_name):
    filters = request.get_json() or {}
    filters = filters['data']
    print(filters)
    new_filters = {}

    for key, value in filters.items():
        if key.endswith('__start') or key.endswith('__end'):
            new_filters[key] = value
        else:
            new_filters[f"{key}__icontains"] = value

    results = filter_entities(entity_name, new_filters)
    print(results)
    serialized = []
    for result in results:
        result_map = result.to_dict()
        result_map.update(result.get_relationships())
        serialized.append(result_map)
    print(serialized)

    return jsonify(serialized), 200
