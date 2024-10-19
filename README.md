# 🐛

# Welcome to Dataville!

As you know, the quiet digital town of Dataville, a peculiar and devastating event had just unfolded—a plague, not of pugs or mugs, but of bugs. These creeping creatures that wormed their way into the town's entire data system, wreaking havoc and bringing it to its knees.

## The Plague 🐞 🐛 🦋 🐝 🐜 🐌 🦗 🕷️ 🦂
The town’s citizens had long relied on their robust DATAVILLE database to keep things running smoothly. Everything from grocery sales to governmental records lived in the system. But one fateful evening, a swarm of these digital bugs emerged from the depths of the system, each bringing a different brand of chaos.

The ladybugs (🐞) were cute but destructive—they managed to munch away the majority of the databases, tables, and records. The inch-worms (🐛) left trails of confusion behind, twisting and reversing the data as they inched. The butterflies (🦋), though elegant, fluttered around the code, disorganizing logic and creating chaos. Bees (🐝) were precise, targeting only encrypted data with their nasty stingers. The ants (🐜) worked systematically but their tiny nibbles consumed critical zeroes. Snails (🐌) shifted sale dates lazily but in their wake left wrong records. The grasshoppers (🦗) leapt through code and kicked up new errors wherever they went. And the scorpions (🦂)? Well, they stole funds leaving the unit prices with fractional cents to cover their tracks.

While the bugs didn’t manage to consume the whole code, they sure left their mark.

## The Aftermath: A Broken Database
Now, with the main database decimated, the citizens of Dataville are in a state of panic. Everything has stopped—sales, inventory tracking, payments. To make matters worse, the town’s backup systems were also partially consumed, leaving only a few corrupted files in the input directory.

But not all hope was lost. A brave intern had been running queries just before the bug invasion. While their queries were incompetent and incomplete, they provided a faint trace of hope for complete restoration. Alongside the intern’s efforts, the senior database architect of Dataville discovered and remembered some important patterns left by the bugs, which will be critical in restoring the database.

## Your Mission: Restore the Past Two Years
You, a legendary bug exterminator, have been called in to save the day. The dictator of Dataville has procured your services to restore the last two fiscal years of records. Here’s what you have to work with:

ID: Every customer ID in the database was a unique integer, all 12 digits long. However, ants (🐜) gnawed away the zeros and then worms (🐛) reversed the remainder of the IDs.

Customer Names: Thanks to Dataville’s strict PII privacy policies, all customer names were encrypted in the database, ensuring that sensitive information stayed protected. However, the bees (🐝) were particularly crafty. With their precision stingers, they managed to selectively sting and eat away the second half of each encrypted name, leaving the encrypted data incomplete.

But the bees didn’t work alone in corrupting the customer names. Another bug the mischievous butterflies (🦋) fluttered into the mess, expanding the truncated bee mess. You see, these butterflies loved literature and beauty, and their obsession led them to expand what remained of the data into fully formed words. However, their logic was whimsical at best, and instead of decrypting the customer names they just left a mess.

To recover the encrypted customer names the architect has instructed you:
For each word in the butterfly's novel mess take each capital letter and if the capital is a consonant, add the next vowel from AEIYOU too.
Ensure no duplicate lowercase vowels appear in the encrypted customer names.
The names were palindrome-protected for top-pot security, which means the encrypted names must create a palindrome.

Sale Dates: The snails (🐌) messed with sale dates by shifting the days forward for each of the days in inventory. You need to roll dates over within the same month when necessary, with overflows starting back at the beginning of the month, to restore the proper sale date.

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

# The Rules

## Use the bug.md file to document your debugging process.

This is a debugging exercise not a see what AI (GPT or co-pilot) can do. Do not just paste the requirements and make new functions, you must identify what and where the bugs are and then discuss how you fixed the bug. Also do not just paste the functions and ask the AI to explain the code to you. You can use AI to help make a solution once you have identified a bug and have a hypothesis how to fix it, similar to how you would have used a google search to look up syntax before.

With that in mind I would recommend not using co-pilot chat during this exercise since it can access more scope that the question you provide. When using GPT ask specific questions and do not tell the AI why you want what you are asking.
