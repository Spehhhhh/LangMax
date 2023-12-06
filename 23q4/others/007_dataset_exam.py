from datasets import load_dataset
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# https://huggingface.co/datasets/keirp/hungarian_national_hs_finals_exam

# Initialize the console
console = Console()

# Load the dataset
dataset = load_dataset("keirp/hungarian_national_hs_finals_exam")

# Dataset structure
dataset_structure = dataset['test'].features
console.print("Dataset Structure:", style="bold blue")
console.print(dataset_structure)

# Number of rows and columns
num_rows = len(dataset['test'])
num_columns = len(dataset['test'].features)
console.print("\nDataset Size:", style="bold blue")
console.print(f"Number of rows: {num_rows}, Number of columns: {num_columns}")

# Sample data
sample_data = dataset['test'].select(range(5))

console.print("\nSample Questions:", style="bold blue")
for record in sample_data:
    question = record['Question']
    console.print(Panel(question, title="Question", border_style="green"))
