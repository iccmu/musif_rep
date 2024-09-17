import importlib.util
import os

def run_script(script_path):
    spec = importlib.util.spec_from_file_location("module.name", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

if __name__ == "__main__":
    pages_dir = os.path.join(os.path.dirname(__file__), 'pages')
    for script in os.listdir(pages_dir):
        if script.endswith('.py'):
            script_path = os.path.join(pages_dir, script)
            print(f"Running {script_path}")
            run_script(script_path)
