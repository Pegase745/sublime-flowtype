# FlowType

*FlowType turns your Sublime Text 3 into a full featured Flow IDE.*

[![GitHub (pre-)release](https://img.shields.io/github/release/Pegase745/sublime-flowtype/all.svg)](https://github.com/Pegase745/sublime-flowtype/releases)
[![Build Status](https://travis-ci.org/Pegase745/sublime-flowtype.svg?branch=master)](https://travis-ci.org/Pegase745/sublime-flowtype)
[![Build status](https://ci.appveyor.com/api/projects/status/jofwwwr30ub7f8r2/branch/master?svg=true)](https://ci.appveyor.com/project/Pegase745/sublime-flowtype)
[![codecov](https://codecov.io/gh/Pegase745/sublime-flowtype/branch/master/graph/badge.svg)](https://codecov.io/gh/Pegase745/sublime-flowtype)
[![Code Climate](http://img.shields.io/codeclimate/github/Pegase745/sublime-flowtype.svg)](https://codeclimate.com/github/Pegase745/sublime-flowtype)
[![Gratipay User](https://img.shields.io/gratipay/user/Pegase.svg)](https://gratipay.com/~Pegase/)

<!-- [![Package Control](https://img.shields.io/packagecontrol/dt/FlowType.svg)]() -->

**Features**

* Add and remove flow pragma on a file
* Check file contents for flow errors and highlight regions
* Go to file containing the type definition
* View a variable's type definition
* Show a file's coverage
* Show a text spinner every time the flow cli is working
* Launch cli commands in a thread in order to never block the IDE

## Installation

This package can be installed using [Package Control](https://packagecontrol.io/). Simply install the `FlowType` package from the official repository.

Otherwise, you must clone this repository in your packages directory. You can find it using the `Preferences -> Browse Packages` menu from within Sublime Text.

```bash
$ git clone https://github.com/Pegase745/sublime-flowtype.git FlowType
```

## Usage

### Settings

The package settings can be modified in three places:

| Description | File Location | Menu Entry |
| ----------- | ------------- | ------------- |
| Global | `Packages/FlowType/FlowType.sublime-settings` | `Preferences > Package Settings > FlowType > Settings-Default` |
| User | `Packages/User/FlowType.sublime-settings` | `Preferences > Package Settings > FlowType > Settings-User` |
| Project (**recommended**) | `<projects_location>/<project_name>.sublime-project` | `Project > Edit Project` (*options must be placed under the settings key*) |

The default available configuration settings

| Key | Description | Default value |
| --- | ----------- | ------------- |
| `log_level` | Set logging level | `info` |
| `flow_bin_path` | Path to flow binary | /usr/local/bin/flow |
| `complete_with_builtintypes` | Allow completions of Flow built-in types | `true` |
| `suggest_autocomplete_on_edit` (**beta**) | Show autocomplete suggestions on edit | `false` |
| `check_contents_on_edit` | Check contents for Flow errors on edit | `true` |
| `check_contents_on_save` | Check contents for Flow errors on save | `false` |

### Key Bindings

The key bindings can be modified in two places:

| Description | File Location | Menu Entry |
| ----------- | ------------- | ------------- |
| Default | `Packages/Default/Default (Linux/OSX/Windows).sublime-keymap` | `Preferences > Key Bindings` |
| User | `Packages/User/Default (Linux/OSX/Windows).sublime-keymap` | `Preferences > Key Bindings` |

The default available key bindings

| Description | Linux/Windows | OSX |
| ----------- | ------------- | --- |
| View all errors | `ctrl+alt+c` | `super+alt+c` |
| Show autocomplete values | `ctrl+alt+space` | `super+alt+space` |

### Mouse Bindings

The mouse bindings can be modified in two places:

| Description | File Location |
| ----------- | ------------- |
| Default | `Packages/Default/Default (Linux/OSX/Windows).sublime-mousemap` |
| User | `Packages/User/Default (Linux/OSX/Windows).sublime-mousemap` |

The default available mouse bindings

| Description | Linux/Windows | OSX |
| ----------- | ------------- | --- |
| Go to definition | `ctrl+left-click` | `super+left-click` |
| View type | `ctrl+right-click` | `super+right-click` |

## Change Log

All notable changes to this project will be documented on the Github [Releases](https://github.com/Pegase745/sublime-flowtype/releases) page.

*This project adheres to [Semantic Versioning](http://semver.org/) and [Keep A Changelog](http://keepachangelog.com/).*

## License

This package is distributed under the terms of the MIT license. See the [LICENSE](LICENSE) file for more details.
