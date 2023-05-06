function export_key {
  source www/.dev.vars
  export OPENAI_API_KEY=$OPENAI_API_KEY
}

function bootstrap {
  python3 -m venv venv
  source venv/bin/activate
  python3 -m pip install -r requirements.txt
}

function deploy {
  source venv/bin/activate
  export_key
  python3 main.py model
  if [ $? -ne 0 ]; then
    echo "Model script did not exit successfully"
    deactivate
    return 1
  fi
  MODEL=$(cat model.txt)
  sed -i "s/model = '.*'/model = '$MODEL'/" www/src/index.js
  git add www/src/index.js model.txt
  git commit -m "Bump model to $MODEL"
  deactivate
  cd www
  npx wrangler publish
  cd ..
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
  git add version.txt www/src/index.js
  git commit -m "Bump to v$VERSION"
  deactivate
}

$1
