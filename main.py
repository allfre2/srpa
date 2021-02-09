from modules.rpa import RPA
from modules.parser import JsonParser, FileDataSource

rpa = RPA(JsonParser(FileDataSource("./sample.json")))
print("DONE!")