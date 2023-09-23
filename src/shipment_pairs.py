

# FIELDS: ORIGIN, DESTINATION, QUANTITY
SHIPMENTS = [
    ['US', 'US', 8],
    ['US', 'IN', 14],
    ['US', 'CA', 4],
    ['US', 'MX', 7],
    ['US', 'VE', 13],
    ['IN', 'US', 3],
    ['IN', 'IN', 13],
    ['IN', 'CA', 18],
    ['IN', 'MX', 16],
    ['IN', 'VE', 3],
    ['CA', 'US', 8],
    ['CA', 'IN', 20],
    ['CA', 'CA', 16],
    ['CA', 'MX', 3],
    ['CA', 'VE', 2],
    ['MX', 'US', 12],
    ['MX', 'IN', 20],
    ['MX', 'CA', 3],
    ['MX', 'MX', 3],
    ['MX', 'VE', 8],
    ['VE', 'US', 3],
    ['VE', 'IN', 7],
    ['VE', 'CA', 5],
    ['VE', 'MX', 15],
    ['VE', 'VE', 13],
 ]


def remove_intra(shipments):
    """remove_intra removes any records in which the origin and destination are the
    same country.
    """
    return [shipment for shipment in shipments if shipment[0] != shipment[1]]


def collect_pairs(shipments):
    """collect_pairs collects shipments for each unique country pair on one row.
    Note: the entire data set should be sorted on shipment count--largest first.

    The resulting fields (since origin and destinations are on the same row) will
    be:
        COUNTRY_A, COUNTRY_B, QUANTITY_AB, QUANTITY_BA

    Example:
    >>> shipments = [
         ['US', 'IN', 14],
         ['US', 'CA', 17],
         ['IN', 'US', 8],
         ['IN', 'CA', 12],
         ['CA', 'US', 7],
         ['CA', 'IN', 5],
     ]
    >>> collect_pairs(shipments)
    [
        ['US', 'CA', 17, 7],
        ['US', 'IN', 14, 8],
        ['IN', 'CA', 12, 5],
    ]
    """
    countries_shipments = {}

    # assert that there are no intra
    shipments = remove_intra(shipments)

    # sort on quantity
    shipments = sorted(shipments, key=lambda x: x[2], reverse=True)

    for orig, dest, quant in shipments:
        if (dest, orig) in countries_shipments:
            countries_shipments[(dest, orig)].append(quant)
        else:
            countries_shipments[(orig, dest)] = [quant]
    return [
        [loc_a, loc_b, quant_ab, quant_ba] for (loc_a, loc_b), (quant_ab, quant_ba)
        in countries_shipments.items()
    ]




if __name__ == '__main__':
    little_shipments = [
        ['US', 'IN', 14],
        ['US', 'CA', 17],
        ['IN', 'US', 8],
        ['IN', 'CA', 12],
        ['CA', 'US', 7],
        ['CA', 'IN', 5],
    ]

    # Part 1
    export_only = remove_intra(little_shipments)
    print('#' * 80, ' ' * 30 + 'Intra Removed', '#' * 80, sep='\n')
    print(export_only)

    # Part 2
    shipment_pairs = collect_pairs(little_shipments)
    print('\n', '#' * 80, ' ' * 30 + 'Pairs collected', '#' * 80, sep='\n')
    print(shipment_pairs)


