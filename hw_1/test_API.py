import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step_1(login):
    response = requests.get(data['website_2'], headers={'X-Auth-Token': login}, params={"owner": "notMe"})
    titles = [i["title"] for i in response.json()['data']]
    assert response.status_code == 200 and data['search_title'] in titles


def test_step_2(login):
    response_post = requests.post(data['website_3'], headers={'X-Auth-Token': login},
                                  data={'title': data['post_title'], 'description': data['post_description'],
                                        'content': data['post_content']})
    response_get = requests.get(data['website_2'], headers={'X-Auth-Token': login})
    descriptions = [i["description"] for i in response_get.json()['data']]
    if response_post.status_code == response_get.status_code == 200:
        assert data['post_description'] in descriptions
