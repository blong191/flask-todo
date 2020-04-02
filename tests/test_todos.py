import pytest

def test_todo_list(client):
    # View the home page and check to see the header and a to-do item
    response = client.get('/')
    assert b'<h1>A simple to-do application</h1>' in response.data
    assert b'clean room' in response.data

    # Mock data should show three to-do items, one of which is complete
    assert response.data.count(b'<li class="">') == 2
    assert response.data.count(b'<li class="completed">') == 1

def test_new_post(client,):
    #adds a new task to the page
    client.post('/', data={'description': 'bigbrain'})
    #gets the page
    response = client.get('/')
    #tests that the new response exists
    assert b'bigbrain' in response.data
