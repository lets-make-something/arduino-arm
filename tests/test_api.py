from arduino-arm import api
import pytest

@pytest.mark.django_db(transaction=True)
def test_api():
  obj = api.Arm()
  assert 1 == obj.one()
