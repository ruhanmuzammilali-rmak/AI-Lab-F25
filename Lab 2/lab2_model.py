# lab 2 

class SmartClassroomAgent:
    def __init__(self):
        self.lastTarget = None
    def choose_mode(self, temp, roomStatus):

        # agar room khali hai to ECO mode use hoga.
        if roomStatus == False:
            mode = "ECO"
        elif temp > 26:
            mode = "COOL"
        elif temp < 20:
            mode = "WARM"
        else:
            mode = "IDLE"
        return mode
    def update(self, temp, roomStatus):

        # purana target mode ko save karte he.
        oldTarget = self.lastTarget
        newTarget = self.choose_mode(temp, roomStatus)
        if oldTarget != newTarget:
            commandStatus = "send command"
        else:
            commandStatus = "no command"
        self.lastTarget = newTarget
        return oldTarget, newTarget, commandStatus
def test_classroom(label, input):
    classroom = SmartClassroomAgent()
    print("\n" + label)
    print(f"{'Step':<6}{'Previous':<12}{'Percept':<16}"f"{'Target':<10}Outcome")
    print("-" * 60)
    for number, (temp, occup) in enumerate(input, start=1):
        old, target, result = classroom.update(temp, occup)

        print(f"{number:<6}{str(old):<12}"
              f"{str((temp, occup)):<16}"
              f"{target:<10}{result}")
# different test for checking agent.
if __name__ == "__main__":
    test_classroom(
        "Repeated percept",
        [(29, True), (29, True), (29, True)]
    )
    test_classroom(
        "Temperature boundarie",
        [(20, True), (26, True)]
    )
    test_classroom(
        "Transition mode",
        [(29, True), (24, True), (19, True), (29, True)]
    )
    test_classroom(
        "empty room",
        [(29, True), (29, False), (15, False), (29, True)]
    )
    test_classroom(
        "Required input sequence",
        [(29, True), (29, True), (20, True),
         (26, True), (19, True), (29, False)]
    )
    test_classroom(
        "Temperature change near 26",
        [(26.2, True), (25.8, True),
         (26.3, True), (25.7, True)]
    )