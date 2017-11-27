from flask import Flask, jsonify, request, make_response
import json
from search import query_api, is_url_valid, validate_string
from decorators import check_error_handler
from mongo import convert_args_to_mongo_query, query

# create the Flask application
app = Flask(__name__)

def init_api_routes(app_ref):
    if app_ref:
        app_ref.add_url_rule('/search', 'search_string',
                             search_string, methods=['GET'])
        app_ref.add_url_rule('/url', 'search_url',
                             search_url, methods=['GET'])


@check_error_handler
def search_string():
    """
    Get string search
    :return: code 200 and json if ok, 400 if malformed string
    """
    src_str = request.form['search']
    is_valid_str = validate_string(src_str)

    if is_valid_str:
        my_url = query_api(src_str)
        is_valid_url = is_url_valid(my_url)

        if my_url != "" and is_valid_url:
            return jsonify({"url": my_url})
        else:
            return make_response(jsonify({"Error": "search url is not valid!"}), 400)

    return make_response(jsonify({"Error": "search string is not valid!"}), 400)


@check_error_handler
def search_url():
    """
    Perform a search into mongo db table
    :param url:
    :return:
    """
    args_dict = json.loads(json.dumps(request.args))
    mongo_query = convert_args_to_mongo_query(args_dict)
    # response = query(mongo_query)
    response = []
    # print(mongo_query)

    return jsonify({"response": "ok", "results": response})


init_api_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
