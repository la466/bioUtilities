from numpy.testing import assert_equal

def check_named_results(observed, expected, attributes):
    """
    Check that named results are equal.
    """

    for i, attribute in enumerate(attributes):
        assert_equal(getattr(observed, attribute), expected[i])
