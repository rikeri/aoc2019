import re
double_pattern = re.compile(r"([0-9])\1")
double_nothree = re.compile(r"([0-9])(\1+)")

password_range = range(264793, 803935+1)

def has_double(number:int) -> bool:
  r = double_pattern.search(str(number))
  return False if r is None else True

def has_double_stricter(number: int) -> bool:
  r = double_nothree.findall(str(number))
  if not r:
    return False
  for _, match in r:
    if len(match) == 1:
      return True
  return False

def is_increasing(number:int) -> bool:
  return str(number) == "".join(sorted(str(number)))

print(len([p for p in password_range if all((has_double(p), is_increasing(p)))]))  # part 1
print(len([p for p in password_range if all((has_double_stricter(p), is_increasing(p)))]))  # part 2
