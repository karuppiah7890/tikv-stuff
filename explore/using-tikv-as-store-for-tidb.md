
I'm wondering how TiDB uses TiKV as it's store backend. I mean, that's what I read, I need to check and research more. But, TiDB is a RDBMS and TiKV is a KV store with Transactional capabilities too. I'm just wondering how it all ties up together

Also, TiKV uses RocksDB underneath. RocksDB uses LevelDB underneath. It's like a lot of layers :P

I'm wondering what each layer does! It would be good to see the talks on these softwares, especially introductory ones, where they talk about the "why" and how the project was born :D The story behind these softwares that is. I think there are some for RocksDB. Gotta check for others

Now, why do I wonder about these layers? Well, TiDB is like I said RDBMS, it does stuff in the form of tables. It's MySQL. SQL. So there will be tables, rows, columns. Not sure if TiDB supports joins, something to check, I think it does or maybe they don't support all the MySQL API and features, which is probably okay if their aim is not that. Every project has it's own aim

So, TiKV is KV store. How does TiDB convert it's RDBMS data to the form a KV is the question I had. I mean, it's possible to do it, I can probably think of some ways if I spend time on it. I want to understand how TiDB does it and I was wondering if the whole thing is efficient and optimized. I mean, if TiKV is meant to be optimized for KV store, it will be performant when used as a KV store. But how can TiDB be performant if it translates it's table, row, column data to KV and store it in TiKV and does the same while reading back? Can it be performant? RocksDB and LevelsDB also seem to be all KV stores

I was also wondering if it's possible for any store to be performant with just a KV store or some other store as backend. All the translations and what not. Also, the access of data to read and write from the disk, all that stuff. I was wondering how someone can model one kind of data (tables, rows, columns) to a different kind of data (kv pairs) and still keep things optimal

Also, is it possible to do it with other kinds of data too? Like Graph database on top of KV store? Document store / Document database on top of KV store? Search Engine (like ElasticSearch) / Full text search database on top of KV store? Spatial data supported database on top of KV store?

Something to ponder about, hmm
