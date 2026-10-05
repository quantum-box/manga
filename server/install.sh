#!/usr/bin/env bash
set -euo pipefail
if ! command -v rustup >/dev/null; then
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile minimal --default-toolchain 1.95.0
fi
source "$HOME/.cargo/env"
rustup toolchain install 1.95.0 --profile minimal --target wasm32-unknown-unknown
cargo +1.95.0 install worker-build --version 0.8.7 --locked
