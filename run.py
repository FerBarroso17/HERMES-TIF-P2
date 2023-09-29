from app import init_app

app = init_app()
app.secret_key = '141119'

if __name__ == "__main__":

    app.run()
