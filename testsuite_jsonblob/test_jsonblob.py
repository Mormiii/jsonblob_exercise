import pytest
from pytest_bdd import given,when,then,scenario, parsers
import requests as REST


url ='https://jsonblob.com/api/jsonBlob'

#@pytest.mark.skip("reason=currently we dont want to test this")
@scenario("features/jsonblob.feature","Create new blog post")
def test_create_new_blog():
    pass


#@pytest.mark.skip("reason=currently we dont want to test this")
@scenario("features/jsonblob.feature","Update the blog post")
def test_update_blog():
    pass


#@pytest.mark.skip("reason=currently we dont want to test this")
@scenario("features/jsonblob.feature","Delete the blog post")
def test_delete_blog():
    pass



@given("a testable API")
def arrange_requirements():
    print("\nThe API is ready to test")
    pass


@when("post request is received on endpoint with <body>", target_fixture = "resp")
def post_request(body):
    print("Sending a POST request to this url:",url)
    print("with body :",body)
    resp = REST.post(url, data =body )
    print("The response is :", resp)
    return resp


@when("put request is received on endpoint/blobId with <update_to_body>", target_fixture = "resp")
def put_request(body, id, update_to_body):
    url_with_id = url+ '/' + id
    print("Sending a PUT request to this url:", url_with_id)
    print("updating the body to:",update_to_body)
    resp = REST.put(url_with_id, data =update_to_body)
    print("The response is :", resp)
    return resp

@when("delete request is received on endpoint/blobId", target_fixture = "resp")
def delete_request(body, id):
    url_with_id = url+ '/' + id
    print("Sending a DELETE request to this url:", url_with_id)
    resp = REST.delete(url_with_id)
    print("The response is :", resp)
    return resp


@then("<expected_status> is responded")
def check_response(resp, expected_status):
    print("The response code is:",resp.status_code, "| and the expected status is:",expected_status )
    assert int(expected_status) == resp.status_code

@when("in the response blobId is found", target_fixture= "id")
@then("in the response blobId is found", target_fixture= "id")
def get_blobId(resp):
    #print(resp.headers)
    headers = resp.headers
    resp_location = str(headers.get("location"))
    resp_location_splitted = resp_location.split('/')
    id = resp_location_splitted[-1]
    print("returning id:",id)
    return id

