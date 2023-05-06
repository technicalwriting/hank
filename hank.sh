function bootstrap {
  python3 -m venv venv
  source venv/bin/activate
  python3 -m pip install -r requirements.txt
}

function create {
  source www/.dev.vars
  export OPENAI_API_KEY=$OPENAI_API_KEY
  HANK_VERSION=$(cat version.txt)
  ((HANK_VERSION++))
  echo $HANK_VERSION > version.txt
  SUFFIX="HANK_V$HANK_VERSION"
  sed -i "s/version = '.*'/version = '$HANK_VERSION'/" www/src/index.js
  # openai api fine_tunes.create -t training.jsonl -m curie --suffix $SUFFIX
  # git add version.txt www/src/index.js
  # git commit -m "Bump to v$HANK_VERSION"
}

$1

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
