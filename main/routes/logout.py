from .baseRoutes import jsonify, status, app, cur, conn
from .login import jwt_required, get_jwt_identity, login

@app.route('/api/v1/logout', methods = ['GET'])
def logout():
    cur.close()
    conn.close()

    return jsonify({"message":"You have successfully logged out."})