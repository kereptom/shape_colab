import sys
import nbformat

def fix_widget_state(path):
    # Read the notebook as version 4
    with open(path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # Ensure top-level widget metadata has a state field
    for meta in nb.metadata.get("widgets", {}).values():
        meta.setdefault("state", {})

    # Ensure each cell's widget metadata has a state field
    for cell in nb.cells:
        for meta in cell.metadata.get("widgets", {}).values():
            meta.setdefault("state", {})

    # Write the modified notebook back to disk
    with open(path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fix_widget_state.py <notebook.ipynb>")
        sys.exit(1)

    notebook_path = sys.argv[1]
    fix_widget_state(notebook_path)
    print(f"Patched widget state in '{notebook_path}'.")
