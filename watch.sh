function cleanup {
  echo "Removing /config.toml"
  rm  config.toml
}
trap cleanup EXIT

python Toml_constructor.py
npm-run-all --parallel tailwind:serve vite:serve zola:serve