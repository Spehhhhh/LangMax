import marimo

__generated_with = "0.4.2"
app = marimo.App(width="medium")


@app.cell
def __():
    1 + 1
    return


@app.cell
def __():
    3 + 3
    return


if __name__ == "__main__":
    app.run()
