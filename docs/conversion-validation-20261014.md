# Conversion Validation

- Source and target units must belong to the same dimension.
- Converting a unit to itself should preserve the input value.
- Reject non-finite values and invalid unit selections.
- Use a canonical unit for each dimension to reduce formula duplication.
- Apply rounding only when formatting the displayed result.