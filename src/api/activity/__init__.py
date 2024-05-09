BASE_ROUTE = "activity"

def register_routes(api, root="api"):
    from .activity import api as activity_api

    api.add_namespace(activity_api, path=f"/{root}/{BASE_ROUTE}")