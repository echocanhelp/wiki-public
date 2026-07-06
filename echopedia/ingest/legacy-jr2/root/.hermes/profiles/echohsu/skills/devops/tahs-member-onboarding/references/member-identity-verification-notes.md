# Member Identity Verification Notes (Chinese + English Name)

Use this note when drafting or revising TAHS member pages where public web evidence is sparse.

## Query Patterns
- "<中文名>"
- "<中文名>" "<English name>"
- "<中文名>" "Taiwanese American Historical Society"
- "<中文名>" "台美史料協會"
- "<中文名>" site:github.com
- "<中文名>" site:linkedin.com

## Confidence Rubric
- **High**: direct self-published profile, official org page, or owner/admin-confirmed identity.
- **Medium**: multiple independent sources align, but no direct confirmation.
- **Low**: noisy/irrelevant search landscape, weak or single-source hints.

## Publication Rule
- If confidence is low, keep page in `pending_verification` and avoid publishing social/profile mappings as facts.
- Store uncertain leads in verification notes only.
- Promote claims to biography text only after explicit member or owner/admin confirmation.

## False-Positive Cleanup
If a profile linkage is corrected as false positive:
1. Remove handle/link immediately.
2. Remove any derived claim based on that handle.
3. Lower confidence and mark verification pending.
4. Add dated revision note describing correction.
