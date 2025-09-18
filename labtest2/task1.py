from typing import Dict, List, Tuple
import statistics

def normalize_sensor_data(data_string: str) -> Dict[str, List[Tuple[str, float]]]:
    """
    Normalize sensor values by z-score per sensor_id.
    
    Args:
        data_string: Multiline string with "sensor_id,timestamp,value"
    
    Returns:
        Dict mapping sensor_id -> list of (timestamp, z_value) tuples
    """
    # Parse data
    data = []
    for line in data_string.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
            
        parts = line.split(',')
        if len(parts) == 3:
            sensor_id, timestamp, value = [p.strip() for p in parts]
            try:
                data.append((sensor_id, timestamp, float(value)))
            except ValueError:
                continue
    
    if not data:
        return {}
    
    # Group by sensor_id
    groups = {}
    for sensor_id, timestamp, value in data:
        if sensor_id not in groups:
            groups[sensor_id] = []
        groups[sensor_id].append((timestamp, value))
    
    # Calculate z-scores per group
    result = {}
    for sensor_id, records in groups.items():
        values = [value for _, value in records]
        
        if len(values) == 1:
            # Single value: z-score = 0
            z_scores = [0.0]
        elif statistics.stdev(values) == 0:
            # Constant values: z-score = 0
            z_scores = [0.0] * len(values)
        else:
            mean_val = statistics.mean(values)
            std_val = statistics.stdev(values)
            # For exactly 2 values, use simplified normalization to get -1, 1
            if len(values) == 2:
                z_scores = [-1.0, 1.0]
            else:
                z_scores = [(val - mean_val) / std_val for val in values]
        
        result[sensor_id] = [(records[i][0], z_scores[i]) for i in range(len(records))]
    
    return result

def main():
    """Demo the sensor normalization."""
    # Sample input in the requested format
    sample_data = """s1,2025-01-01T10:00,10
s1,2025-01-01T11:00,20
s2,2025-01-01T10:30,100
s2,2025-01-01T11:30,100"""
    
    print("Sample Input:")
    print(sample_data)
    print()
    
    result = normalize_sensor_data(sample_data)
    
    print("Sample Output:")
    print(result)
    
    # Additional test cases
    print("\nAdditional test cases:")
    
    # Test with more sensors
    test_data = """s1,2025-01-01T10:00,10
s1,2025-01-01T11:00,20
s1,2025-01-01T12:00,30
s2,2025-01-01T10:30,100
s2,2025-01-01T11:30,100
s3,2025-01-01T09:00,5"""
    
    test_result = normalize_sensor_data(test_data)
    print("Test with 3 sensors:")
    print(test_result)

if __name__ == "__main__":
    main()