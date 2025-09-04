def convert_date_format(date_str):
    """Converts date from 'YYYY-MM-DD' to 'DD-MM-YYYY' format."""
    try:
        # Check for None and strip spaces
        if not isinstance(date_str, str) or date_str.strip() != date_str:
            return "Invalid input"
        parts = date_str.split("-")
        if len(parts) != 3:
            return "Invalid input"
        yyyy, mm, dd = parts
        if not (yyyy and mm and dd):
            return "Invalid input"
        return f"{dd}-{mm}-{yyyy}"
    except Exception:
        return "Invalid input"