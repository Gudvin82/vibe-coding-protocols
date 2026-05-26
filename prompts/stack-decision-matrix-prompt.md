Выбери стек и объясни, почему он подходит именно для этого проекта.

Нужно дать:
- recommended stack;
- simpler alternative;
- safer production-ready alternative;
- primary database;
- expected growing entities / tables;
- migration strategy;
- index strategy;
- background jobs needed now / later;
- caching needed now / later;
- rate limit / external API quota risks;
- idempotency needs;
- first likely bottleneck;
- what is intentionally deferred.

Не предлагай сложную архитектуру без причины. Но если выбранный путь создает архитектурный тупик при росте, укажи это явно и предложи более устойчивую альтернативу без overengineering.
