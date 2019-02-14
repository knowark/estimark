from typing import List, Dict, Any, Tuple
from pathlib import Path
from .rst_analyzer import RstAnalyzer


class RstLoader:

    def __init__(self, root: str, analyzer: RstAnalyzer) -> None:
        self._nodes: Dict[str, Any] = {}
        self.root = root
        self.analyzer = analyzer

    @property
    def nodes(self):
        return self._nodes

    def load(self):
        path = Path(self.root)

        for node in path.rglob('*.rst'):
            data = self._analyze_node(node)
            metadata = {
                'name': node.name,
                'parent': node.parent.absolute
            }
            self._nodes[node.absolute] = {**metadata, **data}

    def _analyze_node(self, node: Path) -> Dict[str, Any]:
        data_dict = self._extract_content(node)
        return data_dict

    def _extract_content(self, node: Path) -> Dict[str, Any]:
        content = node.read_text()
        return self.analyzer.analyze(content)
