# Solution notes/tips (spoilers)

* 1.1 - 2sum, set; `O(n)`

  * Use `visited` set to store each number as you get to it. Check if `target - current` is `in visited`; if it is, return `difference * current`

* 1.2 - 3sum, set; `O(n^2)`

  * Generate the `target - (b + c)` differences, then run 2sum on the list with each difference until one succeeds. Return `difference * b * c`

  * **Exercise: there's an idiomatic `O(n)` two-pointer solution, look it up :)**

* 2.1 - string; `O(n)`

	* Pretty trivial, just parse the rule (could use regex) and validate

* 2.2 - string, xor; `O(n)`

	* For each password, add `(char1 == char) ^ (char2 == char)` to the valid count for ease

* 3 - array2, mod; `O(n)`

	* Index carefully and wrap around horizontally with mod

* 4 - regex; `O(n)`

	* This uses block-oriented input with blocks separated by `\n\n`. Maybe worth rewriting the library to offer this as an option.

* 5.1 - binary; `O(n)`

	* It takes a bit to see that the complicated addressing method is just binary with extra steps. Use string replacement and the builtin `int(n, 2)`.

* 5.2 - binary, math; `O(n)`

	* With Gaussian addition (`n * (n + 1) / 2`), we can find the missing element in a consecutive sequence with elements missing by subtracting the actual sum of the list from the Gaussian total (`gauss(max) - gauss(min)`, since the range starts above 0)

* 6.1 - set; `O(n)`

	* Another block-oriented input one. Fairly simple to just add all the input to a set and return the length

* 6.2 - set; `O(n)`

	* You can do this with set intersection - intersecting all of the people together will yield the answer

	* **Exercise: rewrite this to use ^**

* 7 - regex, graph, search; `O((V + E)^2)`

	* The `regex` library has the nice addition of `match.captures` which returns all matches of the same capture group

	* After parsing the bags, we get the adjacency list of out to in; calculate the reverse to answer part 2.

	* **Exercise: rewrite this recursively with DP to linearize it**

* 8 - vm, queue; `O(n)`, `O(n^2)`

	* Part 2 is a bit annoying; use a queue to keep track of seen `jmp` and `nop`s to try switching them and re-executing from that point with the ins flipped. Also need to keep an execution trace list with the `pc`, current `acc`, and instruction

* 9 - array, 2pointer; `O(n * preamble)`

	* Part 2 is a two-pointer array-range discovery task like "maximum increasing subarray"

	* **Exercise: rewrite this to be correct on all inputs, not just ones where the range doesn't include the preamble**

* 10 - graph, dfs, dp; `O(V + E)`

	* The first one that requires DP to run.

	* **Exercise: convince yourself of the correctness of the mathmatical factorization solutions (here)[https://www.reddit.com/r/adventofcode/comments/ka9pc3/2020_day_10_part_2_suspicious_factorisation/]**

