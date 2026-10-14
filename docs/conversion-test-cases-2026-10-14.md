# Unit Converter Test Cases

| Case | Expected behavior |
|---|---|
| Same unit to same unit | Value stays unchanged |
| Zero input | Valid zero result |
| Negative input | Allowed only for compatible dimensions |
| Blank input | Show validation feedback |
| Unknown unit | Do not attempt conversion |
| Very small value | Preserve useful precision |