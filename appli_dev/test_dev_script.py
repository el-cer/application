import subprocess

def run_shell_script(script_path, *args):
    try:

        # Run the shell script with optional arguments
        result = subprocess.run([script_path] + list(args), capture_output=True, text=True, check=True)
        
        # Print the standard output from the script

        
        # Print any errors encountered
        if result.stderr:
            print(f"Error output: {result.stderr}")
            

    except subprocess.CalledProcessError as e:
        print(f"Script failed with return code {e.returncode}")
        print(f"Error output: {e.stderr}")


# Path to the shell script


# Optional: arguments to pass to the shell script


# Run the shell script


