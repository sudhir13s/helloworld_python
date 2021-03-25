import os


def hello_world():
    api_key = os.environ.get("SECRET_KEY")
    if api_key:
        print("hello world!")
        return "OK"
    return "Error"


if __name__ == "__main__":
    print(hello_world)
