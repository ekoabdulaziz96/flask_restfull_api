from app import create_app

app = create_app()

def try_print_log(app):
    print('print_log')
    app.logger.debug('print_log_debug')

@app.route('/', methods=['GET'])
def index():
    try_print_log(app)
    return 'core-tcico', 200
