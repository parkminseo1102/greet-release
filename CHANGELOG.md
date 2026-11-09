# Changelog

All notable changes to this project will be documented in this file.
The format is based on Keep a Changelog 1.1.0, and this project adheres to Semantic Versioning.

## [Unreleased]

## [0.2.0] - 2026-11-09

### Added
- `greet()` now accepts a `punctuation` parameter (default `!`), allowing custom punctuation marks instead of a fixed exclamation mark.

### Fixed
- `greet()` now uses "world" when name is empty or whitespace-only instead of returning incomplete greetings like "Hello, !".

## [0.1.0] - 2026-11-09

### Added
- `greet()` function returning a greeting and CLI entrypoint `main()` printing greeting to stdout.
