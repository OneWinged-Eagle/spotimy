from typing import Any, List


def chunker(seq: List[Any], size: int) -> List[List[Any]]:
	return (seq[pos:pos + size] for pos in range(0, len(seq), size))
