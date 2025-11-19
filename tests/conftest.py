import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
pytest_plugins = (
'utils.fixtures.device_fixtures',
)
