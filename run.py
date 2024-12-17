from app import create_app

app = create_app()

app.secret_key = '8b5038564c0599aa1fb8d40335770b5d'


if __name__ == '__main__':
    app.run(debug=True)
    