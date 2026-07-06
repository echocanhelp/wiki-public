# Echopedia User Directories

Every LINE user who interacts with EchoHsu gets a structured private directory.

## Structure

```
/users/
    └── [sanitized-username]/
        ├── profile.md          # Private wiki profile
        ├── voice-samples/      # Voice/audio samples (if consented)
        ├── documents/          # User-submitted documents and references
        ├── media/              # User-associated media (photos, videos)
        └── echofeelings.md     # Emotional/narrative memory
```

## Username Sanitization

Generated from LINE display name → lowercase, alphanumeric + hyphens only.

| Display Name | Sanitized Username |
|---|---|
| Lin Mei-Ling | lin-meiling |
| David Chen | david-chen |
| Sarah O'Brien | sarah-obrien |

## Creation Trigger

Directories are created by EchoHsu on **first meaningful interaction** (meets EchoFeelings quality signals checklist: 2-of-3 threshold for narrative depth, emotional valence, or cultural significance).

## Templates

The `.template/` directory contains the canonical file templates. Copy to new user directories using:

```bash
cp -r ~/.echo_system/users/.template ~/.echo_system/users/[sanitized-username]
```

Then populate `profile.md` with user-specific information.

## Privacy

All user directories are **private by default**. Never expose publicly without explicit user consent. See Operations Guide §3.8 (Identity Linking) for hash-based linking procedures.

## Notes for Archivist

- Review new user directories within 24 hours of creation
- Verify consent status and identity linking
- Flag any sensitive material for redaction
