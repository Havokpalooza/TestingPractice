class ScoreMachine:
    def __init__(self):
        pass
    
    def aces(self,rolls):
        total = 0
        for item in rolls:
            if item == 1:
                total += item
        return total
    
    def twos(self,rolls):
        total = 0
        for item in rolls:
            it item == 2:
                total += item
        return total
    
def testAces():
    x = ScoreMachine()
    assert 5 == x.aces([1,1,1,1,1])
    assert 4 == x.aces([1,1,1,1])
    
    print("Aces tests passed!")
    
def testTwos():
    x = ScoreMachine()
    assert 0 == x.twos([1,3,4,1,5])
    assert 3 == x.twos([2,1,2,3,2])
    assert 5 == x.twos([2,2,2,2,2])
    
