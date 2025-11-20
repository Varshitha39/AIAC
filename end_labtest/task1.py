"""
Product Rating Analyzer

This module provides functionality to find the highest-rated product
from a list of product ratings. It handles various edge cases and
provides detailed information about the highest-rated product(s).
"""

from typing import List, Dict, Optional, Tuple


def find_highest_rated_product(products: List[Dict[str, any]]) -> Optional[Dict[str, any]]:
    """
    Find the highest-rated product from a list of products with ratings.
    
    This function identifies the product with the highest rating value.
    If multiple products have the same highest rating, it returns the first one encountered.
    
    Args:
        products: A list of dictionaries, where each dictionary represents a product
                 and must contain at least a 'rating' key with a numeric value.
                 Example: [{'name': 'Product A', 'rating': 4.5}, ...]
    
    Returns:
        The dictionary of the highest-rated product, or None if the list is empty
        or no valid ratings are found.
    
    Raises:
        ValueError: If a product dictionary is missing the 'rating' key.
        TypeError: If a rating value is not numeric.
    
    Example:
        >>> products = [
        ...     {'name': 'Laptop', 'rating': 4.2, 'price': 999},
        ...     {'name': 'Phone', 'rating': 4.8, 'price': 699},
        ...     {'name': 'Tablet', 'rating': 4.1, 'price': 399}
        ... ]
        >>> find_highest_rated_product(products)
        {'name': 'Phone', 'rating': 4.8, 'price': 699}
    """
    # Handle empty list edge case
    if not products:
        return None
    
    # Initialize tracking variables
    highest_rating = float('-inf')  # Start with negative infinity to handle negative ratings
    highest_rated_product = None
    
    # Iterate through each product in the list
    for product in products:
        # Validate that product is a dictionary
        if not isinstance(product, dict):
            raise TypeError(f"Expected dictionary, got {type(product).__name__}")
        
        # Check if 'rating' key exists
        if 'rating' not in product:
            raise ValueError(f"Product missing 'rating' key: {product}")
        
        # Get and validate rating value
        rating = product['rating']
        
        # Ensure rating is numeric (int or float)
        if not isinstance(rating, (int, float)):
            raise TypeError(f"Rating must be numeric, got {type(rating).__name__} for product: {product}")
        
        # Check if current product has a higher rating than the current highest
        if rating > highest_rating:
            highest_rating = rating
            highest_rated_product = product
    
    # Return None if no valid product was found (shouldn't happen, but defensive programming)
    return highest_rated_product


def find_highest_rated_products(products: List[Dict[str, any]]) -> List[Dict[str, any]]:
    """
    Find all products with the highest rating (handles ties).
    
    This function returns all products that share the highest rating value,
    useful when multiple products have the same top rating.
    
    Args:
        products: A list of dictionaries, where each dictionary represents a product
                 and must contain at least a 'rating' key with a numeric value.
    
    Returns:
        A list of dictionaries containing all products with the highest rating.
        Returns empty list if input is empty or no valid ratings found.
    
    Example:
        >>> products = [
        ...     {'name': 'Laptop', 'rating': 4.8},
        ...     {'name': 'Phone', 'rating': 4.8},
        ...     {'name': 'Tablet', 'rating': 4.1}
        ... ]
        >>> find_highest_rated_products(products)
        [{'name': 'Laptop', 'rating': 4.8}, {'name': 'Phone', 'rating': 4.8}]
    """
    if not products:
        return []
    
    # First pass: find the highest rating value
    highest_rating = float('-inf')
    
    for product in products:
        if not isinstance(product, dict) or 'rating' not in product:
            continue
        
        rating = product['rating']
        if isinstance(rating, (int, float)):
            highest_rating = max(highest_rating, rating)
    
    # If no valid ratings found
    if highest_rating == float('-inf'):
        return []
    
    # Second pass: collect all products with the highest rating
    highest_rated_products = []
    for product in products:
        if isinstance(product, dict) and 'rating' in product:
            rating = product['rating']
            if isinstance(rating, (int, float)) and rating == highest_rating:
                highest_rated_products.append(product)
    
    return highest_rated_products


def get_product_rating_stats(products: List[Dict[str, any]]) -> Dict[str, any]:
    """
    Get comprehensive statistics about product ratings.
    
    Returns the highest-rated product along with statistical information
    about all ratings in the dataset.
    
    Args:
        products: A list of product dictionaries with 'rating' keys.
    
    Returns:
        A dictionary containing:
        - 'highest_rated': The highest-rated product
        - 'highest_rating': The highest rating value
        - 'average_rating': Average of all ratings
        - 'total_products': Total number of products
        - 'all_highest_rated': List of all products with highest rating (if ties exist)
    """
    if not products:
        return {
            'highest_rated': None,
            'highest_rating': None,
            'average_rating': None,
            'total_products': 0,
            'all_highest_rated': []
        }
    
    # Collect valid ratings
    valid_ratings = []
    for product in products:
        if isinstance(product, dict) and 'rating' in product:
            rating = product['rating']
            if isinstance(rating, (int, float)):
                valid_ratings.append(rating)
    
    if not valid_ratings:
        return {
            'highest_rated': None,
            'highest_rating': None,
            'average_rating': None,
            'total_products': len(products),
            'all_highest_rated': []
        }
    
    highest_rating = max(valid_ratings)
    average_rating = sum(valid_ratings) / len(valid_ratings)
    highest_rated = find_highest_rated_product(products)
    all_highest = find_highest_rated_products(products)
    
    return {
        'highest_rated': highest_rated,
        'highest_rating': highest_rating,
        'average_rating': round(average_rating, 2),
        'total_products': len(products),
        'all_highest_rated': all_highest
    }
    # Add this at the end of task1.py to see output

if __name__ == '__main__':
    # Example product list
    products = [
        {'name': 'Gaming Laptop', 'rating': 4.5, 'price': 1299, 'category': 'Electronics'},
        {'name': 'Wireless Mouse', 'rating': 4.8, 'price': 29, 'category': 'Accessories'},
        {'name': 'Mechanical Keyboard', 'rating': 4.7, 'price': 149, 'category': 'Accessories'},
        {'name': 'Monitor', 'rating': 4.6, 'price': 299, 'category': 'Electronics'},
        {'name': 'Webcam', 'rating': 4.8, 'price': 79, 'category': 'Accessories'}
    ]
    
    print("=" * 70)
    print("PRODUCT RATING ANALYZER - DEMONSTRATION")
    print("=" * 70)
    print()
    
    # Display all products
    print("📦 ALL PRODUCTS:")
    print("-" * 70)
    for i, product in enumerate(products, 1):
        print(f"  {i}. {product['name']:25} | Rating: {product['rating']}/5.0 | Price: ${product['price']}")
    print()
    
    # Find single highest-rated product
    print("🏆 HIGHEST-RATED PRODUCT (Single):")
    print("-" * 70)
    highest = find_highest_rated_product(products)
    if highest:
        print(f"   Product: {highest['name']}")
        print(f"   Rating:  {highest['rating']}/5.0")
        print(f"   Price:   ${highest.get('price', 'N/A')}")
        print(f"   Category: {highest.get('category', 'N/A')}")
    print()
    
    # Find all highest-rated products (handles ties)
    print("⭐ ALL HIGHEST-RATED PRODUCTS (Handles Ties):")
    print("-" * 70)
    all_highest = find_highest_rated_products(products)
    if all_highest:
        print(f"   Found {len(all_highest)} product(s) with rating {all_highest[0]['rating']}/5.0:")
        for product in all_highest:
            print(f"   • {product['name']} - ${product.get('price', 'N/A')}")
    print()
    
    # Get comprehensive statistics
    print("📊 COMPREHENSIVE STATISTICS:")
    print("-" * 70)
    stats = get_product_rating_stats(products)
    print(f"   Highest Rating:        {stats['highest_rating']}/5.0")
    print(f"   Average Rating:        {stats['average_rating']}/5.0")
    print(f"   Total Products:        {stats['total_products']}")
    print(f"   Products with Top Rating: {len(stats['all_highest_rated'])}")
    print()
    
    # Additional test cases
    print("🧪 ADDITIONAL TEST CASES:")
    print("-" * 70)
    
    # Test with empty list
    print("1. Empty list test:")
    result = find_highest_rated_product([])
    print(f"   Result: {result}")
    print()
    
    # Test with single product
    print("2. Single product test:")
    single_product = [{'name': 'Single Item', 'rating': 4.9}]
    result = find_highest_rated_product(single_product)
    print(f"   Result: {result['name']} with rating {result['rating']}")
    print()
    
    # Test with tied ratings
    print("3. Tied ratings test:")
    tied_products = [
        {'name': 'Product A', 'rating': 4.8},
        {'name': 'Product B', 'rating': 4.8},
        {'name': 'Product C', 'rating': 4.5}
    ]
    result = find_highest_rated_product(tied_products)
    print(f"   First highest: {result['name']} ({result['rating']})")
    all_tied = find_highest_rated_products(tied_products)
    print(f"   All with highest rating: {[p['name'] for p in all_tied]}")
    print()
    
    print("=" * 70)
    print("✅ Demonstration complete!")
    print("=" * 70)