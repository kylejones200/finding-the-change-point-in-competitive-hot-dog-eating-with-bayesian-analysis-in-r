# Finding the Change Point in Competitive Hot Dog Eating with Bayesian Analysis

This project demonstrates Bayesian change point detection techniques.

## Business context

Competitive eating is a curious sport. Part gluttony, part tradition, part innovation. The most famous is Nathan's Hot Dog Eating Contest, held annually in NY Coney Island (with a few exceptions) since 1974 ([data](https://en.wikipedia.org/wiki/Nathan%27s_Hot_Dog_Eating_Contest)).

Starting in 1974, the contest unfolded in a predictable pattern --- a small group of amateurs would gather on Coney Island and devour as many hotdogs as humanly possible. The winner's tally was generally modest (if eating 15 hotdogs in 12 mins is modest). That changed in 2001.

Takeru Kobayashi shocked the crowd (and the organizers) by consuming 50 hot dogs in 12 minutes. The organizers didn't have signs for numbers that high --- so they had to handwrite the increasing tally on sheets of paper.

## Article

Medium article: [Finding the Change Point in Competitive Hot Dog Eating with Bayesian Analysis in R](https://medium.com/@kylejones_47003/finding-the-change-point-in-competitive-hot-dog-eating-with-bayesian-analysis-in-r-57b4dc95c97b)

## Project Structure

```
.
├── README.md           # This file
├── main.py            # Main entry point
├── config.yaml        # Configuration file
├── requirements.txt   # Python dependencies
├── src/               # Core functions
│   ├── core.py        # Change point detection functions
│   └── plotting.py    # Tufte-style plotting utilities
├── tests/             # Unit tests
├── data/              # Data files
└── images/            # Generated plots and figures
```

## Configuration

Edit `config.yaml` to customize:
- Data source or synthetic generation
- Change point parameters
- Detection method and window
- Output settings

## Change Point Detection

Methods demonstrated:
- Sliding Window: Compare means before/after potential change points
- Bayesian Approach: Prior on change point location, posterior inference
- Uncertainty: Quantify uncertainty in change point location

## Caveats

- By default, generates synthetic data with known change point.
- Full Bayesian implementation requires probabilistic programming.
- Window size affects detection sensitivity.

## Disclaimer

Educational/demo code only. Not financial, safety, or engineering advice. Use at your own risk. Verify results independently before any production or operational use.

## License

MIT — see [LICENSE](LICENSE).