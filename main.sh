# source venv/bin/activate
# if [ -z $1 ]; then
#     echo 'Missing $1 (model name)'
#     deactivate
#     return 1
# fi
# export OPENAI_API_KEY=$(cat key.txt)
# python3 transform.py
# openai api fine_tunes.create -t training.jsonl -m ada --suffix $1
# deactivate
# source venv/bin/activate
# if [ -z $1 ]; then
#     echo 'Missing $1 (fine-tuning job ID)'
#     deactivate
#     return 1
# fi
# export OPENAI_API_KEY=$(cat key.txt)
# openai api fine_tunes.follow -i $1
# deactivate
# python3 -m venv venv
# source venv/bin/activate
# python3 -m pip install jsonlines openai
# read -p "Enter your OpenAI API key: " openai_api_key
# echo $openai_api_key > key.txt
# deactivate
# source venv/bin/activate
# export OPENAI_API_KEY=$(cat key.txt)
# openai api fine_tunes.list
# deactivate
