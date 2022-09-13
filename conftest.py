import pytest


@pytest.fixture(scope="function")
def skip_if_already_failed(request, failed=set()):
    key = request.node.name.split("[")[0]
    failed_before = request.session.testsfailed
    if key in failed:
        pytest.skip("previous test {} failed".format(key))
    yield
    failed_after = request.session.testsfailed
    if failed_before != failed_after:
        failed.add(key)
