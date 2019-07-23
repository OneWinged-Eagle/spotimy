import json
import numpy as np
from typing import Any

class NumpyEncoder(json.JSONEncoder):

	def default(self, obj: Any) -> Any:
		if isinstance(obj, np.ndarray):
			return obj.tolist()
		return json.JSONEncoder.default(self, obj)
