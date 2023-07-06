from dotenv import dotenv_values

values = dotenv_values(".env")

API_KEY=values["API_KEY"]
SECRET_KEY=values["SECRET_KEY"]
