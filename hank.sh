function export_key {
  source www/.dev.vars
  export OPENAI_API_KEY=$OPENAI_API_KEY
}

function bootstrap {
  python3 -m venv venv
  source venv/bin/activate
  python3 -m pip install -r requirements.txt
}

function create {
  source venv/bin/activate
  python3 main.py transform
  export_key
  VERSION=$(cat version.txt)
  ((VERSION++))
  echo $VERSION > version.txt
  SUFFIX="hank-v$VERSION"
  openai api fine_tunes.create -t training.jsonl -m curie --suffix $SUFFIX
  python3 main.py model > model.txt
  MODEL=$(cat model.txt)
  sed -i "s/model = '.*'/model = '$MODEL'/" www/src/index.js
  git add version.txt www/src/index.js model.txt
  git commit -m "Bump to v$VERSION ($MODEL)"
  deactivate
}

$1
