from jsonlines import open as jsonl_open
from glob import glob
from json import load, dump
from sys import argv, exit
from openai import Model
from os import getcwd

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
    test = []
    expected = []
    cwd = getcwd()
    try:
        data_files = glob('data/*.json')
        jsonl = []
        stop_sequence = '( ͡° ͜ʖ ͡°)'
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
        with open(f'{cwd}/www/src/data.json', 'w') as f:
            dump({'test': ' '.join(test), 'expected': ' '.join(expected)}, f, indent=2)
        exit(0)
    except Exception as e:
        print(e)
        exit(1)

if __name__ == '__main__':
    if argv[1] == 'model':
        model()
    if argv[1] == 'transform':
        transform()
