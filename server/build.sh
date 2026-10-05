#!/usr/bin/env bash
set -euo pipefail
export CARGO_HOME="$HOME/.manga-toolchain/cargo"
export RUSTUP_HOME="$HOME/.manga-toolchain/rustup"
export PATH="$CARGO_HOME/bin:$PATH"
export RUSTUP_TOOLCHAIN=1.95.0
worker-build --release
