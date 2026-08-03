#!/usr/bin/env bash
# Build do v2 + publicação no GitHub Pages (conta lgcneiva-pessoal).
# Uso:  ./build-and-deploy.sh "mensagem do commit"
# Precisa: python3, git, gh (autenticado como lgcneiva-pessoal).
set -euo pipefail

MSG="${1:-atualiza apresentacao v2}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"   # .../source
REPO="$(cd "$HERE/.." && pwd)"                          # raiz do repo

echo "== build =="
python3 "$HERE/build_v2.py"                             # grava em REPO/v2/index.html

echo "== git commit =="
cd "$REPO"
git add v2/index.html source
git -c user.name="Carla Ulhoa" -c user.email="lgdetailingbsb@gmail.com" commit -m "$MSG" || {
  echo "(nada para commitar)"; exit 0; }

echo "== push (conta lgcneiva-pessoal) =="
TOKEN="$(gh auth token --user lgcneiva-pessoal)"
git push "https://x-access-token:${TOKEN}@github.com/lgcneiva-pessoal/negesp-calass-2026.git" main

echo "== OK. No ar em ~30-90s: https://lgcneiva-pessoal.github.io/negesp-calass-2026/v2/index.html =="
