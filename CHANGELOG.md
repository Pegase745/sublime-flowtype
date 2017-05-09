# Change log

All notable changes to this project will be documented in this file.
*This project adheres to [Semantic Versioning](http://semver.org/) and [Keep A Changelog](http://keepachangelog.com/).*

## [Unreleased]
### Added
  * Add `ctrl+alt+c` as a keybinding for `check_contents`.

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

[Unreleased]: https://github.com/Pegase745/sublime-flowtype/compare/v1.0.0-alpha.1...master
[v1.0.0-alpha.1]: https://github.com/Pegase745/sublime-flowtype/compare/v1.0.0-alpha...v1.0.0-alpha.1
[v1.0.0-alpha]: https://github.com/Pegase745/sublime-flowtype/compare/v1.0.0-alpha