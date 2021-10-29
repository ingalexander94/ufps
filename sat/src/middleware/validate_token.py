import jwt
from flask import request
from functools import wraps
from util import response, environment

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if "x-token" in request.headers:
            token = request.headers["x-token"]
            
        if not token:
            return response.sendError("a valid token is missing", 401)
        
        try:
          data = jwt.decode(token, environment.SECRET_KEY, algorithms=["HS256"])
          current_user = data["payload"] 
        except:
            return response.sendError("token is invalid", 401)
        return f(current_user, *args, **kwargs)
    return decorator
          