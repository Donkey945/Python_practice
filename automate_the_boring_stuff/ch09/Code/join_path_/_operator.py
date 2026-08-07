from pathlib import Path
a = Path('spam') / 'bacon' / 'eggs'
b = Path('spam') / Path('bacon/eggs')
c = Path('spam') / Path('bacon', 'eggs')
print(a,b,c, sep='\n')