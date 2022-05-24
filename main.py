

from src.route.routers import app

if __name__ == '__main__':
    """
    init service
    """
    app.run_server(host="127.0.0.111", debug=True, port=5010)
