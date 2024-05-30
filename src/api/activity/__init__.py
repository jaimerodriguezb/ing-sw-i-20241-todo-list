BASE_ROUTE = "activity"
BASE_ROUTE2 = "categorias"

def register_routes(api, root="api"):
    from .activity import api as activity_api
    from .categorias import api as categorias_api

    api.add_namespace(activity_api, path=f"/{root}/{BASE_ROUTE}")
    api.add_namespace(categorias_api, path=f"/{root}/{BASE_ROUTE2}")