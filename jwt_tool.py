import jwt
import sys
import argparse
import json


def do_sign(data, outfile, secret, alg):
  out = jwt.encode(
    payload=data,
    key = secret,
    algorithm = alg
  )
  outfile.write(out)
  outfile.flush()

def do_verify(data, outfile, secret, alg):
  out = jwt.decode(
    data.decode(),
    key = secret,
    algorithms = alg 
    )
  outfile.write(json.dumps(out))


def main():
  parser = argparse.ArgumentParser(description='JWT Tool')
  parser.add_argument('-m', '--mode', required=True, choices=['s','v'], help='[s]ign or [v]erify')
  parser.add_argument('-a', '--alg',  required=True, help="Algorithm")
  parser.add_argument('-s', '--secret',     default=None, help="secret string")
  parser.add_argument('-S', '--secretfile', default=None, help="secret file")
  parser.add_argument('-i', '--input',  default=None, help="input file (if none => stdin)")
  parser.add_argument('-o', '--output', default=None, help="output file (if none=> stdout)")
  parser.add_argument('-f', '--format', choices=['json','yaml'], default='json', help='(sign mode) Input format')
  args = parser.parse_args()

  secret = None
  if args.secret is None and args.secretfile is None:
    raise Exception("Need secret string OR secret file !")
  if args.secret is not None:
    secret = args.secret
  if args.secretfile is not None:
    secret = open(args.secretfile,'rb').read()

  input_data = None
  if args.input is None:
    print("WARNING: reading from STDIN !", file=sys.stderr)
    input_data = sys.stdin.read()
  else:
    input_data = open(args.input,'rb').read()

  outfile = None
  if args.output is None:
    outfile = sys.stdout.buffer
  else:
    outfile = open(args.output,'wb')

 
  if args.mode == 's':
    data = None
    if args.format == 'json':
      data = json.loads(input_data)
    if args.format == 'yaml':
      import yaml
      data = yaml.safe_load(input_data)
    do_sign(data, outfile, secret, args.alg)

  if args.mode == 'v':
    do_verify(input_data, outfile, secret, args.alg)

if __name__ == '__main__':
  main()



