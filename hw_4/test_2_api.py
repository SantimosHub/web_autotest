import logging
import requests
import yaml

with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

S = requests.Session()


def test_post_create(user_login):
    logging.info("Test1_api Starting")
    res = S.post(url=testdata['address_post'], headers={'X-Auth-Token': user_login},
                 data={'title': testdata['title'], 'description': testdata['description'],
                       'content': testdata['content']})
    logging.info(f"Response is {str(res)}")
    assert str(res) == '<Response [200]>', 'post_create FAIL'


def test_check_post_create(user_login):
    logging.info("Test2_api Starting")
    result = S.get(url=testdata['api_address'], headers={'X-Auth-Token': user_login}).json()['data']
    logging.info(f"get request return: {result}")
    list_description = [i['description'] for i in result]
    assert testdata['description'] in list_description, 'check_post_create FAIL'


def test_check_notme_post(user_login):
    logging.info("Test3_api Starting")
    result = S.get(url=testdata['api_address'], headers={'X-Auth-Token': user_login}, params={'owner': 'notMe'}).json()[
        'data']
    logging.info(f"get request return: {result}")
    result_title = [i['title'] for i in result]
    assert testdata['not_me_title'] in result_title, 'check not me post FAIL'
