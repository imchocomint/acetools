import psutil

def checkrun(process_name):
    # Iterate over all running processes
    for proc in psutil.process_iter(['name']):
        try:
            # Check if the process name matches (case-insensitive)
            if process_name.lower() in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False
