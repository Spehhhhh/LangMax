export LLAMACPP_DIR="$HOME"/Databases/Stacks/LLM/llama.cpp
export GGUF_MODEL_PATH="/Volumes/Workspace/Databases/Models/openhermes-2.5-mistral-7b-16k.Q5_K_M.gguf"
export PROMPT="I have three apples, I eat two pears, how many apples do I have?"

"$LLAMACPP_DIR"/main \
    --model "${GGUF_MODEL_PATH}" \
    --prompt "${PROMPT}" \
    --color \
    --escape \
    --temp 0.8 \
    --n-predict 400
