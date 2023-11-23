export MODEL="/Volumes/Workspace/Databases/Models/openhermes-2.5-mistral-7b-16k.Q5_K_M.gguf"
export PROMPT="I have three apples, I eat two pears, how many apples do I have?"

"$HOME"/Coding/llama.cpp/server \
    -m "${MODEL}"
