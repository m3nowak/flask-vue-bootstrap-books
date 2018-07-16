from flask import Flask as OgFlask

class Flask(OgFlask):
    jinja_options = OgFlask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='{jinja{',  # Default is '{{', I'm changing this because Vue.js uses '{{' / '}}'
        variable_end_string='}jinja}',
    ))