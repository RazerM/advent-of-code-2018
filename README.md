# Installation

```bash
git clone https://github.com/RazerM/advent-of-code-2018
cd advent-of-code-2018
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

# Running

```bash
./aoc.py 1 input/1.txt
```

# Tests

```bash
pip install -e .[test]
pytest tests/
```