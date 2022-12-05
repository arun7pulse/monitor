import json
with open("config.json", "r") as jsonfile:
        data = json.load(jsonfile)

if __name__ == '__main__':
    print("Read successful")
    print(data)