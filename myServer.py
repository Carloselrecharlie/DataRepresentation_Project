from flask import Flask, jsonify, request, abort
from watchDAO import watchDAO

app = Flask(__name__, static_url_path='', static_folder='.')


#curl "http://127.0.0.1:5000/watches"
@app.route('/watches')
def getAll():
    results = watchDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/watches/2"
@app.route('/watches/<int:id>')
def findById(id):
	foundwatch = watchDAO.findByID(id)
	if not foundwatch:
		return jsonify(foundwatch),204
	return jsonify(foundwatch)

#curl -i -H "Content-Type:application/json" -X POST -d "{\"Gender\":\"women\",\"Display\":\"digital\",\"Price\":123}" http://127.0.0.1:5000/watches
@app.route('/watches', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    watch = {
        "Gender": request.json['Gender'],
        "Display": request.json['Display'],
        "Price": request.json['Price'],
    }
    values =(watch['Gender'],watch['Display'],watch['Price'])
    newId = watchDAO.create(values)
    watch['id'] = newId
    return jsonify(watch)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Gender\":\"women\",\"Display\":\"digital\",\"Price\":456}" http://127.0.0.1:5000/watches/2
@app.route('/watches/<int:id>', methods=['PUT'])
def update(id):
    foundwatch = watchDAO.findByID(id)
    if not foundwatch:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)

    if 'Gender' in reqJson:
        foundwatch['Gender'] = reqJson['Gender']
    if 'Display' in reqJson:
        foundwatch['Display'] = reqJson['Display']
    if 'Price' in reqJson:
        foundwatch['Price'] = reqJson['Price']
    values = (foundwatch['Gender'],foundwatch['Display'],foundwatch['Price'],foundwatch['id'])
    watchDAO.update(values)
    return jsonify(foundwatch)


@app.route('/watches/<int:id>' , methods=['DELETE'])
def delete(id):
    watchDAO.delete(id)
    return jsonify({"done":True})


if __name__ == '__main__' :
    app.run(debug= True)