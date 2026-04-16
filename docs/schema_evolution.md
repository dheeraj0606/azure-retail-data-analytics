# Schema Evolution Strategy

## Approach

We follow schema evolution principles:

- Additive changes allowed (new columns)
- Breaking changes require versioning
- Backward compatibility maintained

## Handling Changes

| Change Type     | Strategy                  |
|-----------------|---------------------------|
| Add column      | Auto-merge schema         |
| Remove column   | Deprecation cycle         |
| Type change     | Create new version        |
