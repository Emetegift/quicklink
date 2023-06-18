# from api import create_app
# from api.config.config import config_dict


# app = create_app(config=config_dict['dev'])


# if __name__=="__main__":
#     app.run()


from api import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
