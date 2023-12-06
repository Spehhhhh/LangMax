export GGUF_MODEL_PATH="/Volumes/Workspace/Databases/Models/openhermes-2.5-mistral-7b-16k.Q5_K_M.gguf"
export PROMPT="I have three apples, I eat two pears, how many apples do I have?"

"$HOME"/Databases/Stacks/LLM/llama.cpp/server \
    -m "${GGUF_MODEL_PATH}"
