from datetime import datetime
from typing import List, Tuple, Dict, Any

def parse_time(time_str: str) -> datetime:
    """Parse time string to datetime."""
    time_str = time_str.strip()
    
    # Try common formats including ISO format
    formats = [
        "%Y-%m-%dT%H:%M",      # 2025-01-01T08:00
        "%Y-%m-%dT%H:%M:%S",   # 2025-01-01T08:00:00
        "%H:%M:%S",            # 10:00:00
        "%H:%M",               # 10:00
        "%Y-%m-%d %H:%M:%S",   # 2025-01-01 10:00:00
        "%Y-%m-%d %H:%M",      # 2025-01-01 10:00
    ]
    
    for fmt in formats:
        try:
            result = datetime.strptime(time_str, fmt)
            # For time-only, use today's date
            if fmt in ("%H:%M:%S", "%H:%M"):
                return datetime.combine(datetime.today().date(), result.time())
            return result
        except ValueError:
            continue
    
    raise ValueError(f"Invalid time format: {time_str}")

def detect_irrigation_overlaps(data: List[Dict[str, Any]]) -> List[Tuple[str, str]]:
    """
    Find overlapping irrigation intervals using sweep-line algorithm.
    
    Args:
        data: List of dictionaries with 'field', 'start', 'end' keys
    
    Returns:
        List of overlapping field pairs
    """
    # Parse data from list of dictionaries
    intervals = []
    for item in data:
        try:
            field_id = item['field']
            start = parse_time(item['start'])
            end = parse_time(item['end'])
            if end > start:
                intervals.append((field_id, start, end))
        except (KeyError, ValueError):
            continue
    
    if len(intervals) < 2:
        return []
    
    # Create events: (time, is_start, field_id, index)
    events = []
    for i, (field_id, start, end) in enumerate(intervals):
        events.append((start, True, field_id, i))
        events.append((end, False, field_id, i))
    
    # Sort by time, start events before end events
    events.sort(key=lambda x: (x[0], not x[1]))
    
    # Sweep line algorithm
    active = set()  # Active interval indices
    overlaps = set()  # Overlapping field pairs
    
    for time, is_start, field_id, index in events:
        if is_start:
            # Check overlaps with active intervals
            for active_index in active:
                active_field = intervals[active_index][0]
                active_start, active_end = intervals[active_index][1], intervals[active_index][2]
                current_start, current_end = intervals[index][1], intervals[index][2]
                
                # Check if intervals overlap
                if current_start < active_end and active_start < current_end:
                    pair = tuple(sorted([active_field, field_id]))
                    overlaps.add(pair)
            
            active.add(index)
        else:
            active.discard(index)
    
    return sorted(overlaps)

def main():
    """Demo the irrigation overlap detection."""
    # Sample input in the requested format
    sample_data = [
        {'field': 'F1', 'start': '2025-01-01T08:00', 'end': '2025-01-01T10:00'},
        {'field': 'F2', 'start': '2025-01-01T09:30', 'end': '2025-01-01T11:00'},
        {'field': 'F3', 'start': '2025-01-01T11:00', 'end': '2025-01-01T12:00'},
        {'field': 'F4', 'start': '2025-01-01T14:00', 'end': '2025-01-01T16:00'},
        {'field': 'F5', 'start': '2025-01-01T15:00', 'end': '2025-01-01T17:00'},
        {'field': 'F6', 'start': '2025-01-01T09:00', 'end': '2025-01-01T11:30'},
    ]
    
    print("Sample Input:")
    print(sample_data)
    print()
    
    overlaps = detect_irrigation_overlaps(sample_data)
    
    print("Sample Output:")
    print(overlaps)
    
    # Test edge cases
    print("\nEdge case tests:")
    
    # No overlaps
    test1 = [
        {'field': 'F1', 'start': '2025-01-01T10:00', 'end': '2025-01-01T11:00'},
        {'field': 'F2', 'start': '2025-01-01T12:00', 'end': '2025-01-01T13:00'}
    ]
    result1 = detect_irrigation_overlaps(test1)
    print(f"No overlaps: {result1}")
    
    # Adjacent (no overlap)
    test2 = [
        {'field': 'F1', 'start': '2025-01-01T10:00', 'end': '2025-01-01T11:00'},
        {'field': 'F2', 'start': '2025-01-01T11:00', 'end': '2025-01-01T12:00'}
    ]
    result2 = detect_irrigation_overlaps(test2)
    print(f"Adjacent: {result2}")
    
    # Multiple overlaps
    test3 = [
        {'field': 'F1', 'start': '2025-01-01T10:00', 'end': '2025-01-01T12:00'},
        {'field': 'F2', 'start': '2025-01-01T11:00', 'end': '2025-01-01T13:00'},
        {'field': 'F3', 'start': '2025-01-01T11:30', 'end': '2025-01-01T12:30'}
    ]
    result3 = detect_irrigation_overlaps(test3)
    print(f"Multiple overlaps: {result3}")

if __name__ == "__main__":
    main()