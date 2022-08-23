from c_meet import app
import os

if __name__ == '__main__':
    if os.getenv("DEBUG"):
        app.run(host="0.0.0.0")
    else:
        app.run(host="0.0.0.0", ssl_context = ("ssl/server.crt", "ssl/server.key"))
