from flask import Flask, request
from rainbond_python.parameter import Parameter
from rainbond_python.error_handler import error_handler
from rainbond_python.db_connect import DBConnect

app = Flask(__name__)
error_handler(app)

db_books = DBConnect(db='demo', collection='books')


@app.route('/api/v1/demo', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_v1_demo():
    parameter = Parameter(request)

    if parameter.method == 'GET':
        find_data = db_books.find_paging(parameter)
        return find_data

    elif parameter.method == 'POST':
        param = parameter.verification(
            checking=parameter.param_json,
            verify={'title': str, 'author': str}
        )
        new_id = db_books.write_one_docu(docu=param)
        return {'new_id': new_id}

    elif parameter.method == 'PUT':
        param = parameter.verification(
            checking=parameter.param_json,
            verify={'id': str, 'title': str, 'author': str}
        )
        update_result = db_books.update_docu(
            find_docu={'id': param['id']},
            modify_docu={'title': param['title'], 'author': param['author']}
        )
        return update_result

    elif parameter.method == 'DELETE':
        param = parameter.verification(
            checking=parameter.param_json,
            verify={'id': str}
        )
        delete_result = db_books.delete_docu(find_docu=param)
        return delete_result


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
