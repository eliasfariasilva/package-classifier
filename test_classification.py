from classifier import classifier

def run_tests():
    assert classifier(100, 100, 100, 10) == "SPECIAL"
    assert classifier(120, 120, 70, 25) == "REJECTED"
    assert classifier(200, 50, 50, 5) == "SPECIAL"
    assert classifier(160, 160, 160, 25) == "REJECTED"
    assert classifier(50, 50, 50, 10) == "STANDARD"
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()