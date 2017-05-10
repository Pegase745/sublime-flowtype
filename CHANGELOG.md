# Change log

All notable changes to this project will be documented in this file.
*This project adheres to [Semantic Versioning](http://semver.org/) and [Keep A Changelog](http://keepachangelog.com/).*

## [Unreleased]

## [v1.0.0-alpha.3] - 2017-05-10
### Added
  * Add `goto_definition` command binded to `ctrl+left-mouse-click`.
  * Add `view_type` command binded to `ctrl+right-mouse-click`.
  * Add `coverage` command showing percentage of uncovered lines in status bar.
  * Add `autocomplete` command showing Flow suggestions on `ctrl+alt+space`, and is also activate by default on file edit.
  * Add `suggest_annotations` applying suggested type annotations to file.

### Changed
  * Activate check contents by default on file save, without showing the quick panel.

### Fixed
  * Show error context and full description in quick panel.
  * Use `--quiet` option to suppress output about server startup.
  * Don't include commands in coverage until the separation of unit and functional tests.
  * Fix autocomplete trigger and show type as the suggestion's description.
  * Don't add a pragma if it's already there.

## [v1.0.0-alpha.2] - 2017-05-09
### Added
  * Add `ctrl+alt+c` as a keybinding for `check_contents`.

### Changed
  * Show the errors in a quick panel instead of status bar.

## [v1.0.0-alpha.1] - 2017-05-08
### Added
  * Add a spinner in status bar for threaded processes.

### Fixed
  * Run `check_contents` in a thread in order to not freeze UI.
  * Fix `check_contents` result not showing on Flow server initialization.

## [v1.0.0-alpha] - 2017-05-06
### Added
  * Auto-complete built-in types available in Flow 0.44.0.
  * Add an `Check contents` command checking the contents of a JS file, listing the errors and highlighting corresponding regions.
  * Add an `Add pragma` command inserting the pragma on the first row of a JS file.
  * Add tests raising coverage to 99%.

[Unreleased]: https://github.com/Pegase745/sublime-flowtype/compare/v1.0.0-alpha.2...master
[v1.0.0-alpha.2]: https://github.com/Pegase745/sublime-flowtype/compare/v1.0.0-alpha.1...v1.0.0-alpha.2
[v1.0.0-alpha.1]: https://github.com/Pegase745/sublime-flowtype/compare/v1.0.0-alpha...v1.0.0-alpha.1
[v1.0.0-alpha]: https://github.com/Pegase745/sublime-flowtype/compare/v1.0.0-alpha