import os
import markdown
import yaml
import chevron

def get_data():
    with open('data.yml', 'r') as file:
        data = yaml.safe_load(file)
        data['content'] = {}
        for file in os.listdir('content'):
            id = os.path.splitext(file)[0]
            with open(f"content/{file}", 'r') as md_file:
                text = md_file.read()
                html = markdown.markdown(text)
                data['content'][id] = html
        return data
        
def get_content(data, item_id):
    try:
        return data['content'][item_id]
    except KeyError:
        return make_error(f'Contenu de `{item_id}` introuvable dans mes contenus.')

def fill_template(template, data):
    with open(f'template/{template}.mustache', 'r') as template:
        return chevron.render(template, data)

def make_error(text):
    html = markdown.markdown(text)
    return fill_template('error', {'html':html})

def make_section(data, section_id):
    html = get_content(data, section_id)
    section_data = {'id': section_id, 'html':html}
    return fill_template('section', section_data)

def make_conference(data, conference_id):
    try:
        conference_data = next(c for c in data['conferences'] if c['id'] == conference_id)
    except StopIteration:
        return make_error(f'Conférence `{conference_id}` introuvable dans mes données.')
    
    conference_data['html'] = get_content(data, conference_id)
    return fill_template('conference', conference_data)

def make_item(data, item):
    if item['type'] == 'conference':
        return make_conference(data, item['id'])
    if item['type'] == 'section':
        return make_section(data, item['id'])

def make_book(data):
    items = (make_item(data, item) for item in data['sommaire'])
    html = '\n'.join(items)
    return fill_template('livre', data | {'html':html})

def write_book(data):
    with open('livre.html', 'w') as file:
        file.write(make_book(data))

if __name__ == '__main__':
    data = get_data()
    write_book(data)