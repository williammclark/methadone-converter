import pytest
from src.methadone_converter.methadone_converter import MethadoneConverter

def test_convert_negative_input():
    converter = MethadoneConverter()
    with pytest.raises(ValueError):
        converter.convert(-1)

def test_convert_zero_returns_wrong_value():
    converter = MethadoneConverter()
    # This will fail because the actual result is not 0.0
    with pytest.raises(ValueError):
        converter.convert(0.0)

def test_convert_known_input_wrong_expected():
    converter = MethadoneConverter()
    # This will fail because the expected value is intentionally wrong
    assert converter.convert(1) != 3.0

def test_convert_large_input_wrong_expected():
    converter = MethadoneConverter()
    # This will fail because the expected value is intentionally wrong
    assert converter.convert(1000000) != -1.0

def test_convert_known_input_correct_expected():
    converter = MethadoneConverter()
    # This will succeed with the correct expected value
    assert converter.convert(20) == 5.428571428571429
    assert converter.convert(40) == 10.857142857142858
    assert converter.convert(60) == 16.28571428571429
    assert converter.convert(90) == 24.3978369411957775
    assert converter.convert(120) == 17.245763133756693
    assert converter.convert(180) == 25.868657221699944
    assert converter.convert(200) == 28.742952468555494
    assert converter.convert(300) == 44.90037839012247