# Pokemon Data Access - Adapt to Standards - Implementation Plan

## Implementation Progress

- [x] Phase 1: Project Setup Alignment ✅
- [ ] Phase 2: Code Quality and Testing
- [!] Phase 3: Schema, Workflow and Remediation [🚧Ph2]
- [!] Phase 4: Final Validation (compliance milestone) [🚧Ph3]
- [!] Phase 5: SPARC Design for Project Future (optional) [🚧Ph4]

## Summary of Deliverables Per Phase

### Phase 1: Project Setup Alignment ✅
☑ pytest.ini merged into pyproject.toml [tool.pytest.ini_options] (1.1)
☑ requires-python bumped to >=3.13, ruff target-version and mypy python_version updated (1.2)
☑ Dev dependency duplication resolved: pytest-cov consolidated to [dependency-groups].dev (1.3)
☑ .envrc gitignore coverage verified (1.4)

### Phase 2: Code Quality and Testing
☑ Baseline test results recorded in BASELINE_RESULTS.md (2.1)
☑ catch-log-rethrow anti-pattern removed from rdf_store.py _handle_errors (2.2)
☑ Redundant docstrings removed from rdf_store.py, schema_utils.py, sparql_utils.py (2.3)
☑ F-string logging calls converted to lazy formatting (2.4)
☐ Sentry SDK dependency added and monitoring module created (2.5)
☑ Integration test markers added to test_graph.py and test_rdf_store.py (2.6)
☑ Resource leak refactoring in test_graph.py (2.7)
☑ Print statements removed from tests (2.8)

### Phase 3: Schema, Workflow and Remediation
☐ Upstream schema defects documented (3.1)
☐ Justfile standard LinkML recipes added (3.2)
☐ Automated fixes applied via ruff and mypy (3.3)
☐ Post-autofix regression check completed (3.4)
☐ Manual fixes for remaining violations applied (3.5)

### Phase 4: Final Validation
☐ Full test suite with coverage report passing (4.1)
☐ All validators pass or violations explicitly accepted (4.2)
☐ Functional verification of core SPARQL operations (4.3)
☐ Documentation review completed (4.4)

### Phase 5: SPARC Design for Project Future
☐ Design decisions documented in 01-design-decisions.md (5.1)
☐ Ranked feature list with MVP scope identified (5.2)
☐ SPARC sections (Specification, Architecture, Pseudocode, Refinement) completed (5.3)
☐ SPARC design document produced at 01-sparc-design.md (5.4)

## Overview

The pokemon-data-access project is a Python library providing RDF/SPARQL data access to a LinkML-modeled Pokemon knowledge graph stored in MarkLogic. It currently sits at alpha maturity with working core functionality: SPARQL query execution, schema-driven data loading via Pydantic models, and a graph abstraction layer over the RDF store.

This remediation plan (ADPT type) brings the project into conformance with established workspace standards. The project has good bones — a working library with real test coverage against a live MarkLogic endpoint — but accumulated several common quality debt items: configuration fragmentation, dependency duplication, error handling anti-patterns, missing observability instrumentation, and test hygiene issues.

The plan proceeds in a logical dependency order: configuration alignment first (so the environment is clean), then code quality fixes (so the codebase is sound), then workflow tooling (so day-to-day development is smooth), then final validation, and concludes with a SPARC design session to define the project's future direction.

**Key Value**: After completing this plan the project will meet workspace quality standards (ruff exits zero, mypy exits zero, test coverage >= 80%), have production-grade error observability via Sentry, clean test infrastructure that distinguishes unit from integration tests, and a documented architectural vision for future development.

**Target Users**: Developers building applications that consume Pokemon knowledge graph data from MarkLogic via SPARQL.

**Constraints**: Tests require a live MarkLogic endpoint (ML_USER/ML_PASS from environment). All Python commands use `uv run`. The project uses Hatchling build system, not poetry or setuptools.

## Architecture

```
pokemon-app/data-access/
├── pyproject.toml               # Project config (Hatchling + uv)
├── justfile                     # Task runner recipes
├── .envrc                       # Local env vars (gitignored)
├── pytest.ini                   # To be merged into pyproject.toml
│
├── src/pokemon_data_access/
│   ├── __init__.py              # Package exports
│   ├── __about__.py             # Version string
│   ├── config.py                # pydantic-settings config (ML_USER, ML_PASS, etc.)
│   ├── rdf_store.py             # RDF store client (httpx to MarkLogic SPARQL endpoint)
│   ├── rdf.py                   # RDF namespace / term helpers
│   ├── graph.py                 # PokemonKG - high-level graph access layer
│   ├── schema_utils.py          # LinkML schema introspection utilities
│   ├── sparql_utils.py          # SPARQL query construction helpers
│   └── data/linkml/
│       ├── pokemon.yaml         # Copied LinkML schema
│       ├── linkml_pokemon.py    # Copied generated Pydantic models
│       └── (supporting yaml)
│
└── tests/
    ├── conftest.py              # Fixtures (graph_layer, rdf_store, etc.)
    ├── test_graph.py            # PokemonKG integration tests
    ├── test_rdf_store.py        # RDF store integration tests
    ├── test_schema_utils.py     # Schema utility tests
    ├── test_sparql_utils.py     # SPARQL utility tests
    └── test_pydantic.py         # Pydantic model tests
```

**Technology Stack:**

| Component | Technology | Notes |
|-----------|------------|-------|
| Build system | Hatchling + hatch-vcs | Dynamic versioning from git tags |
| Package manager | uv | Lockfile-based, [dependency-groups] for dev |
| HTTP client | httpx | SPARQL over HTTP to MarkLogic |
| Data modeling | pydantic-settings + linkml-runtime | Config and schema introspection |
| CLI | typer + rich | Entry point: pokemon-data-access |
| Testing | pytest + pytest-asyncio + pytest-cov | asyncio_mode=auto |
| Linting | ruff | Comprehensive rule set |
| Type checking | mypy | Strict mode |
| Monitoring | sentry-sdk (to be added) | Error tracking and performance |
| Task runner | just | Schema copy, coverage, etc. |

## Detailed Implementation Phases

### Phase 1: Project Setup Alignment ✅

**Goal**: Eliminate configuration fragmentation and dependency duplication so the project has a single clean source of truth in pyproject.toml and the Python version target reflects current reality.

#### Step 1.1: Merge pytest.ini into pyproject.toml ✅

**Implementation**:
- Read current pytest.ini contents (logging config, markers, etc.)
- Add matching entries to [tool.pytest.ini_options] in pyproject.toml
- Delete pytest.ini
- Verify pytest still discovers and runs tests correctly

**Deliverables**:
- [x] pytest.ini deleted
- [x] [tool.pytest.ini_options] in pyproject.toml contains all previous pytest.ini settings
- [x] `uv run pytest --collect-only` succeeds without warnings about config file

#### Step 1.2: Bump Python version target ✅

**Implementation**:
- Change `requires-python = ">=3.11"` to `requires-python = ">=3.13"` in [project]
- Change `target-version = "py311"` to `target-version = "py313"` in [tool.ruff]
- Change `python_version = "3.11"` to `python_version = "3.13"` in [tool.mypy]
- Update classifiers list to reflect 3.13 instead of 3.11

**Deliverables**:
- [x] pyproject.toml [project] requires-python is >=3.13
- [x] pyproject.toml [tool.ruff] target-version is py313
- [x] pyproject.toml [tool.mypy] python_version is "3.13"
- [x] Classifiers updated

#### Step 1.3: Consolidate dev dependencies ✅

**Implementation**:
- Identify the duplication: pytest-cov appears in both [project.optional-dependencies].dev and [dependency-groups].dev
- Remove pytest-cov from [project.optional-dependencies].dev
- Verify [dependency-groups].dev retains pytest-cov>=6.2.1
- Check if other packages in [project.optional-dependencies].dev should move to [dependency-groups].dev or stay as optional extras (pytest, pytest-asyncio, ruff, mypy, coverage are likely developer-only and should move)
- Update [project.optional-dependencies] accordingly

**Deliverables**:
- [x] pytest-cov appears only once (in [dependency-groups].dev)
- [x] [project.optional-dependencies].dev section cleaned of duplicates
- [x] `uv sync --dev` succeeds

#### Step 1.4: Verify .envrc gitignore ✅

**Implementation**:
- Check if a .gitignore file exists at the project root
- Verify .envrc is listed in .gitignore (it contains ML_USER=admin and ML_PASS=admin)
- If not gitignored, add it
- Verify git does not track .envrc (check git status)

**Deliverables**:
- [x] .envrc is listed in .gitignore (or .gitignore created with that entry)
- [x] .envrc is not tracked by git

**Validation Checkpoint**:
```bash
# Verify pyproject.toml is the single config source
uv run pytest --collect-only 2>&1 | head -20
# Expected: Tests discovered, no warning about multiple config files

# Verify Python version targets
grep "requires-python\|target-version\|python_version" pyproject.toml
# Expected: All show 3.13

# Verify no duplication
grep -n "pytest-cov" pyproject.toml
# Expected: Appears exactly once (in [dependency-groups].dev)

# Verify .envrc is gitignored
cat .gitignore | grep envrc
# Expected: .envrc appears in gitignore

# Functional smoke test: package still loads correctly after config changes
uv run pokemon-data-access --help
# Expected: CLI help output displayed
```
**User Validated**: ☐

### Phase 2: Code Quality and Testing

**Goal**: Achieve operational observability and clean test infrastructure — Sentry captures errors and performance, error handling is idiomatic, integration tests are isolated from unit tests, and test resources are properly managed.

#### Step 2.1: Baseline test run documentation ✅

**Implementation**:
- Run the full test suite against live MarkLogic endpoint
- Capture which tests pass, which fail, and which are skipped
- Note any flaky tests or ordering dependencies
- Record the baseline as a reference for regression checking in Phase 3

**Deliverables**:
- [x] Baseline test results recorded in BASELINE_RESULTS.md (pass/fail/skip counts, flaky tests)
- [x] Any pre-existing failures documented as known issues in BASELINE_RESULTS.md

#### Step 2.2: Fix catch-log-rethrow anti-pattern in rdf_store.py (TDD) ✅

**What**: The `_handle_errors` method (lines 117-124) currently catches `HTTPStatusError`, logs four separate log lines about it, then re-raises the exception. This is the catch-log-rethrow anti-pattern: the exception carries all the context itself, and Sentry (once added) will capture the full traceback. The extra logging just creates noise.

**Tests First**:
- Test: Confirm that after the fix, an HTTPStatusError raised by the store still propagates to the caller unchanged
- Test: Confirm the exception message and status code are preserved through propagation
- Verify: No log output generated for HTTP errors in normal test runs (error appears in Sentry, not logs)

**Implementation**:
- Remove the except block that catches, logs, and re-raises HTTPStatusError
- Let the exception propagate naturally from the httpx call
- Ensure the calling context (in rdf_store.py public methods) has sufficient context for Sentry to capture

**Deliverables**:
- [x] _handle_errors no longer catches-logs-rethrows HTTPStatusError
- [x] HTTPStatusError propagates naturally from httpx calls
- [x] Tests still pass (HTTP errors still surface correctly to callers)

#### Step 2.3: Remove redundant docstrings ✅

**What**: Approximately 10 docstrings across rdf_store.py, schema_utils.py, and sparql_utils.py just restate the function name in sentence form (e.g., `def get_classes(self):` followed by `"""Get classes."""`). These add no value and should be removed. Keep meaningful docstrings that describe non-obvious behavior, parameters, or return values.

**Implementation**:
- Scan each of the three files for docstrings that are trivially redundant with the function name
- Remove those docstrings (leave the function intact)
- Preserve any docstring that explains intent, caveats, or non-obvious behavior

**Deliverables**:
- [x] Redundant docstrings removed from rdf_store.py
- [x] Redundant docstrings removed from schema_utils.py
- [x] Redundant docstrings removed from sparql_utils.py
- [x] `uv run ruff check` still passes

#### Step 2.4: Convert f-string logging to lazy formatting ✅

**What**: Calls like `logger.info(f"Loading {count} pokemon")` eagerly format the string even if the log level is disabled. The correct pattern is `logger.info("Loading %s pokemon", count)` which defers formatting. Ruff rule LOG001/LOG002 covers this.

**Implementation**:
- Search all source files for `logger.*(f"` patterns
- Convert each to positional `%s` style lazy formatting
- Verify ruff LOG rules now pass

**Deliverables**:
- [x] All f-string logger calls converted to lazy `%s` formatting
- [x] `uv run ruff check --select LOG` passes clean

#### Step 2.5: Add Sentry SDK and monitoring module (TDD)

**What**: Sentry is mandatory for all projects. This step adds the sentry-sdk dependency and creates a `monitoring.py` module following the standard pattern. SPARQL operations will be instrumented with transactions and spans so performance regressions in MarkLogic queries are visible.

**Tests First**:
- Test: `setup_sentry()` does not raise (smoke test)
- Verify: After calling setup_sentry(), trigger a test exception, flush, and confirm it appears in Sentry Issues console (manual)
- Verify: A test transaction with a SPARQL span appears in Sentry Performance console (manual)

**Implementation**:

Add sentry-sdk to [project.dependencies] in pyproject.toml:
```
sentry-sdk = { version = ">=2.0.0", extras = ["httpx"] }
```

Create `src/pokemon_data_access/monitoring.py`:
```
setup_sentry(environment):
    initialize sentry_sdk with hardcoded DSN (obtain from user)
    set traces_sample_rate=0.03
    set environment, release from __version__
    enable attach_stacktrace, disable send_default_pii

instrument_sparql_query(store, query):
    start sentry transaction for "sparql.query"
    execute query
    finish transaction
    return result
```

Call `setup_sentry()` early in the CLI entry point `cli.py` / `main()`.

**Deliverables**:
- [ ] sentry-sdk dependency added to pyproject.toml
- [ ] `src/pokemon_data_access/monitoring.py` created with setup_sentry() and real DSN
- [ ] setup_sentry() called in CLI main()
- [ ] SPARQL operations instrumented with Sentry spans
- [ ] Smoke test: `test_setup_sentry_does_not_crash` passes
- [ ] Manual Sentry console verification completed (error tracking confirmed)
- [ ] Manual Sentry console verification completed (performance tracing confirmed)

#### Step 2.6: Add @pytest.mark.integration markers ✅

**What**: Tests in test_graph.py and test_rdf_store.py require a live MarkLogic endpoint. These should be marked `@pytest.mark.integration` so they can be skipped when the endpoint is unavailable and run selectively in CI that has endpoint access.

**Implementation**:
- Add `integration` marker definition to pyproject.toml [tool.pytest.ini_options] markers section
- Add `@pytest.mark.integration` decorator to all tests in test_graph.py that use the live endpoint
- Add `@pytest.mark.integration` decorator to all tests in test_rdf_store.py that use the live endpoint
- Verify `uv run pytest -m "not integration"` runs without needing MarkLogic

**Deliverables**:
- [x] `integration` marker registered in pyproject.toml
- [x] All live-endpoint tests in test_graph.py marked with @pytest.mark.integration
- [x] All live-endpoint tests in test_rdf_store.py marked with @pytest.mark.integration
- [x] `uv run pytest -m "not integration"` passes without MarkLogic

#### Step 2.7: Fix resource leaks in test_graph.py ✅

**What**: Approximately 10 tests in test_graph.py (lines 280-624) create `PokemonKG()` instances inline without using the `graph_layer` fixture or context managers. These instances hold httpx client connections and may not be properly closed, causing resource leaks and potentially interfering with other tests.

**Implementation**:
- Identify all inline `PokemonKG()` instantiations in tests (lines 280-624)
- Refactor each to use either the existing `graph_layer` fixture (if appropriate) or a `with` context manager pattern
- If PokemonKG does not implement a context manager, add `__enter__`/`__exit__` (or an async equivalent) that closes the httpx client
- Verify all tests still pass after refactoring

**Deliverables**:
- [x] All inline PokemonKG() instantiations replaced with fixture or context manager usage
- [x] PokemonKG supports context manager protocol (if not already)
- [x] No resource leak warnings from pytest

#### Step 2.8: Remove print() statements from tests ✅

**What**: Test files should not use print() for output — they should use logging or pytest's capsys/caplog fixtures when output inspection is needed. Lines 220, 276, 337, 395, 405, 451-457, 530-554, 585-589, and 621 in test_graph.py contain print() calls that were used for debugging and were never cleaned up.

**Implementation**:
- Remove all print() calls from test_graph.py at the identified lines
- Remove T201 from the ruff ignore list (or make it apply only to non-test files) so future print() in tests is caught automatically
- Run ruff check to confirm T201 violations are resolved

**Deliverables**:
- [x] All print() statements removed from test_graph.py
- [x] T201 ignore rule removed or scoped appropriately in pyproject.toml
- [x] `uv run ruff check tests/` passes without T201 suppression

**Validation Checkpoint**:
```bash
# Verify baseline and integration markers
uv run pytest -m "not integration" -v
# Expected: Unit tests and schema tests pass; integration tests skipped

# Verify Sentry smoke test
uv run pytest tests/test_monitoring.py -v
# Expected: test_setup_sentry_does_not_crash passes

# Verify ruff is clean
uv run ruff check src/ tests/
# Expected: No errors (or only accepted suppressions)

# Verify Sentry receives events (manual)
# Expected: Test event visible in Sentry Issues console at sentry.r4.v-lad.org
# Expected: Test transaction visible in Sentry Performance console
```
**User Validated**: ☐

### Phase 3: Schema, Workflow and Remediation

**Goal**: Achieve full standards compliance — clean linters, clean type checker, smooth workflow tooling — while documenting upstream schema debt for the pokemon project.

#### Step 3.1: Document upstream schema defects

**What**: Several defects exist in the upstream pokemon project's LinkML schema that affect this library. Documenting them creates a clear actionable list for the pokemon project maintainer.

**Implementation**:
- Open `src/pokemon_data_access/data/linkml/pokemon.yaml` and identify:
  - Line 280: `describedInPokedex` uses `description` as a list (should be a string)
  - Line 297: `featuresSpecies` uses `description` as a list (should be a string)
  - Missing `tree_root: true` annotation on the root class
  - Missing `version:` field in the schema header
  - Approximately 15 classes using `annotations.rdfs:comment` instead of the `description:` field
- Create a brief document or inline comments in the schema copy noting each defect with line reference
- Optionally open issues in the pokemon project if there is a tracker

**Deliverables**:
- [ ] SCHEMA_DEFECTS.md created listing all upstream defects with file and line references
- [ ] (Optional) Issues opened in pokemon project tracker

#### Step 3.2: Add standard LinkML recipes to justfile

**What**: The current justfile has schema copy and coverage recipes but is missing standard LinkML development recipes that make day-to-day work uniform across workspace projects.

**Implementation**:
- Add these missing recipes to the justfile:
  - `lint`: run ruff check on src/ and tests/
  - `gen-project`: copy schema and regenerate models in one step
  - `gen-python`: run gen-python against the local schema copy
  - `test`: run pytest (integration + unit if endpoint available)
  - `test-unit`: run pytest excluding integration markers
  - `serve-docs`: placeholder or mkdocs serve if docs exist
  - `clean`: remove __pycache__, .pytest_cache, htmlcov, .mypy_cache
  - `install`: uv sync --dev

**Deliverables**:
- [ ] `just lint` runs ruff check
- [ ] `just test` runs full test suite
- [ ] `just test-unit` runs tests excluding integration markers
- [ ] `just clean` removes build artifacts
- [ ] `just install` runs uv sync --dev
- [ ] `just --list` shows all recipes with descriptions

#### Step 3.3: Apply automated fixes

**Implementation**:
- Run `uv run ruff check --fix src/ tests/` to apply all safe auto-fixes
- Run `uv run mypy src/` and record any type errors
- Apply any mypy-reported issues that can be fixed mechanically (missing type annotations on non-test code, etc.)

**Deliverables**:
- [ ] `uv run ruff check --fix` applied to src/ and tests/
- [ ] `uv run mypy src/` run and output captured
- [ ] Mechanical mypy fixes applied

#### Step 3.4: Post-autofix regression check

**Implementation**:
- Run full test suite after automated fixes
- Compare pass/fail counts to Phase 2 baseline
- Investigate and fix any regressions introduced by automated fixes

**Deliverables**:
- [ ] Test suite passes post-autofix at same or better rate than Phase 2 baseline
- [ ] Any regressions investigated and resolved

#### Step 3.5: Manual fixes for remaining violations

**What**: Some violations require judgment or manual cleanup:
- `from __future__ import annotations` imports are unnecessary for Python 3.13+ (PEP 563 behavior is the default)
- Typing imports like `from typing import List, Dict` should be replaced with built-in generics (`list[str]`, `dict[str, Any]`)
- Module docstrings that just say what the module is named should be improved or removed
- Test files should not import typing constructs that are unnecessary

**Implementation**:
- Remove `from __future__ import annotations` from all source and test files
- Replace `typing.List`, `typing.Dict`, `typing.Optional`, `typing.Tuple` etc. with native generics throughout src/
- Remove or improve content-free module docstrings
- Run ruff UP rules to catch any remaining modern-Python equivalence violations

**Note**: These changes are syntactic modernizations that do not alter runtime behavior. The regression check in Step 3.4 confirms existing tests cover the affected code. Re-run `uv run pytest` after completing manual fixes to verify.

**Deliverables**:
- [ ] No `from __future__ import annotations` in any file
- [ ] No deprecated `typing.List/Dict/Optional/Tuple` usage in src/ files
- [ ] Module docstrings improved or removed where they were content-free
- [ ] `uv run ruff check src/ tests/` fully clean

**Validation Checkpoint**:
```bash
# Verify ruff is fully clean
uv run ruff check src/ tests/
# Expected: No output (all clean)

# Verify mypy is clean
uv run mypy src/
# Expected: Success: no issues found (or documented accepted suppressions)

# Verify justfile recipes work
just lint
just test-unit
just clean
# Expected: Each recipe executes without error

# Confirm schema defect doc exists
cat SCHEMA_DEFECTS.md
# Expected: Lists upstream schema issues with line references
```
**User Validated**: ☐

### Phase 4: Final Validation

**Goal**: Confirm the full project meets quality gates across all dimensions: tests, static analysis, functional behavior, and documentation.

#### Step 4.1: Full test suite with coverage

**Implementation**:
- Run complete test suite including integration tests (requires live MarkLogic endpoint)
- Generate coverage report
- Verify coverage is above 80% for src/ code

**Deliverables**:
- [ ] `uv run pytest --cov=src --cov-report=term-missing` completes
- [ ] Coverage report shows >= 80% for pokemon_data_access package
- [ ] All integration tests pass against live MarkLogic endpoint

#### Step 4.2: Validators clean

**Implementation**:
- Run ruff in strict mode
- Run mypy
- Document any remaining violations as explicitly accepted with rationale

**Deliverables**:
- [ ] `uv run ruff check src/ tests/` passes clean (zero violations)
- [ ] `uv run mypy src/` passes clean (zero errors)
- [ ] Any accepted suppressions have inline comments explaining rationale

#### Step 4.3: Functional verification

**Implementation**:
- Verify the CLI entry point works: `uv run pokemon-data-access --help`
- Verify a basic SPARQL query executes against MarkLogic and returns data
- Verify schema utils correctly introspect the pokemon schema
- Verify Sentry setup_sentry() smoke test passes and test event appears in Sentry console
- Verify failure mode: unreachable MarkLogic endpoint raises clear error (not unhandled exception)
- Security check: credentials sourced only from environment (never hardcoded), Sentry DSN does not leak in CLI output or logs, .envrc confirmed gitignored

**Deliverables**:
- [ ] `uv run pokemon-data-access --help` shows CLI help
- [ ] A SPARQL query against live endpoint returns results
- [ ] Schema introspection returns expected class list
- [ ] Sentry setup_sentry() smoke test passes and test event confirmed in Sentry console

#### Step 4.4: Documentation review

**Implementation**:
- Read README.md and verify it accurately describes the project, installation, and basic usage
- Add Operations Notes section to README.md: how to configure ML_USER/ML_PASS, how to run integration vs unit tests, how to respond to Sentry alerts
- Verify CHANGES.md exists and has at least an initial entry documenting this remediation work
- Verify the justfile `--list` output gives meaningful descriptions of all recipes

**Deliverables**:
- [ ] README.md is accurate and complete for current state
- [ ] CHANGES.md has an entry for the standards-alignment work
- [ ] `just --list` shows meaningful recipe descriptions
- [ ] README.md includes Operations Notes section

**Validation Checkpoint**:
```bash
# Full test run with coverage
uv run pytest --cov=src --cov-report=term-missing -v
# Expected: All tests pass, >= 80% coverage

# Validators
uv run ruff check src/ tests/ && echo "ruff OK"
uv run mypy src/ && echo "mypy OK"
# Expected: Both print OK

# Functional check
uv run pokemon-data-access --help
# Expected: Shows help with available commands

# Documentation check
test -f README.md && test -f CHANGES.md && echo "docs OK"
# Expected: docs OK
```
**User Validated**: ☐

### Phase 5: SPARC Design for Project Future

**Goal**: Conduct an architectural design conversation to define the project's vision and produce a SPARC design document guiding future development beyond standards compliance.

#### Step 5.1: Interactive design conversation

**What**: Before writing any code, the right architectural decisions must come from understanding what users need this library to do. This is an open-ended conversation about the project's future.

**Implementation**:
- Discuss questions such as:
  - What query patterns do consumers of this library most commonly use?
  - Should the library expose a query builder API or raw SPARQL execution?
  - Is async-first the right design or should sync be primary?
  - What caching strategy makes sense for MarkLogic query results?
  - Should the library own schema introspection or delegate fully to linkml-runtime?
  - What authentication patterns beyond ML_USER/ML_PASS should be supported?

**Deliverables**:
- [ ] Design conversation completed, key decisions documented in `.claude/plans/POKEMON-DATA-ACCESS-01/01-design-decisions.md`

#### Step 5.2: Feature and enhancement prioritization

**What**: Based on the design conversation, identify and rank the most valuable features to add.

**Implementation**:
- List candidate features (query builder, result caching, bulk loading, schema validation on write, etc.)
- Prioritize by user value and implementation complexity
- Identify which features form a natural MVP for the next development cycle

**Deliverables**:
- [ ] Ranked feature list produced
- [ ] Next-cycle MVP features identified

#### Step 5.3: Run full SPARC flow

**What**: Execute the Specification, Architecture, Pseudocode, Refinement flow for the prioritized feature set to produce a complete architectural blueprint.

**Implementation**:
- Specification: Document what the enhanced library must do, for whom, and how success is measured
- Architecture: Design the module structure, interfaces, and data flows for the new features
- Pseudocode: Sketch key algorithms and data transformations in language-neutral pseudo-code
- Refinement: Review the design for gaps, risks, and simplifications

**Deliverables**:
- [ ] Specification section completed
- [ ] Architecture section completed with module diagram
- [ ] Pseudocode sketches for key operations
- [ ] Refinement pass completed

#### Step 5.4: Produce SPARC design document

**Implementation**:
- Write the SPARC design document to `.claude/plans/POKEMON-DATA-ACCESS-01/01-sparc-design.md`
- Include all four SPARC sections
- Include a feature roadmap section ordering the prioritized capabilities

**Deliverables**:
- [ ] SPARC design document written at `.claude/plans/POKEMON-DATA-ACCESS-01/01-sparc-design.md`
- [ ] Document reviewed and accepted by user

**Validation Checkpoint**:
```bash
# Verify SPARC document exists
test -f .claude/plans/POKEMON-DATA-ACCESS-01/01-sparc-design.md && echo "SPARC doc exists"
# Expected: SPARC doc exists

# Confirm document has all four SPARC sections
grep -E "^## (Specification|Architecture|Pseudocode|Refinement)" \
    .claude/plans/POKEMON-DATA-ACCESS-01/01-sparc-design.md
# Expected: All four section headers found
```
**User Validated**: ☐

## Dependencies

**External Dependencies:**
- Python >= 3.13
- uv package manager
- Live MarkLogic endpoint for integration tests (ML_USER and ML_PASS in environment)
- Sentry instance (private: sentry.r4.v-lad.org or SaaS: sentry.io) for Sentry DSN

**Internal Dependencies:**
- linkml-runtime (editable install from ../../linkml-runtime)
- pokemon project schema files (copied via `just copy-schema`)

## Notes

**Testing Approach:**
- Integration tests require live MarkLogic endpoint; use `@pytest.mark.integration` to separate them
- Unit tests (schema_utils, sparql_utils, pydantic models) should pass without MarkLogic
- Real services preferred over mocks per workspace standards

**ADPT Context:**
- This is a remediation plan for an existing project, not a greenfield build
- Phase 1-3 are cleanup; Phase 4 is validation; Phase 5 is forward design
- The project has working functionality that must be preserved throughout
- The project already has basic logging and test infrastructure; Phase 1 consolidates config, Phase 2 adds production-grade Sentry observability
- Phase 5 is optional — work can stop after Phase 4 and the compliance goal is fully achieved

**Sentry DSN:**
- Obtain real DSN from user before starting Phase 2, Step 2.5
- Use private Sentry instance (sentry.r4.v-lad.org) as default for this internal tool

**Known Pre-existing Issues:**
- Upstream pokemon schema defects (documented in Phase 3.1) are out of scope to fix here; only document them
- The justfile uses emoji in echo statements (will be preserved as-is unless ruff flags them)

**Known Risks:**
- Sentry DSN must be obtained from user before Phase 2 Step 2.5 can start — this is an external blocker that could stall mid-phase if not arranged in advance
- Automated ruff/mypy fixes in Phase 3.3 may alter behavior in edge cases — mitigated by Phase 3.4 regression check against Phase 2 baseline
- MarkLogic endpoint availability required for integration tests — no fallback strategy; unit tests run independently via `pytest -m "not integration"`
