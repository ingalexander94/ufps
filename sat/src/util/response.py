from flask import jsonify

def sendError(msg, codeStatus):
    return jsonify({"ok":False,"data": None,"msg": msg}), codeStatus
    
def sendSuccess(msg, data, codeStatus=200):
    return jsonify({"ok":True,"data":data,"msg":msg}), codeStatus

def sendToken(current_user, token):
    return jsonify({"ok":True, "user": current_user, "token":token})