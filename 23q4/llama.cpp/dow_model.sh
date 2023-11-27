# export SPACE="TheBloke/Yi-6B-GGUF"
# export MODEL="yi-6b.Q5_K_M.gguf"
export SPACE=""
export MODEL=""
export DIR="/Volumes/Workspace/Databases/Models"

huggingface-cli download "${SPACE}" "${MODEL}" \
    --local-dir "${DIR}" \
    --local-dir-use-symlinks False
