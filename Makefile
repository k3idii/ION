
all: schema2json yaml2json validate sign
	echo "ALL DONE"

schema2json:
	echo "Generate JSON schema form YAML"
	cat schema.yaml | yq . > schema.json

yaml2json:
	echo "Generate JSON ruleset from YAML"
	cat full.yaml | yq . > full.json

validate:
	echo "validate JSON ruleset against schema"
	python validate.py schema.json full.json 

sign:
	echo "Signing JSON -> JWT"
	openssl genrsa 1024 > key.rsa.prv
	python jwt_tool.py -m s -a RS256 -S key.rsa.prv -i full.json -o full.jwt
