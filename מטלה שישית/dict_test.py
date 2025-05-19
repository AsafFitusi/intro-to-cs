
def main():
    # Sample dictionaries for testing
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'b': 20, 'c': 30, 'd': 40}

    # Test join_dict function
    print("Testing join_dict:")
    joined = join_dict(d1, d2)
    print(f"join_dict(d1, d2) = {joined}")
    # Expected output: [(2, 20), (3, 30)]

    # Test is_mutual2 function
    print("\nTesting is_mutual2:")
    test_tpl1 = (2, 20)
    test_tpl2 = (3, 30)
    test_tpl3 = (1, 10)  # Not mutual

    print(f"is_mutual({test_tpl1}, d1, d2) = {is_mutual(test_tpl1, d1, d2)}")  # Expected: True
    print(f"is_mutual({test_tpl2}, d1, d2) = {is_mutual(test_tpl2, d1, d2)}")  # Expected: True
    print(f"is_mutual({test_tpl3}, d1, d2) = {is_mutual(test_tpl3, d1, d2)}")  # Expected: False

if __name__ == "__main__":
    main()
    
'''   
Testing join_dict:
join_dict(d1, d2) = [(2, 20), (3, 30)]

Testing is_mutual2:
is_mutual((2, 20), d1, d2) = True
is_mutual((3, 30), d1, d2) = True
is_mutual((1, 10), d1, d2) = False

    
'''  