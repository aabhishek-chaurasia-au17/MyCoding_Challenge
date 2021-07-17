
"""
Q-1 ) Design Tiny Url and explain all the steps and estimations. (5 marks)
"""


"""
URL shortening is used to create shorter aliases for long URLs. We call these shortened aliases “short links.” Users are redirected to the original URL when they hit these short links. Short links save a lot of space when displayed, printed, messaged, or tweeted. Additionally, users are less likely to mistype shorter URLs.
Bandwidth estimates: For write requests, since we expect 200 new URLs every second, total incoming data for our 
service will be 100KB per second:
200 * 500 bytes = 100 KB/s
For read requests, since every second we expect ~20K URLs redirections, total outgoing data for our service would 
be 10MB per second:
20K * 500 bytes = ~10 MB/s
Memory estimates: If we want to cache some of the hot URLs that are frequently accessed, how much memory will we
 need to store them? If we follow the 80-20 rule, meaning 20% of URLs generate 80% of traffic, we would like to 
 cache these 20% hot URLs.
Since we have 20K requests per second, we will be getting 1.7 billion requests per day:
20K * 3600 seconds * 24 hours = ~1.7 billion
To cache 20% of these requests, we will need 170GB of memory.
0.2 * 1.7 billion * 500 bytes = ~170GB
One thing to note here is that since there will be many duplicate requests (of the same URL), our actual memory
 usage will be less than 170GB.
"""







