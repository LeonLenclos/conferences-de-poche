import os
import datetime

import markdown
import yaml
import chevron
import pdfkit

def get_data():
    with open('data.yml', 'r') as file:
        data = yaml.safe_load(file)
        data['date'] = datetime.datetime.today().strftime('%d/%m/%Y')
        data['contenu'] = {}
        for file in os.listdir('contenu'):
            id = os.path.splitext(file)[0]
            with open(f"contenu/{file}", 'r') as md_file:
                text = md_file.read()
                html = markdown.markdown(text)
                data['contenu'][id] = html
        return data
        
def get_content(data, item_id):
    try:
        return data['contenu'][item_id]
    except KeyError:
        return make_error(f'Contenu de `{item_id}` introuvable dans mes contenus.')

def fill_template(template, data):
    with open(f'template/{template}.mustache', 'r') as template:
        return chevron.render(template, data)

def make_error(text):
    html = markdown.markdown(text)
    return fill_template('error', {'html':html})

def make_section(data, section_id): #unused
    html = get_content(data, section_id)
    section_data = {'id': section_id, 'html':html}
    return fill_template('section', section_data)

def make_conference(data, conference_id): #unused
    try:
        conference_data = next(c for c in data['conferences'] if c['id'] == conference_id)
    except StopIteration:
        return make_error(f'Conférence `{conference_id}` introuvable dans mes données.')
    
    conference_data['html'] = get_content(data, conference_id)
    return fill_template('conference', conference_data)

def make_item(data, item):
    html = get_content(data, item['id'])
    try:
        conference_data = next(c for c in data['conferences'] if c['id'] == item['id'])
    except StopIteration:
        conference_data = {}
    item_data = {'id': item['id'], 'html':html, 'conf':conference_data}
    return fill_template(item['type'], item_data)


def make_book(data, book):
    items = (make_item(data, item) for item in data['sommaires'][book])
    html = '\n'.join(items)
    return fill_template(book, data | {'html':html})

def write_book(data, book):
    with open(f"{book}.html", 'w') as file:
        file.write(make_book(data, book))
    make_pdf(book)

def make_pdf(book):
    options = {"enable-local-file-access": True}
    pdfkit.from_file(f"{book}.html", f"pdf/{book}.pdf", verbose=True, options=options)

if __name__ == '__main__':
    data = get_data()
    write_book(data, 'livre')
    write_book(data, 'dossier')
