import json


class ReadJson(object):
    def __init__(self, filename):
        self.filepath = "../data/" + filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)


if __name__ == "__main__":
    print(ReadJson("login.json").read_json())
