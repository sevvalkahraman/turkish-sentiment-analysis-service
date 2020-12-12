import optparse
from config import FlaskConfig as Config


def flaskrun(app, default_host=Config.DEFAULT_HOST, default_port=Config.DEFAULT_PORT):
    """
    Takes a flask.Flask instance and runs it. Parses
    command-line flags to configure the app.
    """

    # Set up the command-line options
    parser = optparse.OptionParser()
    msg = 'Hostname of Flask app [{}]'.format(default_host)
    parser.add_option("-H", "--host",
                      help=msg,
                      default=default_host)
    msg = 'Port for Flask app [{}]'.format(default_port)
    parser.add_option("-P", "--port",
                      help=msg,
                      default=default_port)
    parser.add_option("-d", "--debug",
                      action="store_true", dest="debug",
                      help=optparse.SUPPRESS_HELP)

    options, _ = parser.parse_args()

    app.run(
        debug=options.debug,
        host=options.host,
        port=int(options.port)
    )