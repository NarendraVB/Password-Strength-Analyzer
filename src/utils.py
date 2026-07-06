def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return f"{int(minutes)} minutes, {remaining_seconds:.2f} seconds"
    elif seconds < 86400:
        hours = seconds // 3600
        remaining_minutes = (seconds % 3600) // 60
        remaining_seconds = seconds % 60
        return f"{int(hours)} hours, {int(remaining_minutes)} minutes, {remaining_seconds:.2f} seconds"
    else:
        days = seconds // 86400
        remaining_hours = (seconds % 86400) // 3600
        remaining_minutes = (seconds % 3600) // 60
        remaining_seconds = seconds % 60
        return f"{int(days)} days, {int(remaining_hours)} hours, {int(remaining_minutes)} minutes, {remaining_seconds:.2f} seconds"