export SPACE_NAME="TheBloke/deepseek-llm-67b-chat-GGUF" # TheBloke/Yi-6B-GGUF
export MODEL_NAME="deepseek-llm-67b-chat.Q5_K_M.gguf"   # yi-6b.Q5_K_M.gguf
export MODELS_DIR="/Volumes/Workspace/Databases/Models" # /Volumes/Workspace/Databases/Models

huggingface-cli download "${SPACE_NAME}" "${MODEL_NAME}" \
    --local-dir "${MODELS_DIR}" \
    --local-dir-use-symlinks False
