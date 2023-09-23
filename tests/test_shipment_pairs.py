# Create your pytest cases here
from src.shipment_pairs import remove_intra, collect_pairs


# Write tests for remove_intra


# Write tests for collect_pairs
import pytest
from src.shipment_pairs import remove_intra, collect_pairs

# Sample shipments for testing
sample_shipments = [
    ['US', 'IN', 14],
    ['US', 'CA', 17],
    ['IN', 'US', 8],
    ['IN', 'CA', 12],
    ['CA', 'US', 7],
    ['CA', 'IN', 5],
]

def test_remove_intra_no_intra():
    # Ensure no intra-country shipments
    shipments = [['US', 'IN', 14], ['CA', 'MX', 3]]
    assert remove_intra(shipments) == shipments

def test_remove_intra_with_intra():
    # Ensure intra-country shipments are removed
    shipments = [
        ['US', 'US', 8],
        ['US', 'IN', 14],
        ['IN', 'IN', 13],
        ['CA', 'CA', 16],
        ['CA', 'MX', 3],
        ['VE', 'VE', 13]
    ]
    expected_result = [
        ['US', 'IN', 14],
        ['CA', 'MX', 3]
    ]
    assert remove_intra(shipments) == expected_result

def test_collect_pairs_empty_input():
    # Ensure an empty list is handled correctly
    assert collect_pairs([]) == []

def test_collect_pairs_single_pair():
    # Ensure correct output for a single pair of countries
    shipments = [['US', 'CA', 10],[‘CA', 'US',1]
    expected_result = [['US', 'CA', 10, 1]]
    assert collect_pairs(shipments) == expected_result

def test_collect_pairs_multiple_pairs():
    # Ensure correct output for multiple pairs of countries
    expected_result = [
        ['US', 'CA', 17, 7],
        ['US', 'IN', 14, 8],
        ['IN', 'CA', 12, 5]
    ]
    assert collect_pairs(sample_shipments) == expected_result

if __name__ == '__main__':
    pytest.main()
