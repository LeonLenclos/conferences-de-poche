import os
import datetime
import subprocess

import markdown
import yaml
import chevron
import pdfkit

def get_data():
    '''Return the content of data.yml (also add the current date)'''
    with open('data.yml', 'r') as file:
        data = yaml.safe_load(file)
        data['date'] = datetime.datetime.today().strftime('%d/%m/%Y')
        for d in data['documents'] :
            if d['document'] == 'livre':
              data['sommaire'] = [{'id':item['id'], 'title':get_conference(item['id'], data)['titre']} for item in d['sommaire'] if item['template'] == 'livre/conference']
        return data

def get_document(doc):
    '''Return data of given document'''
    data = get_data()
    try:
        return next(d for d in data['documents'] if d['document'] == doc)
    except StopIteration:
        return {}

def get_conference(conf, data=None):
    '''Return data of ginven conf'''
    data = data or get_data()
    try:
        return next(c for c in data['conferences'] if c['id'] == conf)
    except StopIteration:
        return {}

def get_content(item_id):
    '''Get the markdown file corresponding to passed id, convert it to html and return it'''
    try:
        with open(f"contenu/{item_id}.md", 'r') as md_file:
            text = md_file.read()
            html = markdown.markdown(text)
            return html
    except OSError:
        return make_error(f'Contenu de `{item_id}` introuvable dans mes contenus.')

def fill_template(template, data):
    '''Get the template corresponding to passed name, fill it with passed data and return it'''
    with open(f'template/{template}.mustache', 'r') as template:
        return chevron.render(template, data)

def make_error(text):
    '''Generate html code for an error with the passed text'''
    html = markdown.markdown(text)
    return fill_template('error', {'html':html})


def make_chapter(chapter):
    '''Return the html corresponding to the given chapter'''
    fill_data = get_data()
    fill_data['id'] = chapter['id']
    fill_data['html'] = get_content(chapter['id'])
    fill_data['conf'] = get_conference(chapter['id'])
    if not chapter['template'] :
      return fill_data['html']
    return fill_template(chapter['template'], fill_data)


def make_document(document):
    '''Return the html corresponding to the given document'''
    data = get_data()
    chapters = (make_chapter(chapter) for chapter in document['sommaire'])
    html = '\n'.join(chapters)
    if not document['template'] :
      return html
    return fill_template(document['template'], data | {'html':html})


def export_html(document):
    doc = make_document(document)
    html_file = document['dist']['html']
    with open(html_file, 'w') as file:
        file.write(doc)
    return html_file

def export_pdf(document):
    html_file = export_html(document)
    pdf_file = document['dist']['pdf']
    subprocess.call(['sh', './make-pdf.sh', html_file, pdf_file])
    return pdf_file

def dist_document(document):
    '''Generate and save the document'''
    export_html(document)
    if 'pdf' in document['dist'] :
        export_pdf(document)
    return document['document']

def dist_all():
    data = get_data()
    for document in data['documents']:
      dist_document(document)
    return 'oui!'

if __name__ == '__main__':
    dist_all()
