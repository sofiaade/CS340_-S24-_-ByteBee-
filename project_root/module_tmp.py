from Config import CONFIG  

def log_progress(message):
    """Writes log messages to a file."""
    log_file_path = CONFIG.get("log_file", "app.log")  
    try:
        with open(log_file_path, "a") as log_file:  
            log_file.write(f"{message}\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")
        #

def catch_errors(func):
    """Decorator to catch and log errors in functions."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            log_progress(f"Error in {func.__name__}: {e}")
            raise e  
    return wrapper
    #

# Test the logging functionality
if __name__ == "__main__":
    # Test log_progress
    log_progress("Testing log functionality in module_tmp.py.")
    print("Log message should now be written to app.log.")
    #