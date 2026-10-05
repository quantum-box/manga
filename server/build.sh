#!/usr/bin/env bash
set -euo pipefail
source "$HOME/.cargo/env"
export RUSTUP_TOOLCHAIN=1.95.0
worker-build --release
