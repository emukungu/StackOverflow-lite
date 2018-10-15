from .baseRoutes import jsonify, status, app, cur, conn
from .login import jwt_required, get_jwt_identity, get_raw_jwt, login

@app.route('/api/v1/logout', methods = ['GET'])
def logout():
    return jsonify({"message":"You have successfully logged out."}), 200