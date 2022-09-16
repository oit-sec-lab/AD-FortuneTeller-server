import json

# receive json array
json_array = '[{"id":1, "URL":"https://hogehoge"},{"id":2, "URL":"https://foo"}]'

def Json2Dict(data):
    j2p_data = json.loads(data)

    url_dict = {}

    for d in j2p_data:
        index = d['id']
        url = d['URL']
        url_dict[index] = url

    return url_dict


if __name__ == "__main__":
    print(Json2Dict(json_array))
