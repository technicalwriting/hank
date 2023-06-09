from jsonlines import open as jsonl_open
from glob import glob
from json import load, dump
from sys import argv, exit
from openai import Model
from os import getcwd
from tiktoken import get_encoding

def data2():
    jsonl = []
    data_files = glob('data2/*')
    for data_file in data_files:
        start = data_file.index('/') + 1
        end = len(data_file)
        file_name = data_file[start:end]
        start = 0
        end = file_name.index('_')
        doc_number = file_name[start:end]
        start = file_name.index('.') + 1
        end = len(file_name)
        file_type = file_name[start:end]
        with open(f'data2/{doc_number}_a.{file_type}', 'r') as f:
            a = f.read()
        with open(f'data2/{doc_number}_b.{file_type}', 'r') as f:
            b = f.read()
        jsonl.append({'prompt': a, 'completion': b})
    print(jsonl)


def tmp(filename):
    with open('tmp.json', 'r') as f:
        data = load(f)
    out = {
      'test': '',
      'expected': '',
      'training': data
    }
    with open(f'data/{filename}.json', 'w') as f:
        dump(out, f, indent=2)

def model():
    with open('version.txt', 'r') as f:
        version = f.readlines()[0].replace('\n', '')
    version = f'hank-v{version}'
    response = Model.list()
    model = None
    for m in response['data']:
        if version not in m['id']:
            continue
        if model is None:
            model = m['id']
            continue
        exit(f'ERROR: Multiple models match {version}!')
    if model is None:
        exit('ERROR: No matching model found!')
    with open('model.txt', 'w') as f:
        f.write(model)
    exit(0)

def transform():
    encoder = get_encoding('r50k_base')
    test = []
    expected = []
    cwd = getcwd()
    try:
        data_files = glob('data/*.json')
        jsonl = []
        stop_sequence = '\n\n( ͡° ͜ʖ ͡°)\n\n(☞ ͡° ͜ʖ ͡°)☞\n\n'
        for data_file in data_files:
            print(data_file)
            with open(data_file, 'r') as f:
                data = load(f)
            test.append(data['test'])
            expected.append(data['expected'])
            for pair in data['training']:
                prompt = pair[0]
                completion = pair[1]
                # Remember that the completion is supposed to start with a space!
                # https://platform.openai.com/docs/guides/fine-tuning/data-formatting
                jsonl.append({'prompt': f'{prompt}{stop_sequence}', 'completion': f' {completion}'})
            with jsonl_open('training.jsonl', 'w') as writer:
                writer.write_all(jsonl)
        test = ' '.join(test)
        expected = ' '.join(expected)
        token_count = len(encoder.encode(test)) + 50
        with open(f'{cwd}/www/src/data.json', 'w') as f:
            dump({'test': test, 'token_count': token_count, 'expected': expected, 'stop_sequence': stop_sequence}, f, indent=2)
        exit(0)
    except Exception as e:
        print(e)
        exit(1)

if __name__ == '__main__':
    if argv[1] == 'model':
        model()
    if argv[1] == 'transform':
        transform()
    if argv[1] == 'tmp':
        tmp(argv[2])
    if argv[1] == 'data2':
        data2()
