from bottle import static_file
from bottle import route, run

import make

@route('/content/<content_id>')
def content(content_id):
    return make.get_content(content_id)



@route('/live/<doc>')
def live(doc):
    return make.make_document(make.get_document(doc));

@route('/dist', method=['GET', 'POST'])
def dist_all():
    return make.dist_all();

@route('/dist/<doc>', method=['GET', 'POST'])
def dist(doc):
    return make.dist_document(make.get_document(doc));

@route('/export_pdf/<doc>', method=['GET', 'POST'])
def export_pdf(doc):
    return make.export_pdf(make.get_document(doc));

@route('/export_html/<doc>', method=['GET', 'POST'])
def export_html(doc):
    return make.export_html(make.get_document(doc));

@route('/')
def index():
    return server_static('index.html');

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=".")


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
