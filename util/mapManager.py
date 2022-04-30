import json


def addMap(name, mapUid):
    with open("../data/maps.json", "r") as f:
        maps = json.load(f)

    maps["playlist"].append(
        {
            "name": name,
            "id": maps["maxId"] + 1,
            "mapUid": mapUid
        }
    )

    maps["maxId"] += 1

    with open("../data/maps.json", "w") as f:
        json.dump(maps, f, indent=4)

    # Todo : Send confirmation message


def modifyMap(id, newName, newMapUid):
    with open("../data/maps.json", "r") as f:
        maps = json.load(f)

    index = next((i for i, item in enumerate(maps["playlist"]) if item["id"] == id), None)

    maps["playlist"][index]["name"] = newName
    maps["playlist"][index]["mapUid"] = newMapUid

    with open("../data/maps.json", "w") as f:
        json.dump(maps, f, indent=4)

    # Todo : Send confirmation message


def printMaps():
    with open("../data/maps.json", "r") as f:
        maps = json.load(f)


if __name__ == "__main__":
    addMap('test map', 'wrong uid')

    modifyMap(9, "modified","pareil")