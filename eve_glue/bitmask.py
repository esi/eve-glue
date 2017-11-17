"""Helpers for dealing with integer representations of bitmasks."""


def mask_list(mask):
    """Return the list of set bits in a mask as integers."""

    set_bits = []

    for position, bit in enumerate(reversed(bin(mask)[2:])):
        if bit == "1":
            set_bits.append(int("1{}".format("0" * position), base=2))

    return set_bits


def num_set_bits(mask):
    """Return a count of set bits in a given mask."""

    return bin(mask).count("1")


def trailing_zero_bits(mask):
    """Return a count of trailing zero bits in the mask."""

    # NB: why would anyone care?
    mask_str = bin(mask)
    mask_len = len(mask_str)
    right_most_set_bit = mask_str.rfind("1")

    if right_most_set_bit > 0:
        return mask_len - right_most_set_bit - 1

    return mask_len
