#!/usr/bin/env python3
"""
Health Sensor Data Analysis Script

Complete the TODO sections to analyze health sensor data using NumPy.
This script demonstrates basic NumPy operations for data loading, statistics,
filtering, and report generation.
"""

import numpy as np


def load_data(filename):
    """Load CSV data using NumPy.
    
    Args:
        filename: Path to CSV file
        
    Returns:
        NumPy structured array with all columns
    """
    # This code is provided because np.genfromtxt() is not covered in the lecture
    dtype = [('patient_id', 'U10'), ('timestamp', 'U20'), 
             ('heart_rate', 'i4'), ('blood_pressure_systolic', 'i4'),
             ('blood_pressure_diastolic', 'i4'), ('temperature', 'f4'),
             ('glucose_level', 'i4'), ('sensor_id', 'U10')]
    
    data = np.genfromtxt(filename, delimiter=',', dtype=dtype, skip_header=1)
    return data


def calculate_statistics(data):
    """Calculate basic statistics for numeric columns.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with statistics
    """
    # Calculate averages using NumPy's mean() method
    avg_heart_rate = data['heart_rate'].mean()
    avg_systolic_bp = data['blood_pressure_systolic'].mean()
    avg_glucose = data['glucose_level'].mean()

    # Return as a dictionary, formatted to 1 decimal place
    stats = {
        'avg_heart_rate': f"{avg_heart_rate:.1f}",
        'avg_systolic_bp': f"{avg_systolic_bp:.1f}",
        'avg_glucose': f"{avg_glucose:.1f}"
    }

    return stats


def find_abnormal_readings(data):
    """Find readings with abnormal values.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with counts
    """
    # Count readings where values exceed thresholds using boolean indexing
    high_hr_count = (data['heart_rate'] > 90).sum()
    high_bp_count = (data['blood_pressure_systolic'] > 130).sum()
    high_glucose_count = (data['glucose_level'] > 110).sum()

    # Return dictionary with counts
    abnormal = {
        'high_heart_rate': int(high_hr_count),
        'high_blood_pressure': int(high_bp_count),
        'high_glucose': int(high_glucose_count)
    }

    return abnormal


def generate_report(stats, abnormal, total_readings):
    """Generate formatted analysis report.
    
    Args:
        stats: Dictionary of statistics
        abnormal: Dictionary of abnormal counts
        total_readings: Total number of readings
        
    Returns:
        Formatted string report
    """
    # Create a formatted multi-line string using f-strings
    report = (
        "Health Sensor Data Analysis Report\n"
        "==================================\n\n"
        f"Dataset Summary:\n"
        f"- Total readings: {total_readings}\n\n"
        f"Average Measurements:\n"
        f"- Heart Rate: {stats['avg_heart_rate']} bpm\n"
        f"- Systolic BP: {stats['avg_systolic_bp']} mmHg\n"
        f"- Glucose Level: {stats['avg_glucose']} mg/dL\n\n"
        f"Abnormal Readings:\n"
        f"- High Heart Rate (>90): {abnormal['high_heart_rate']} readings\n"
        f"- High Blood Pressure (>130): {abnormal['high_blood_pressure']} readings\n"
        f"- High Glucose (>110): {abnormal['high_glucose']} readings\n"
    )

    return report


import os

def save_report(report, filename):
    """Save report to file.
    
    Args:
        report: Report string
        filename: Output filename
    """
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Write the report string to the specified file
    with open(filename, 'w') as f:
        f.write(report)


def main():
    """Main execution function."""
    # Load the data from the CSV file
    data = load_data('health_data.csv')

    # Calculate overall statistics
    stats = calculate_statistics(data)

    # Find abnormal readings
    abnormal = find_abnormal_readings(data)

    # Count total readings
    total_readings = len(data)

    # Generate the formatted report
    report = generate_report(stats, abnormal, total_readings)

    # Save the report to the output directory
    save_report(report, 'output/analysis_report.txt')

    # Print a success message
    print("✅ Analysis complete! Report saved to output/analysis_report.txt")


if __name__ == "__main__":
    main()