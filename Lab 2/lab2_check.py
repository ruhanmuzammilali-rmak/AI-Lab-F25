from lab2_percept import ClassroomAgent
from lab2_model import SmartClassroomAgent
reflex = ClassroomAgent()
test = [
    ((29, True), "COOL"),
    ((20, True), "IDLE"),
    ((26, True), "IDLE"),
    ((19, True), "WARM"),
    ((29, False), "ECO"),
    ((15, False), "ECO")
]
for percept, expected in test:
    assert reflex.act(*percept) == expected, percept

print("Reflex agent: all", len(test), "check passed")
s = SmartClassroomAgent()
assert s.update(29, True) == (None, "COOL", "send command")
assert s.update(29, True) == ("COOL", "COOL", "no command")
assert s.update(24, True) == ("COOL", "IDLE", "send command")
assert s.update(29, False) == ("IDLE", "ECO", "send command")
assert s.update(15, False) == ("ECO", "ECO", "no command")
print("Stateful agent: all check passed")