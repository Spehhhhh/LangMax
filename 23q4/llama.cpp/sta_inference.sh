export MODEL="/Volumes/Workspace/Databases/Models/openhermes-2.5-mistral-7b-16k.Q5_K_M.gguf"
export PROMPT="I have three apples, I eat two pears, how many apples do I have?"

"$HOME"/Databases/Stacks/LLM/llama.cpp/main \
    --model "${MODEL}" \
    --prompt "${PROMPT}" \
    --color \
    --escape \
    --temp 0.8 \
    --n-predict 400

#     --ctx-size 2048 \
#     --n-gpu-layers 1 \
#     --n-predict -1 \
#     --repeat_penalty 1.1 \
#     --threads 8
