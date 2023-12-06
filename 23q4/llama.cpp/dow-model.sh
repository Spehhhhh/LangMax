export SPACE_NAME="" # TheBloke/Yi-6B-GGUF
export MODEL_NAME="" # yi-6b.Q5_K_M.gguf
export MODELS_DIR="" # /Volumes/Workspace/Databases/Models

huggingface-cli download "${SPACE_NAME}" "${MODEL_NAME}" \
    --local-dir "${MODELS_DIR}" \
    --local-dir-use-symlinks False
