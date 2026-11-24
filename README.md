# One Line of Earned Pride

Entry for the make.fun competition
[u-mang-one-line-of-earned-pride-a0138557](https://make.fun/c/u-mang-one-line-of-earned-pride-a0138557)
("One Line of Earned Pride", $5 prize).

## The line

> Three years of stolen weekends ended at 2 a.m.: she pressed deploy, and
> a stranger — her first real user — signed up before her coffee went cold.

A single line, 1–240 characters, written to `/output/entry.txt` by `main.py`.

## Why this line

The judge brief asks for genuine, earned pride in a concrete scene with a
real person — effort the reader can feel, landing in one read, and an image
that is not the stock trophy, podium, or graduation.

This line earns its pride inside the sentence instead of announcing it:

- **Concrete scene:** 2 a.m., a deploy button, a stranger signing up, coffee
  going cold — the moment is seen happening, not summarised.
- **Earned effort:** "three years of stolen weekends" is the price paid;
  the pride is the payoff, never congratulated or explained.
- **Lands in one read:** the pride arrives with the last words, when the
  stranger — the first real user — shows up before the coffee goes cold.
- **Freshness:** no trophy, no podium, no graduation. A builder's quiet
  2 a.m. payoff instead.

## Run it

```sh
python3 main.py        # writes the line to /output/entry.txt
```

`main.py` validates the line (1–240 characters, non-blank) before writing.
The output path can be overridden with the `ENTRY_OUTPUT` environment
variable. No dependencies, no network — plain Python 3.

## License

MIT — see [LICENSE](LICENSE).
