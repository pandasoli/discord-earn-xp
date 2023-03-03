import sys
from time import sleep
from program import Program


props = {
  'countdown': 5,
  'ex-bot': 'loritta',
  'anti-spam': '',
  'text': 'shrek-movie-script'
}

def main(argv: list[str], argc: int):
  for i in range(argc):
    arg = argv[i]

    if ':' in arg:
      key = arg.split(':')[0]
      val = ':'.join(arg.split(':')[1:])
      props[key] = val
    else:
      props[arg] = True

  countdown = int(props['countdown'])
  for i in range(countdown):
    print(f'{countdown - i}...', end = '\r')
    sleep(1)

  Program(props).run()


if __name__ == '__main__':
  main(sys.argv, len(sys.argv))
