# passg

A minimal password generator that can generate passwords made up of random characters or
passphrases made up of random words (using the [EFF long word list](https://www.eff.org/dice)).

## Features

- Generate random-character passwords using a choice of built-in alphabets
  (full, readable, reduced, alphanumeric, alphabetic, or numeric only).
- Generate diceware-style passphrases from a word list, with optional
  capitalization and custom word separators.
- Copy a single password or passphrase directly to the clipboard with
  `--copy`, without printing it to the terminal.
- Optionally print an entropy-based quality assessment for the generated
  password or passphrase with `--quality`.
- Word lists are downloaded once and cached locally for future runs.

## Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) (Python package manager)
- `xclip` (for `--copy` to work on Linux)

## Installation

```bash
uv tool install .
uv tool update-shell
```

## Usage

### Passwords

Generate a list of random passwords using `passg`:

```bash 
passg
```

Output:

```
k6P5ayLtkbT-mL2ABV9?
.:m!bK7!DDB_cgw88UBt
h6Q$TCAQ9w%j5q!aK6U_
[...]
```

which is equivalent to calling `passg password` with no arguments:

```bash
passg password
```

Output:

```
.$4KmCzxxwirfQNf7Xvp
e?p:M%WS29egERW4JdUs
p;p2H.wbc2wkhF%f8bF;
[...]
```

You can also select a specific alphabet using `--alphabet`:

```bash
passg password --alphabet alphanum
```
Output:

```
cDR176vhG25UoO91Pf5x
ppmAI7WwOv3AoGNkzhfL
UiQp6ORn1dGkJBy68aTV
[...]
```


Available alphabet options are: 

|Option|Description|
|-|-|
|full|Full alphabet, i.e. letters, digits, and punctuation|
|readable|Readable alphabet, i.e. letters, digits, and punctuation without ambiguous characters: 0, O, o, 1, l, I|
|reduced|Reduced alphabet, i.e. letters, digits and punctuation that are commonly allowed in passwords|
|reduced-readable (default)|Reduced readable alphabet, i.e. letters, digits and punctuation that are commonly allowed in passwords without ambiguous characters: 0, O, o, 1, l, I|
|alpha|Only letters|
|alphanum|Only letters and digits|
|num|Only digits|

You can specify a length for the password using `--length`;

```bash
passg password --length 16
```

Output:

```
RyGMpLsxF7,Kp6.x
R$MrKd;D$%ki!BNT
:j;Et;SAxy9uAjnS
[...]
```

To generate a single password and copy it directly to the
clipboard instead of printing it, add `--copy`:

```bash
passg password --copy
```

### Passphrases

Generate a list of random passphrases using `passg passphrase`:

```bash
passg passphrase
``` 

Output:

```
RetryWieldableSaucinessHandinessStarship
OozyExhumeSplendidAfterlifeImpurity
EraserClimaticPayingFrostbiteShimmy
[...]
```

You can specify a length (i.e. number of words) for the passphrase using `--length`;

```bash
passg passphrase --length 3
```

Output:

```
CurtainEuphemismCelery
DeodorantFableCrying
CrazyDreamlandConjuror
[...]
```

To generate a single passphrase and copy it directly to the
clipboard instead of printing it, add `--copy`:

```bash
$ passg passphrase --copy
```

### Quality Assessment

To print an entropy-based quality assessment alongside the output, add
`--quality`:

```bash
passg password --quality
k6P5ayLtkbT-mL2ABV9?
.:m!bK7!DDB_cgw88UBt
h6Q$TCAQ9w%j5q!aK6U_
[...]
Password quality: very strong (entropy: 121.32 bits)
```

This also works for passphrases.

### More Options

See all available options for each command:

```console
passg password --help
passg passphrase --help
```

## License

This project is distributed under the terms specified in the LICENSE.md file.

## Contributing

Passg is an open-source project. For bug reports, feature requests, or contributions, please visit the [project repository](https://github.com/maxbrixner/passg).

## Support

For issues and support requests, please use the [project's issue tracker](https://github.com/maxbrixner/passg/issues)
