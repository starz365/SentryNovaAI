import subprocess, os, shutil
import threading, time

def main():
    filename = "process.txt"
    command = input(f"Enter Command: ")
    result = subprocess.run([f"{command}"],capture_output=True, text=True)
    output = result.stdout
    output_thread = threading.Thread(target = output, daemon = True)
    output_thread.start
    print(result.stdout)
    output_thread._stop

    print("\n\n")

    content_list = result.stdout
    def write_to_file(output):
        """Write a list of method names to the file in 3 aligned columns."""
    
        if not filename:
            print("Invalid filename.")
            #mkdir("process.txt")
            return

        try:
            with open(filename, 'a') as file:
                col_width = 25
                for i in range(0, len(content_list), 3):
                    first = content_list[i]
                    second = content_list[i + 1] if i + 1 < len(content_list) else ""
                    third = content_list[i + 2] if i + 2 < len(content_list) else ""
                    line = f"{first.ljust(col_width)}{second.ljust(col_width)}{third}"
                    file.write(line + "\n")
            print("Writing completed.")
        except IOError as e:
            raise IOError(f"Error writing to file: {str(e)}")
        except Exception as e:
            print(f"{e}")

    #write_to_file(output)


    def read_from_file(filename):
        """Read and display the stored methods for the selected type/module."""
        try:
            with open(filename, 'r') as file:
                contents = file.read()
                print(f"{contents}", end=" ")

        except IOError as e:
            raise IOError(f"Error reading from file: {str(e)}")
        except Exception as e:
            print(f"{e}(")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"{str(e)}")

    #read_from_file(filename)
    os.remove(filename)

if __name__ == "__main__":
    main()