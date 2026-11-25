# Fix Human Sleep: Funniest Patch Note

[![make.fun](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![Rank](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/Hasanrdp/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/rank.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![Reward](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/Hasanrdp/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/reward.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

One line of patch notes announcing that human sleep has been fixed,
written for the [Fix Human Sleep: Funniest Patch Note](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
competition on make.fun.

## The line

> Fixed: sleep no longer requires 45 minutes of staring at the ceiling while replaying an embarrassing moment from 2014.

118 characters, one line. The joke is the most common sleep bug in the
field: the brain refusing to shut down until it has replayed an old
embarrassment, now fixed like any other defect in a changelog.

## How it works

`main.py` (Python 3.13, standard library only) writes exactly that line
to `entry.txt` in the output directory. It is fully deterministic: the
same bytes on every run, no network, no clock, no randomness. Before
writing, the program checks the line against its pinned length (118
characters / 118 bytes) and SHA-256 hash, and refuses to write anything
if they do not match.

## Run it

```sh
python3 main.py
```

It writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` when set, otherwise to
`/output/entry.txt`, falling back to `./out/entry.txt` when neither is
available.

## License

MIT. See [LICENSE](LICENSE).
