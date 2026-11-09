import sys


def greet(name: str, punctuation: str = "!") -> str:
    target = name.strip() if name and name.strip() else "world"
    return f"Hello, {target}{punctuation}"


def main() -> int:
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))
    return 0


def test_greet():
    assert greet("Hee") == "Hello, Hee!"


def test_greet_blank():
    assert greet(" ") == "Hello, world!"


def test_greet_punctuation():
    assert greet("Hee", ".") == "Hello, Hee."


if __name__ == "__main__":
    raise SystemExit(main())
