from bottle import static_file
from bottle import route, run

import make

@route('/hello')
def hello():
    return "Hello World!"

@route('/livre')
def livre():
    data = make.get_data()
    return make.make_book(data)

@route('/content/<content_id>')
def content(content_id):
    data = make.get_data()
    return make.get_content(data, content_id)


@route('/page/<page_id>')
def page(page_id):
    data = make.get_data()
    return make.fill_template(page_id, data)

@route('/')
def index():
    return page('index');

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=".")


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)