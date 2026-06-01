---
author: "Kyle Jones"
date_published: "October 21, 2024"
date_exported_from_medium: "November 10, 2025"
canonical_link: "https://medium.com/@kyle-t-jones/finding-the-change-point-in-competitive-hot-dog-eating-with-bayesian-analysis-in-r-57b4dc95c97b"
---

# Finding the Change Point in Competitive Hot Dog Eating with Bayesian Analysis in R Competitive eating is a curious sport. Part gluttony, part tradition,
part innovation. The most famous is Nathan's Hot Dog Eating Contest...

### Finding the Change Point in Competitive Hot Dog Eating with Bayesian Analysis in R 

Competitive eating is a curious sport. Part gluttony, part tradition, part innovation. The most famous is Nathan's Hot Dog Eating Contest, held annually in NY Coney Island (with a few exceptions) since 1974 ([data](https://en.wikipedia.org/wiki/Nathan%27s_Hot_Dog_Eating_Contest)).

Starting in 1974, the contest unfolded in a predictable pattern --- a small group of amateurs would gather on Coney Island and devour as many hotdogs as humanly possible. The winner's tally was generally modest (if eating 15 hotdogs in 12 mins is modest). That changed in 2001.

Takeru Kobayashi shocked the crowd (and the organizers) by consuming 50 hot dogs in 12 minutes. The organizers didn't have signs for numbers that high --- so they had to handwrite the increasing tally on sheets of paper.

It felt like something from another world. But could it last, or was this just a fluke? Then Kobayashi won the contest six times in a row. Not a fluke --- a new era. Nathan's Hot Dog Eating Contest data starts in 1974. There is an apocryphal story about it starting in 1916, but that appears to have been created for publicity. I wanted to understand if we could use bayesian analysis to find the year when hotdog consumption changed (in a statistically significant way).

There are caveats to consider with the competition factors to consider, such as changes in the length of the competition (from 12 minutes to 10 minutes in recent years) and the emergence of female champions like Sonya "The Black Widow" Thomas. Focusing solely on the male winners for this analysis, is 2001 the "change point" year?

The math for this process can be tricky and uses techniques like Gibbs sampling and Markov Chains. But the underlying principle is straightforward: we're looking for a distinct departure from the way things have been done, a point where the average values before that point are different from the average values after.

And yes, 2001 was a change point year. Since 2001, no winner has consumed fewer than 44 hotdogs (Min value). Before 2001, the record number of hotdogs consumed was 25 and 1/8 (Max value).

I use the [changepoint library](https://www.rdocumentation.org/packages/changepoint/versions/2.2.4) in R. I prefer the "AMOC" method which is "at most one change". I use the Modified Bayes Information Criterion (MBIC) to optimize the calculation.

``` 
require(changepoint)
results <- cpt.mean(y,penalty="MBIC",method="AMOC")
cpts(results)

plot(results,cpt.col="blue",xlab="Year since Start", ylab="Hotdogs and Buns Consumed",cpt.width=4)
```

<figcaption>Tracking hotdog consumption. Made by the author.</figcaption>

Average before Kobayashi: 16.12\ Average after Kobayashi: 62.1

Yeah, he changed the game with his "Solomon method" of dividing the hotdog in half and eating the bun separately.

Later eaters like Joey Chestnut and Miki Sudo expanded on Kobayashi's approach. Chestnut holds the record with 76 hotdogs in 10 mins.

If we allow more than one big change, then we can identify 5 time frames with increasing set points. I use the method "SegNeigh" for binary segmentation. SegNeigh doesn't allow MBIC as a penalty function, so I removed that parameter.

``` 
results <- cpt.mean(y,penalty="None",method="SegNeigh")
cpts(results)

plot(results,cpt.col="blue",cpt.width=4)
```

Even with having multiple set points, Kobayashi's move in 2001 is the most dramatic shift.

So there you go, Nathan's Hot Dog Eating Contest illustrates bayesian change points --- one hot dog at a time.
