from functools import wraps
from flask import request, abort, session
from app.models import Users, Groups
import json

def set_endpoint(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        
        session["endpoint"] = request.endpoint
        return func(*args, **kwargs)
    return decorated_function

def create_perm(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        
        group_usr = session.get("groups_usr", None)
        if group_usr:
            if check_permit(group_usr, "CREATE") is False:
                abort(405)    
                
        return func(*args, **kwargs)
    return decorated_function

def read_perm(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        
        group_usr = session.get("groups_usr", None)
        if group_usr:
            if check_permit(group_usr, "READ") is False:
                abort(405)     
        
        return func(*args, **kwargs)
    return decorated_function

def update_perm(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        
        group_usr = session.get("groups_usr", None)
        if group_usr:
            if check_permit(group_usr, "UPDATE") is False:
                abort(405)
        
        return func(*args, **kwargs)
    return decorated_function

def delete_perm(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        
        group_usr = session.get("groups_usr", None)
        if group_usr:
            if check_permit(group_usr, "DELETE") is False:
                abort(405)
        
        return func(*args, **kwargs)
    return decorated_function

def query_db(group_usr: str) -> dict:
    
    dbase = Groups.query.filter(Groups.name_group == group_usr).first()
    if dbase: 
        return json.loads(dbase.perms)

def check_permit(groups_usr: list, PERM: str) -> bool:
    
    returns = False
    
    for grp in groups_usr:
    
        rotas = query_db(grp)
        checkroute = rotas.get(str(session["endpoint"]), None)
        if not checkroute:
            continue
        
        grant = list(checkroute['permissoes'])
        if any(PERM == perms for perms in grant):
            returns = True
            break
        
    return returns
        
    
            
        