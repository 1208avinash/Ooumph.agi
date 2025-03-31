# theory_of_mind_module.py
# Belief modeling module (ToM)
tom_code = '''
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Belief:
    holder: str
    statement: str

@dataclass
class ToMState:
    beliefs: Dict[str, List[Belief]]

class TheoryOfMind:
    def __init__(self):
        self.state = ToMState(beliefs={})

    def add_belief(self, holder: str, statement: str):
        belief = Belief(holder, statement)
        self.state.beliefs.setdefault(holder, []).append(belief)

    def get_beliefs(self, holder: str) -> List[str]:
        return [b.statement for b in self.state.beliefs.get(holder, [])]

    def holds_belief(self, holder: str, statement: str) -> bool:
        return any(b.statement == statement for b in self.state.beliefs.get(holder, []))
'''
with open("theory_of_mind_module.py", "w") as f:
    f.write(tom_code)

