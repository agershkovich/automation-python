import pytest


@pytest.yield_fixture()
def resource_setup():
    print("resource_setup")
    yield
    print("resource_teardown")


def test_1_that_needs_resource(resource_setup):
    print("test_1_that_needs_resource")


def test_2_that_does_not():
    print("test_2_that_does_not")


def test_3_that_does_again(resource_setup):
    print("test_3_that_does_again")
