# 🐛

## About

> A Python debugging exercise that I developed for a workshop. I started with a presentation on strategies and best practices for debugging, then provided each participant with the [plague](https://github.com/tnjordan/bug/tree/plague) branch in a new repository so they couldn't reverse anything out of the Git history.
> 
> The instructions below were provided and, like real life, they are occasionally vague and ambiguous, requiring investigation and testing to fill in the details.
> 
> [A favorite bug](https://github.com/tnjordan/bug/blob/2b2ef848ee970329cd8402a430c436378ae4e421/test/test.py#L17)
> 
> The whimiscal story for the debugging exercise was inspired by my love of [Advent of Code](https://adventofcode.com/) puzzles.

# Welcome to Dataville!

As you know, in the quiet digital town of Dataville, a peculiar and devastating event has just unfolded—a plague, not of rats or locusts, but of bugs. These creeping creatures have wormed their way into the town's entire data system, wreaking havoc and bringing the town to its knees.

## The Plague 🐞 🐛 🦋 🐝 🐜 🐌 🦗 🕷️ 🦂
The town’s citizens had long relied on their robust database to keep things running smoothly. Everything from grocery sales to governmental records lived in the system. But one fateful evening, a swarm of these digital bugs emerged from the depths of the system, each bringing a different brand of chaos.

The ladybugs (🐞) were cute but destructive—they managed to munch away the majority of the databases, tables, and records. The worms (🐛) left trails of confusion behind, twisting and reversing numbers. The butterflies (🦋), though elegant, fluttered around the code, disorganizing logic and creating chaos. Bees (🐝) were precise, targeting only encrypted data with their nasty stingers. The ants (🐜) worked systematically but their tiny nibbles took critical zeroes off. Snails (🐌) shifted sale dates lazily but in their wake left wrong records. The grasshoppers (🦗) leapt through code and kicked up new errors wherever they went. And the scorpions (🦂)? Well, they stole funds leaving the unit prices with fractional cents to cover their tracks.

While the bugs didn’t manage to consume the whole code, they sure left their mark.

## The Aftermath: A Broken Database
Now, with the main database decimated, the citizens of Dataville are in a state of panic. Everything has stopped—sales, inventory tracking, payments. To make matters worse, the town’s backup systems were also partially consumed, leaving only a few corrupted files in the input directory.

But not all hope was lost. A brave intern had been running queries just before the bug invasion. While their queries were incompetent and incomplete, it provided a faint trace of hope for restoration. Alongside the intern’s efforts, the senior database architect of Dataville discovered some important patterns left by the bugs, which will be critical in restoring the database.

## Your Mission: Restore the Past Two Years
You, a legendary bug exterminator, have been called in to save the day. The dictator of Dataville has demanded you to restore the last two fiscal years of records. Here’s what you have to work with:

ID Fix: Every customer ID in the database was a unique integer, 12 digits long. However, ants (🐜) gnawed away the zeros and then worms (🐛) reversed the digits of the IDs.

Customer Names: Thanks to Dataville’s strict PII privacy policies, all customer names were encrypted in the database, ensuring that sensitive information stayed protected. However, the bees (🐝) were particularly crafty. With their precision stingers, they managed to selectively sting and eat away the second half of each encrypted name, leaving the encrypted data incomplete.

But the bees didn’t work alone in corrupting the customer names. Another bug—the mischievous butterflies (🦋) fluttered into the mess, expanding the truncated, encrypted words into full names. These butterflies loved literature and beauty, and their obsession led them to expand what remained of the encrypted data into fully formed words. However, their logic was whimsical at best, and instead of restoring the original names they just left a mess.

To recover the encrypted customer names the architect has instructed you:
For each word in the butterfly's novel mess take each capital letter and if the capital is a consonant, add the next vowel from AEIYOU too.
Ensure no duplicate lowercase vowels appear in the restored names.
The names were palindrome-protected for top-pot security, which means the encrypted names must create a palindrome.

Sale Dates: The snails (🐌) messed with sale dates by shifting the days forward by the number of days in inventory. You need to roll dates over within the same month when necessary, with overflows starting back at the beginning of the month, to restore the proper sale date.

Unit Prices: Finally, the scorpions (🦂) have tampered with item prices by sneaking away fractional cents per item. These pesky critters only took or sometimes left alone full cents. You need to figure out what the correct total sale price was for each transaction.

Inventory Dates: Unfortunately, the spiders (🕷️) were ruthless. They didn’t just corrupt the inventory dates—they devoured them entirely, leaving behind nothing but bits of tangled webbing. With no actual dates left, you must rely on the days in inventory field to calculate when each item was first added to inventory.

## The Town’s Financial Crisis: Reconcile the Accounts
The havoc these bugs caused wasn’t limited to corrupting names and dates. There’s also a more pressing problem the bugs stole money!

The Dataville accountants need your help to reconcile their accounts. You must analyze the corrupted price entries and determine exactly how much money was stolen by the scorpions each month. This will allow you to correct the financial records and ensure the world is in balance again.

But that’s not all the senior database architect has one more request: identify the top customers based on sales records. These high-value customers are the leadership's top priority, and their accounts need to be restored as quickly as possible. By analyzing the sales data, you’ll be able to highlight the most important clients.

## The Debugging Challenge: Help the Intern
The enthusiastic intern left has already started working, but their code is riddled with bugs. You’ll need to go through the code, clean it up, and restore the necessary data. 

## The Final Task
After everything from IDs, customer names, sale dates, and inventory dates is repaired (or cleverly reconstructed), your final mission is to trace the stolen money and exterminate all bugs, you will ensure that Dataville not only survives the bug plague but comes out stronger than ever.

The town's proletariat are counting on you, and your family is too.
