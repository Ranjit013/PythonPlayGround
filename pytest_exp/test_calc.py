import argparse


def test_add():
    a = 5
    b = 6
    sum = a + b
    assert 11 == sum


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
