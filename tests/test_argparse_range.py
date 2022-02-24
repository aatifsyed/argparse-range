from argparse_range import range_action
import argparse
import pytest


def test_single_int_argument_in_range():
    parser = argparse.ArgumentParser()
    parser.add_argument("testarg", action=range_action(0, 1))
    args = parser.parse_args(["1"])
    assert args.testarg == 1
    assert isinstance(args.testarg, int)


def test_single_float_argument_in_range():
    parser = argparse.ArgumentParser()
    parser.add_argument("testarg", action=range_action(0.0, 1.0))
    args = parser.parse_args(["1"])
    assert args.testarg == 1.0
    assert isinstance(args.testarg, float)


def test_single_argument_below_range():
    parser = argparse.ArgumentParser()
    parser.add_argument("testarg", action=range_action(0, 1))
    with pytest.raises(SystemExit):
        parser.parse_args(["-1"])


def test_single_argument_above_range():
    parser = argparse.ArgumentParser()
    parser.add_argument("testarg", action=range_action(0, 1))
    with pytest.raises(SystemExit):
        parser.parse_args(["2"])


def test_multiple_arguments_all_in_range():
    parser = argparse.ArgumentParser()
    parser.add_argument("testarg", action=range_action(0, 1), nargs="*")
    args = parser.parse_args(["0", "1"])
    assert args.testarg == [0, 1]


def test_multiple_arguments_some_out_of_range():
    parser = argparse.ArgumentParser()
    parser.add_argument("testarg", action=range_action(0, 1), nargs="*")
    with pytest.raises(SystemExit):
        parser.parse_args(["0", "1", "2"])


def test_multiple_arguments_all_out_of_range():
    parser = argparse.ArgumentParser()
    parser.add_argument("testarg", action=range_action(0, 1), nargs="*")
    with pytest.raises(SystemExit):
        parser.parse_args(["2"])


def test_optional_argument_absent():
    parser = argparse.ArgumentParser()
    parser.add_argument("testarg", action=range_action(0, 1), nargs="?")
    args = parser.parse_args([])
    assert args.testarg == None


def test_optional_argument_present_in_range():
    parser = argparse.ArgumentParser()
    parser.add_argument("testarg", action=range_action(0, 1), nargs="?")
    args = parser.parse_args(["0"])
    assert args.testarg == 0


def test_optional_argument_present_out_of_range():
    parser = argparse.ArgumentParser()
    parser.add_argument("testarg", action=range_action(0, 1), nargs="?")
    with pytest.raises(SystemExit):
        parser.parse_args(["2"])


def test_explicit_type_in_range():
    parser = argparse.ArgumentParser()
    parser.add_argument("testarg", action=range_action(0, 1), type=float)
    args = parser.parse_args(["1"])
    assert args.testarg == 1
    assert isinstance(args.testarg, float)


def test_explicit_type_out_of_range():
    parser = argparse.ArgumentParser()
    parser.add_argument("testarg", action=range_action(0, 1), type=float)
    with pytest.raises(SystemExit):
        parser.parse_args(["2"])


def test_explicit_type_multiple_in_range():
    parser = argparse.ArgumentParser()
    parser.add_argument("testarg", action=range_action(0, 1), type=float, nargs="*")
    args = parser.parse_args(["0", "1"])
    assert args.testarg == [0, 1]
    for arg in args.testarg:
        assert isinstance(arg, float)


def test_explicit_type_multiple_some_out_of_range():
    parser = argparse.ArgumentParser()
    parser.add_argument("testarg", action=range_action(0, 1), type=float, nargs="*")
    with pytest.raises(SystemExit):
        parser.parse_args(["0", "1", "3"])


def test_default():
    parser = argparse.ArgumentParser()
    parser.add_argument("--testarg", action=range_action(0, 1), default=0)
    args = parser.parse_args([])
    assert args.testarg == 0


def test_default_overridden():
    parser = argparse.ArgumentParser()
    parser.add_argument("--testarg", action=range_action(0, 1), default=0)
    args = parser.parse_args(["--testarg", "1"])
    assert args.testarg == 1


def test_default_overridden_out_of_range():
    parser = argparse.ArgumentParser()
    parser.add_argument("--testarg", action=range_action(0, 1), default=0)
    with pytest.raises(SystemExit):
        parser.parse_args(["--testarg", "2"])
