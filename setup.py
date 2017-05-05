from cx_Freeze import setup, Executable

setup(name='C2J',
      version='1.0',
      description='Converts CSV files to JSON files',
      executables=[Executable("C2J.py")])
