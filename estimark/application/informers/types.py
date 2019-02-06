from typing import List, Dict, Union, Tuple


TermTuple = Tuple[str, str, Union[str, int, float, bool, list, tuple]]

SearchDomain = List[Union[str, TermTuple]]

RecordsList = List[Dict[str, str]]
