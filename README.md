# IOCVault

> Normalize and deduplicate indicators for defensive analysis.

IOCVault is a small Python utility for cleaning indicator data before it is consumed by security analysis or reporting pipelines.

## Features

- Detect common indicator types
- Normalize case and surrounding whitespace
- Deduplicate indicators while preserving input order
- Keep processing local and deterministic
- Zero network requirement

## Workflow

```text
raw indicators
      ↓
normalize
      ↓
identify
      ↓
deduplicate
      ↓
structured collection
```

## Example

```python
from iocvault import normalize, deduplicate

items = [" Example.COM ", "example.com", "192.0.2.1"]
clean = deduplicate(normalize(items))
print(clean)
```

Check the package source and tests for the exact supported API.

## Scope

IOCVault is intended for defensive analysis of data you are authorized to handle. It does not perform exploitation or remote access.

## Development

```bash
python -m pytest
```

## License

MIT. See `LICENSE`.

## Author

Built by **Medu** · https://guns.lol/meduu