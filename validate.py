from jsonschema import validate
import json
import sys 
import yaml


SCHEMA_FILE=sys.argv[1]
SCHEMA = json.load(open(SCHEMA_FILE))

if len(sys.argv) > 2:
  tmp = open(sys.argv[2], 'rb').read()
  data = json.loads(tmp)
else:
  print("WARNING: reading from stdin !", file=sys.stderr)
  data = json.loads(sys.stdin.buffer.read())
  
validate(
  instance = data,
  schema = SCHEMA,
)
print("Looks good !")