#!/usr/bin/env bash
set -euo pipefail
# Keep runner-provided Cargo/Rustup homes from mixing with the app toolchain.
export CARGO_HOME="$HOME/.manga-toolchain/cargo"
export RUSTUP_HOME="$HOME/.manga-toolchain/rustup"
export PATH="$CARGO_HOME/bin:$PATH"
if [ ! -x "$CARGO_HOME/bin/rustup" ]; then
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --no-modify-path --profile minimal --default-toolchain 1.95.0
fi
rustup toolchain install 1.95.0 --profile minimal --target wasm32-unknown-unknown
cargo +1.95.0 install worker-build --version 0.8.7 --locked
