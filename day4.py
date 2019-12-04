import re
double_pattern = re.compile(r"([0-9])\1")

password_range = range(264793, 803935+1)

def has_double(number:int) -> bool:
  r = double_pattern.search(str(number))
  return False if r is None else True

def is_increasing(number:int) -> bool:
  return str(number) == "".join(sorted(str(number)))

print(len([p for p in password_range if all((has_double(p), is_increasing(p)))]))